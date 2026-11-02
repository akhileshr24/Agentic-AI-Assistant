
from dotenv import load_dotenv

# Load environment variables before importing tools
load_dotenv()

from langchain_groq import ChatGroq
from langchain.agents import create_agent

from tools.search_tool import search_tool
from tools.weather_tool import get_weather_data
from tools.wikipedia_tool import wikipedia_search
from prompts.system_prompt import SYSTEM_PROMPT


def build_agent():
    """Create and return the LangChain agent."""

    # Initialize Groq LLM
    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0,
        max_tokens=512,
    )

    # Register available tools
    tools = [
        search_tool,
        get_weather_data,
        wikipedia_search,
    ]

    # Create LangChain agent
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )

    return agent
