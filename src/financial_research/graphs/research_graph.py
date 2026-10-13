from langgraph.graph import StateGraph, START, END

from financial_research.state.fin_schemas import ResearchState
from financial_research.nodes.financial_node import fin_stmt_node

graph = StateGraph(ResearchState)

graph.add_node(
    "financial_statement",
    fin_stmt_node,
)

graph.add_edge(
    START,
    "financial_statement",
)

graph.add_edge(
    "financial_statement",
    END,
)

research = graph.compile()