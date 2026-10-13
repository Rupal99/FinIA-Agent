from tavily import TavilyClient
from dotenv import load_dotenv
import os

from news.state.news_schemas import NewsState

print("News Research Node is being initialized...")
load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

async def news_research_node(state: NewsState):
    print("Executing news research node for company:", state["company_name"])
    if not TAVILY_API_KEY:
        raise ValueError("TAVILY_API_KEY is not set")
    print("TAVILY_API_KEY is set, proceeding with news research...")
    client = TavilyClient(TAVILY_API_KEY)
    response = client.search(
        query=f"{state['company_name']} latest financial news",
        search_depth="advanced"
    )
    #print("News node state:", state["company_name"])
    #print("News Research Result:", response)
    return { "latest_news": str(response)}
