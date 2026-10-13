# import asyncio
# import sys
# from pathlib import Path

# SRC_PATH = Path(__file__).resolve().parents[2]
# if str(SRC_PATH) not in sys.path:
#     sys.path.insert(0, str(SRC_PATH))

# from finacial_research.graphs.research_graph import research
# from finacial_research.graphs.news_research_graph import news_research

# company_name = input("Enter the company name (e.g., AAPL, MSFT, NVDA): ")


# async def main():
#     result_fin = await research.ainvoke(
#         {
#             "company_name": company_name,
#         }
#     )
#     result_news = await news_research.ainvoke(
#             {
#                 "company_name": company_name,
#             }
#         )

#     print(result_fin)
#     print("--------------------------------------------------\n\n\n\n\n")
#     print(result_news)


# if __name__ == "__main__":
#     asyncio.run(main())