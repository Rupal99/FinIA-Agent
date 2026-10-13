from typing_extensions import TypedDict 
from financial_research.state.fin_schemas import financial_statement
from typing import Annotated


def keep_first(a: str, b: str) -> str:
    return a or b

class InputState(TypedDict):
    user_message: str
    company_name: Annotated[str, keep_first]
    intention: str
    latest_news: str
    final_report: str
    financial_statement: financial_statement

