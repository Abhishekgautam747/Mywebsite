import json
from datetime import datetime, timezone

def fetch_and_rank_news():
    # TODO: REPLACE THIS with your real logic:
    # scrape APIs, compute impact_score, categorize into critical/high/medium
    critical = []
    high = []
    medium = []

    # Example dummy item – replace this whole function with your code
    critical.append({
        "title": "Dummy critical headline",
        "summary": "This is a placeholder. Replace with real summary.",
        "impact_score": 9.2,
        "regions": ["Global"],
        "sectors": ["Economy"],
        "source": "Example Source",
        "link": "https://example.com/article"
    })

    return {
        "critical": critical,
        "high": high,
        "medium": medium
    }

def main():
    data = fetch_and_rank_news()
    data["generated_at"] = datetime.now(timezone.utc).isoformat()

    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
