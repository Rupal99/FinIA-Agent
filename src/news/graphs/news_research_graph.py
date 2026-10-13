from langgraph.graph import START, END, StateGraph
from news.state.news_schemas import NewsState
from news.nodes.news_research_node import news_research_node

print("News Research Graph is being compiled...")
graph = StateGraph(NewsState)

graph.add_node( 
    "news_research",
    news_research_node
)

graph.add_edge(
    START,
    "news_research",
)

graph.add_edge(
    "news_research",
    END,
)
news_research = graph.compile()
