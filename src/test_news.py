import asyncio
import sys
from pathlib import Path

SRC_PATH = Path(__file__).resolve().parents[2]
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from news.graphs.news_research_graph import news_research
from financial_research.graphs.research_graph import research
from supervisor.graphs.supervisor_graph import supervisor_graph

user_message = input("Enter what u want to research: ")


async def main():
    # result_news = await news_research.ainvoke(
    #         {
    #             "company_name": company_name,
    #         }
    #     )
    # fin_research_result = await research.ainvoke(
    #         {
    #             "company_name": company_name,
    #         }
    #     )
    supervisor_result = await supervisor_graph.ainvoke(
            {
                "user_message": user_message,
            }
        )

    print("supervisor_result:", supervisor_result)
    # print(result_news)
    # print("--------------------------------------------------\n\n\n\n")
    # print(fin_research_result)


if __name__ == "__main__":
    asyncio.run(main())


    # I want to know about APPLE, i want a financial report on it