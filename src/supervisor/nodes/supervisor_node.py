import os
import json

from dotenv import load_dotenv
from groq import Groq
from supervisor.state.input_schema import InputState

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None


def supervisor_node(state: InputState):
    print("Executing supervisor node for user message:", state["user_message"])

    if not client:
        raise ValueError("GROQ_API_KEY is not set in the .env file")

    # Get the user's original query
    user_message = state["user_message"]

    # Instruct the LLM to extract the company ticker and research intention
    system_prompt = """
    You are a financial research query parser.

    Extract two fields from the user's message:

    1. company_name:
       - Return the company's official stock ticker (e.g., Apple -> AAPL).
       - Prefer its primary stock listing.
       - If the company cannot be identified confidently, return "UNKNOWN".

    2. intention:
       - Clearly describe what the user wants to research or evaluate.
       - Preserve relevant metrics, time periods, and constraints.
       - Do not answer the user's question; only interpret it.

    Return a JSON object with exactly these two string fields:
    {
        "company_name": "...",
        "intention": "..."
    }

    Return JSON only, without Markdown formatting.
    """

    # Call Groq
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0,
        response_format={"type": "json_object"}
    )

    # Parse the LLM response into a Python dictionary
    result = json.loads(response.choices[0].message.content)
    
    # Update the LangGraph state with the extracted values
    return {
        "company_name": result["company_name"],
        "intention": result["intention"]
    }