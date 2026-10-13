

from supervisor.state.input_schema import InputState

def final_report_node(state: InputState):
    print("Executing final report node for company:", state["company_name"])
    # Extract relevant information from the state
    company_name = state["company_name"]
    financial_data = state["financial_statement"]
    news_data = state["latest_news"]  

    # Generate a final report based on the collected data
    report = f"Final Report for {company_name}:\n\n"
    print("-----\nGenerating Final Report for:", company_name)
    report += "\n\n\nFinancial Research:\n\n\n"
    report += f"{financial_data}\n\n"
    report += "\n\n\nNews Research:\n\n\n\n"
    report += f"{news_data}\n"

    print("Final Report Node has generated the report successfully.")
    print("-----\nFinal Report:\n", report)
    return {
        "final_report": report
    }