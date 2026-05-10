# Content Usage Analyzer

A tool for automatically tracking how a given article is cited, shared, and reused across the web. The script generates targeted search queries, scrapes results via Tavily AI, classifies each page using an LLM, and produces a structured Markdown report.

---

## How It Works

```
Source article
      │
      ▼
[1] Query generation (LLM)
      │  40 queries across Reddit, Quora, X/Twitter, and general web
      ▼
[2] Search & scraping (Tavily AI)
      │  Up to 4 results per query, deduplicated by URL
      ▼
[3] Filtering
      │  Discard paywalls, 404 errors, and pages with too little content
      ▼
[4] Classification (LLM)
      │  6 usage categories + confidence level
      ▼
[5] Markdown report
```

---

## Installation

### Requirements

- Python 3.10+
- API keys for [OpenRouter](https://openrouter.ai/) and [Tavily](https://tavily.com/)

### Steps

```bash
git clone https://github.com/your-username/content-usage-analyzer.git
cd content-usage-analyzer

uv add openai tavily-python httpx python-dotenv
```

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=sk-or-...
TAVILY_API_KEY=tvly-...
```

---

## Usage

1. Place the article you want to analyze in a text file (default: `dyatlow.txt`).
2. Run the script:

```bash
uv run main.py
```

3. The report will be saved to `report_final.md`.

### Changing the source file or query count

At the top of `main.py` you'll find the configuration variables:

```python
ARTICLE_FILE = "dyatlow.txt"   # source article file
NUM_QUERIES  = 40              # number of search queries to generate
OUTPUT_FILE  = "report_final.md"
```

---

## Project Structure

```
.
├── main.py            # main script
├── dyatlow.txt        # example source article
├── report_final.md    # generated report (after running)
├── .env               # API keys (do not commit!)
└── README.md
```

---

## Classification Categories

Every page found is assigned to one of the following categories:

| Category | Description |
|---|---|
| `original_content` | Identical content reproduced without changes |
| `direct_citation` | Explicitly quotes or links to the source article |
| `discussion` | Discusses the same topic with its own analysis |
| `indirect_reuse` | Uses conclusions from the source without attribution |
| `topic_mention` | Mentions the topic in passing; source is not a reference |
| `unrelated` | No meaningful connection to the source article |

Each classification also includes a confidence level: `high`, `medium`, or `low`.

---

## LLM Models

The script uses two models via OpenRouter with automatic rotation and error handling:

- `openai/gpt-oss-20b:free`
- `openai/gpt-oss-120b:free`

If a rate limit or timeout is hit, the script automatically falls back to the next model.

---

## Known Limitations

- Pages behind paywalls or login walls are automatically discarded.
- Free models on OpenRouter may be unavailable during peak hours — the script retries automatically but cannot guarantee 100% success.
- Tavily may return limited results for very niche queries.
