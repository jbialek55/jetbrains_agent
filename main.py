import json
import time
import re
import os
from pathlib import Path
from dotenv import load_dotenv  # Importujemy obsługę .env
from openai import OpenAI
from tavily import TavilyClient

# ── Ładowanie zmiennych środowiskowych ────────────────────────────────────────
load_dotenv()

OR_API_KEY = os.getenv("OPENROUTER_API_KEY")
TV_API_KEY = os.getenv("TAVILY_API_KEY")
# ── Config ────────────────────────────────────────────────────────────────────

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OR_API_KEY,
    timeout=30,
)

tavily = TavilyClient(api_key=TV_API_KEY)

MODEL_NAME     = "google/gemma-3-27b-it:free"
ARTICLE_FILE   = "dyatlow.txt"
NUM_QUERIES    = 6          
OUTPUT_FILE    = "report_final.md"

# ── Utils ─────────────────────────────────────────────────────────────────────

def ask_llm(prompt: str) -> str:
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a professional data extractor. You ALWAYS respond with VALID JSON. No prose, no explanations."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,

            )
            raw = response.choices[0].message.content
            print(f"   [DEBUG] Raw response: {raw[:200]}")  # <-- dodaj to
            return raw
        except Exception as e:
            print(f"   [DEBUG] Full error: {repr(e)}")  # repr zamiast str
            if "429" in str(e) and attempt < max_retries - 1:
                wait = 30 * (attempt + 1)  # rosnące czekanie: 30s, 60s
                print(f"Rate limit. Czekam {wait}s...")
                time.sleep(wait)
                continue
            return "{}"
    return "{}"

def clean_json_string(raw: str) -> str:
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    return match.group() if match else "{}"

# ── Step 1: Generate search queries ──────────────────────────────────────────

def generate_queries(article: str) -> dict:
    print("Step 1/3 — Analyzing FULL article and generating targeted queries...")
    
    prompt = f"""Based on the article below, generate exactly {NUM_QUERIES} search queries.
    
    CRITICAL INSTRUCTIONS:
    - 2 queries must focus on Reddit using 'site:reddit.com'
    - 1 query must focus on Quora using 'site:quora.com'
    - 1 query must focus on X/Twitter using 'site:x.com'
    - 2 queries should be general academic/forensic searches.

    Format the output as a JSON object with keys "queries" and "summary".

    ARTICLE:
    {article}
    """
    
    raw = ask_llm(prompt)
    try:
        return json.loads(clean_json_string(raw))
    except:
        print("   ⚠ Failed to parse JSON, using fallback.")
        return {
            "queries": ["Dyatlov Pass avalanche site:reddit.com", "Dyatlov Pass investigation site:x.com"],
            "summary": "Full article analysis."
        }

# ── Step 2: Search & Scrape via Tavily ────────────────────────────────────────

def search_and_scrape(queries: list) -> list[dict]:
    print(f"Step 2/3 — Searching and Scraping with Tavily AI...")
    results = []
    seen_urls = set()

    for i, q in enumerate(queries):
        print(f"   [{i+1}/{len(queries)}] Tavily is searching: {q}...")
        try:
            response = tavily.search(query=q, search_depth="advanced", include_raw_content=True, max_results=2)
            
            for res in response.get('results', []):
                url = res.get('url')
                if url not in seen_urls:
                    seen_urls.add(url)
                    results.append({
                        "url": url,
                        "title": res.get('title'),
                        "page_content": res.get('raw_content') or res.get('content'),
                    })
        except Exception as e:
            print(f" Tavily Error: {e}")
    
    return results

# ── Step 3: Classify (Full Comparison) ────────────────────────────────────────

def classify(result: dict, full_article: str) -> dict:
    prompt = f"""COMPARE THESE TWO DOCUMENTS IN FULL:

    SOURCE RESEARCH:
    {full_article}

    WEBPAGE CONTENT (from {result['url']}):
    {result['page_content']}

    TASK:
    Analyze how the Webpage uses the Source Research. 
    Be very specific in your summary.
    Return JSON ONLY:
    {{
      "related": true,
      "usage_type": "direct_citation | discussion | idea_reuse | topic_mention | unrelated | original_article",
      "summary": "Detailed explanation of the relationship"
    }}
    """
    try:
        raw = ask_llm(prompt)
        return json.loads(clean_json_string(raw))
    except:
        return {"related": False, "usage_type": "error", "summary": "Failed to analyze full content."}

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    path = Path(ARTICLE_FILE)
    if not path.exists():
        print(f"File {ARTICLE_FILE} not found.")
        return

    article_content = path.read_text(encoding="utf-8")
    
    meta = generate_queries(article_content)
    queries = meta.get("queries", [])
    
    search_results = search_and_scrape(queries)

    print(f"Step 3/3 — Classifying {len(search_results)} results (Full text mode)...")
    for i, res in enumerate(search_results):
        print(f"   [{i+1}/{len(search_results)}] Analyzing full page: {res['url'][:50]}...")
        res["cls"] = classify(res, article_content)
        # Małe opóźnienie, aby nie przeciążyć darmowego API OpenRouter
        time.sleep(1)

    print("Generating report...")
    related = [r for r in search_results if r.get("cls", {}).get("related")]
    
    report_header = f"# Tavily Content Analysis: Dyatlov Pass (FULL TEXT MODE)\n\n"
    report_summary = f"## Research Summary\n{meta.get('summary', 'Analysis performed on full document.')}\n\n"
    
    items = ""
    for i, r in enumerate(related, 1):
        items += f"### {i}. {r['title']}\n"
        items += f"- **URL:** {r['url']}\n"
        items += f"- **Type:** {r['cls'].get('usage_type')}\n"
        items += f"- **Detailed Insight:** {r['cls'].get('summary')}\n\n"
    
    Path(OUTPUT_FILE).write_text(report_header + report_summary + items, encoding="utf-8")
    print(f"\nDone! Full report saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()