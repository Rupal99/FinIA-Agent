from IPython.display import display, Image
from langgraph.graph import END, START, StateGraph

from supervisor.state.input_schema import InputState
from news.graphs.news_research_graph import news_research
from financial_research.graphs.research_graph import research
from supervisor.nodes.supervisor_node import supervisor_node
from final_report.nodes.final_report_node import final_report_node

print("Supervisor Graph is being initialized...")

graph=StateGraph(InputState)

graph.add_node("supervisor", supervisor_node)
graph.add_node("financial_research", research)
graph.add_node("news_research", news_research)
graph.add_node("final_report",final_report_node) #tbd


graph.add_edge(START,"supervisor")
graph.add_edge("supervisor","financial_research")
graph.add_edge("supervisor","news_research")  
# graph.add_edge("financial_research",END)  

graph.add_edge(
    ["financial_research", "news_research"],
    "final_report"
)

graph.add_edge("final_report",END)

supervisor_graph = graph.compile()

print("Supervisor Graph has been compiled successfully.")

display(Image(supervisor_graph.get_graph().draw_mermaid_png()))

