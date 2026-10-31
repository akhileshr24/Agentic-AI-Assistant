
import requests
from langchain_core.tools import tool

WIKIPEDIA_API = "https://en.wikipedia.org/w/api.php"

HEADERS = {
    "User-Agent": "AgenticAISingleAgent/1.0 (educational project)"
}


@tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia and retrieve article summaries and source URLs."""

    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": query,
        "gsrlimit": 2,
        "prop": "extracts|info",
        "exintro": True,
        "explaintext": True,
        "exsentences": 4,
        "inprop": "url",
        "format": "json",
        "formatversion": 2,
    }

    try:
        response = requests.get(
            WIKIPEDIA_API,
            params=params,
            headers=HEADERS,
            timeout=15,
        )

        if response.status_code == 429:
            return "Wikipedia is temporarily rate-limiting requests. Try again later."

        response.raise_for_status()

        data = response.json()
        pages = data.get("query", {}).get("pages", [])

        if not pages:
            return "No relevant Wikipedia articles found."

        results = []

        for page in pages:
            results.append(
                f"Title: {page.get('title', 'Unknown')}\n"
                f"Summary: {page.get('extract', 'No summary available.')}\n"
                f"Source: {page.get('fullurl', 'URL unavailable')}"
            )

        return "\n\n".join(results)

    except requests.RequestException as error:
        return f"Wikipedia request failed: {error}"
    except (ValueError, TypeError, KeyError) as error:
        return f"Could not process Wikipedia response: {error}"
