from langchain_protocol import TypedDict

from financial_research.state.fin_schemas import ResearchState
from financial_research.tools.equibles import client

async def fin_stmt_node(state: ResearchState):
    print("Executing financial statement node for company:", state["company_name"])
    tools = await client.get_tools()

    fin_stmt_tool = next(
        tool
        for tool in tools
        if tool.name == "GetFinancialStatement"
    )

    RevenueBreakdown_tool = next(
            tool
            for tool in tools
            if tool.name == "GetRevenueBreakdown"
    )

    FinancialFact_tool= next(
            tool
            for tool in tools
            if tool.name == "GetFinancialFact"         
            
            )

    timeline_tool= next(
            tool
            for tool in tools
            if tool.name == "GetValuationMultiplesHistory"         
            
            )


    result_fin_s = await fin_stmt_tool.ainvoke(
        {
            "ticker": state["company_name"],
            "statement": "income",
        }
    )
    # print("Financial Statement Result:", result_fin_s)
    result_revenue = await RevenueBreakdown_tool.ainvoke(
        {
                "ticker": state["company_name"],
                "statement": "income",
        }
    )
    # print("Revenue Breakdown Result:", result_revenue)

    result_timeline = await timeline_tool.ainvoke(
        {
                "ticker": state["company_name"]
        }
    )
    # print("Timeline Result:", result_timeline)

    result_fin_fact = await FinancialFact_tool.ainvoke(
        {
                "ticker": state["company_name"],
                "concept": "revenue",
        }
    )
    # print("Financial Fact Result:", result_fin_fact)
    #print("Financial node state:", state["company_name"])


    return {
        "financial_statement": {
            "fin_stmt": result_fin_s,
            "Revenue_breakdown": result_revenue,
            "Timeline": result_timeline,
            "Financial_Fact": result_fin_fact
        }
    }

