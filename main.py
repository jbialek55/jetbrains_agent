import json
import time
import re
import os
import httpx
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from tavily import TavilyClient
import random
load_dotenv()

OR_API_KEY = os.getenv("OPENROUTER_API_KEY")
TV_API_KEY = os.getenv("TAVILY_API_KEY")
MODELS = [
    "openai/gpt-oss-20b:free",
    "openai/gpt-oss-120b:free",
]

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OR_API_KEY,
    http_client=httpx.Client(
        timeout=httpx.Timeout(
            connect=10.0,
            read=45.0,
            write=10.0,
            pool=5.0,
        )
    ),
)


tavily = TavilyClient(api_key=TV_API_KEY)

ARTICLE_FILE = "dyatlow.txt"
NUM_QUERIES = 40
OUTPUT_FILE = "report_final.md"



def ask_llm(prompt: str) -> str:
    attempts = []
    models = MODELS.copy()
    random.shuffle(models)
    for model in models:
        attempts.append((model, 1))
        attempts.append((model, 2))

    for model, attempt_num in attempts:
        try:
            print(f"   [LLM] Attempting with model: {model} (attempt {attempt_num})")
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a professional data extractor. You ALWAYS respond with VALID JSON. No prose, no explanations."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
            )
            raw = response.choices[0].message.content
            print(f"   [LLM] OK — {model} responded ({len(raw)} characters)")
            return raw

        except (httpx.TimeoutException, httpx.ReadTimeout,
                httpx.ConnectTimeout, httpx.PoolTimeout) as e:
            print(f"   [LLM] TIMEOUT ({type(e).__name__}) — {model}, skipping to next model...")
            continue

        except Exception as e:
            err = str(e)
            if "429" in err or "rate" in err.lower():
                wait = 10 * attempt_num
                print(f"   [LLM] Rate limit hit — {model}. Waiting {wait}s...")
                time.sleep(wait)
                continue
            elif "404" in err or "No endpoints" in err:
                print(f"   [LLM] Model unavailable — {model}, skipping to next model...")
                continue
            else:
                print(f"   [LLM] Error — {model}: {repr(e)}, skipping to next model...")
                continue

    print("   [LLM] All models failed. Returning empty JSON object.")
    return "{}"



def clean_json_string(raw: str) -> str:
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    return match.group() if match else "{}"



def generate_queries(article: str) -> dict:
    print("Step 1/3 — Analyzing article and generating targeted queries...")
    prompt = f"""Based on the article below, generate exactly {NUM_QUERIES} search queries.

CRITICAL INSTRUCTIONS:
Return a JSON object with keys "queries" and "summary".

"queries" must be a list of objects, each with:
  - "q": the search query text (WITHOUT any site: operators)
  - "domain": one of "reddit.com", "quora.com", "x.com", or null for general search

Distribution:
- 10 queries with domain "reddit.com"
- 8 query with domain "quora.com"
- 8 query with domain "x.com"
- remaining queries with domain null (general/academic)

"summary" must be 3-4 sentences describing:
- main topic of the article
- key claims or findings
- why it's notable or controversial

ARTICLE:
{article}
"""
    raw = ask_llm(prompt)
    try:
        parsed = json.loads(clean_json_string(raw))
        queries = parsed.get("queries", [])
        if not queries:
            raise ValueError("No queries found in the response")
        print(f"   Successfully generated {len(queries)} queries.")
        return parsed
    except Exception as e:
        print(f"   ⚠ Failed to parse JSON ({e}). Utilizing fallback queries.")
        return {
            "queries": [
                {"q": "Dyatlov Pass avalanche evidence",         "domain": "reddit.com"},
                {"q": "Dyatlov Pass mystery theories",           "domain": "reddit.com"},
                {"q": "Dyatlov Pass what really happened",       "domain": "quora.com"},
                {"q": "Dyatlov Pass incident",                   "domain": "x.com"},
                {"q": "Dyatlov Pass forensic analysis",          "domain": None},
                {"q": "Dyatlov Pass infrasound hypothesis",      "domain": None},
            ],
            "summary": "Fallback queries — LLM failed to respond."
        }



def search_and_scrape(queries: list) -> list[dict]:
    print(f"Step 2/3 — Searching and Scraping with Tavily AI...")
    results = []
    seen_urls = set()

    for i, q in enumerate(queries):
        if isinstance(q, dict):
            clean_query = q.get("q", "").strip()
            domain = q.get("domain")
            include_domains = [domain] if domain else []
        else:
            domain_map = {
                "site:reddit.com": "reddit.com",
                "site:quora.com":  "quora.com",
                "site:x.com":      "x.com",
            }
            include_domains = []
            clean_query = q
            for marker, domain in domain_map.items():
                if marker in q:
                    include_domains = [domain]
                    clean_query = q.replace(marker, "").strip()
                    break

        if not clean_query:
            print(f"   [{i+1}/{len(queries)}] Empty query, skipping.")
            continue

        domain_label = include_domains[0] if include_domains else "general"
        print(f"   [{i+1}/{len(queries)}] [{domain_label}] {clean_query}")

        try:
            response = tavily.search(
                query=clean_query,
                search_depth="advanced",
                include_raw_content=True,
                max_results=4,
                include_domains=include_domains if include_domains else None,
            )
            for res in response.get('results', []):
                url = res.get('url')
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    results.append({
                        "url": url,
                        "title": res.get('title', 'No title'),
                        "page_content": (res.get('raw_content') or res.get('content') or ""),
                    })
        except Exception as e:
            print(f"   Tavily Error: {e}")

    print(f"   Collected {len(results)} unique pages.")
    return results


MIN_CONTENT_LENGTH = 500


def filter_results(results: list[dict]) -> list[dict]:
    filtered = []
    for r in results:
        content = r.get("page_content") or ""
        length = len(content.strip())

        if length < MIN_CONTENT_LENGTH:
            print(f"   [FILTER] Discarded (insufficient content: {length} characters): {r['url'][:60]}")
            continue

        red_flags = [
            "access denied", "403 forbidden", "404 not found",
            "sign in to continue", "please log in", "enable javascript",
            "subscribe to read", "create an account",
        ]
        content_lower = content.lower()
        flagged = any(flag in content_lower for flag in red_flags)
        if flagged:
            print(f"   [FILTER] Discarded (paywall/error detected): {r['url'][:60]}")
            continue

        filtered.append(r)

    print(f"   [FILTER] Kept {len(filtered)}/{len(results)} results after filtering.")
    return filtered


def classify(result: dict, full_article: str) -> dict:
    prompt = f"""You are an academic research analyst. Your task is to determine how a webpage references or uses a source article.

SOURCE ARTICLE (the original content being tracked):
{full_article}

WEBPAGE TO ANALYZE (URL: {result['url']}):
{str(result['page_content'])}

INSTRUCTIONS:
Carefully compare both texts and return a JSON object with these exact fields:

{{
  "related": true or false,
  "confidence": "high | medium | low",
  "usage_type": one of:
    "original_content"     - original article content without any changes
    "direct_citation"      - quotes or explicitly cites the source article by name or URL,
    "discussion"           - discusses the same topic with own analysis, source may be implicit,
    "indirect_reuse"       - uses conclusions or findings from the source without attribution,
    "topic_mention"        - mentions the same topic in passing but source is not a reference,
    "unrelated"            - content is not meaningfully related to the source article,
  "evidence": "Quote or paraphrase from the WEBPAGE that best proves your classification (max 2 sentences)",
  "summary": "2-3 sentence explanation of the relationship between the two texts"
}}

RULES:
- Base your answer ONLY on the text provided, not on prior knowledge.
- If the webpage does not mention any concept from the source article, set related to false.
- Be conservative: prefer lower confidence when unsure.
- Return ONLY the JSON object, no markdown, no explanation outside it.
"""
    try:
        raw = ask_llm(prompt)
        return json.loads(clean_json_string(raw))
    except Exception:
        return {
            "related": False,
            "confidence": "low",
            "usage_type": "error",
            "evidence": "",
            "summary": "Failed to analyze."
        }

def generate_report(meta: dict, search_results: list[dict], article_file: str) -> str:
    related = [r for r in search_results if r.get("cls", {}).get("related")]
    unrelated = [r for r in search_results if not r.get("cls", {}).get("related")]
    total = len(search_results)

    by_type = {}
    by_confidence = {"high": 0, "medium": 0, "low": 0}
    for r in related:
        t = r['cls'].get('usage_type', 'unknown')
        by_type[t] = by_type.get(t, 0) + 1
        c = r['cls'].get('confidence', 'low')
        by_confidence[c] = by_confidence.get(c, 0) + 1

    report = f"# Content Usage Analysis: {article_file}\n\n"
    
    report += "## Methodology\n\n"
    report += f"1. **Source article**: `{article_file}` — analyzed in full\n"
    report += f"2. **Query generation**: LLM ({len(MODELS)} models with random rotation) generated {NUM_QUERIES} targeted search queries covering Reddit, Quora, X/Twitter, and academic sources\n"
    report += f"3. **Search & scrape**: Tavily AI (`search_depth=advanced`) retrieved up to 4 results per query, deduplicated by URL\n"
    report += f"4. **Filtering**: Pages with fewer than {MIN_CONTENT_LENGTH} characters or paywall/error indicators were discarded\n"
    report += f"5. **Classification**: Each page compared to source article by LLM using 6-category taxonomy with confidence scoring\n"
    report += f"6. **Models used**: {', '.join(MODELS)}\n\n"

    report += "## Statistics\n\n"
    report += f"- Pages analyzed: {total}\n"
    report += f"- Related found: {len(related)} ({len(related) * 100 // total if total else 0}%)\n"
    report += f"- Unrelated / discarded: {len(unrelated)}\n\n"
    report += "**By usage type:**\n"
    for t, count in sorted(by_type.items(), key=lambda x: -x[1]):
        report += f"- `{t}`: {count}\n"
    report += "\n**By confidence:**\n"
    for c in ["high", "medium", "low"]:
        report += f"- {c}: {by_confidence[c]}\n"
    report += "\n"

    report += f"## Research Summary\n\n{meta.get('summary', 'N/A')}\n\n"

    report += f"## Related Pages ({len(related)})\n\n"
    for i, r in enumerate(related, 1):
        cls = r['cls']
        report += f"### {i}. {r['title']}\n"
        report += f"- **URL:** {r['url']}\n"
        report += f"- **Usage type:** `{cls.get('usage_type')}`\n"
        report += f"- **Confidence:** {cls.get('confidence')}\n"
        report += f"- **Evidence:** {cls.get('evidence')}\n"
        report += f"- **Summary:** {cls.get('summary')}\n\n"


    report += f"## Discarded as Unrelated ({len(unrelated)})\n\n"
    for r in unrelated:
        report += f"- [{r['title']}]({r['url']}) — `{r['cls'].get('usage_type', 'n/a')}`\n"

    return report

def main():
    path = Path(ARTICLE_FILE)
    if not path.exists():
        print(f"File {ARTICLE_FILE} does not exist.")
        return

    article_content = path.read_text(encoding="utf-8")

    meta = generate_queries(article_content)
    queries = meta.get("queries", [])

    search_results = search_and_scrape(queries)
    search_results = filter_results(search_results)

    print(f"Step 3/3 — Classifying {len(search_results)} results...")
    for i, res in enumerate(search_results):
        print(f"   [{i + 1}/{len(search_results)}] Analyzing: {res['url'][:60]}...")
        res["cls"] = classify(res, article_content)
        time.sleep(1)

    print("Generating report...")
    report = generate_report(meta, search_results, ARTICLE_FILE)
    Path(OUTPUT_FILE).write_text(report, encoding="utf-8")
    print(f"\nDone! Report successfully saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
