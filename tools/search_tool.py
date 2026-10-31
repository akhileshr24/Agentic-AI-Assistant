
from langchain_tavily import TavilySearch

# Initialize Tavily search tool
search_tool = TavilySearch(
    max_results=3,
    topic="general",
)
