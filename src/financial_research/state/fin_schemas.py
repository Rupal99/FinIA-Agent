from typing_extensions import TypedDict


# company_name = "Apple Inc."
# timeline="5 years"

# assess_investment_horizon()
#           │
#           ├── get_price_momentum()
#           │        └── MCP: GetStockPrices
#           │
#           ├── get_price_volatility()
#           │        └── MCP: GetAverageTrueRange
#           │
#           ├── get_forward_guidance()
#           │        └── MCP: GetGuidance
#           │
#           ├── get_earnings_signal()
#           │        └── MCP: GetEarningsBrief
#           │
#           ├── get_business_growth()
#           │        └── MCP: GetFinancialFact
#           │
#           ├── get_valuation_history()
#           │        └── MCP: GetValuationMultiplesHistory
#           │
#           └── get_upcoming_catalysts()
#                    └── MCP: GetInvestorRelationsEvents

class financial_statement(TypedDict):
    fin_stmt: str
    Revenue_breakdown: str
    Timeline: str
    Financial_Fact: str


class ResearchState(TypedDict):
    company_name: str
    financial_statement: financial_statement