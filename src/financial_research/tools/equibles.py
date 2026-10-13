import os

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

equibles_api_key = os.getenv("EQUIBLES_API_KEY")

if not equibles_api_key:
    raise ValueError("EQUIBLES_API_KEY is not set")

client = MultiServerMCPClient(
    {
        "equibles": {
            "transport": "http",
            "url": "https://mcp.equibles.com/mcp",
            "headers": {
                "Authorization": f"Bearer {equibles_api_key}"
            },
        }
    }
)

