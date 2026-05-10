# Content Usage Tracker

An automated system designed to track and analyze how specific articles (scientific papers, investigative journalism, or blog posts) are reused, cited, or discussed across the web. The tool leverages Agentic AI (LLMs) and advanced semantic search (Tavily AI) to identify direct citations, informal discussions, and uncredited content reuse.

## Key Features

*   **Automated Query Generation**: Based on the source article (`.txt`), the LLM generates dozens of targeted search queries optimized for specific platforms (Reddit, Quora, X/Twitter, and academic hubs).
*   **Deep Web Scraping**: Integration with Tavily AI allows the script to bypass surface-level results and fetch raw content for deep analysis.
*   **Semantic Classification**: Instead of simple keyword matching, each found page is analyzed by an LLM against a 6-category taxonomy:
    *   `original_content`: Verbatim reproduction of the source.
    *   `direct_citation`: Explicitly quotes or links to the source.
    *   `discussion`: Independent analysis of the same topic.
    *   `indirect_reuse`: Uses findings/conclusions without attribution.
    *   `topic_mention`: Passing reference to the subject.
    *   `unrelated`: Discarded results.
*   **Comprehensive Reporting**: Generates a detailed `report_final.md` including statistical summaries, evidence quotes, and confidence scoring.

##  Technology Stack

*   **Language**: Python 3.14+
*   **Orchestration**: OpenAI SDK (compatible with OpenRouter for model rotation).
*   **Search Engine**: [Tavily AI](https://tavily.com/) (Optimized for LLM agents).
*   **Models**: Supports high-parameter models via OpenRouter to ensure high classification accuracy.
