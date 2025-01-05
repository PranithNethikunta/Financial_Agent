from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os 
os.environ["GROQ_API_KEY"]="gsk_T1nleOBtK7Bj3zsgjLhdWGdyb3FYrqF80gDdcXFPMFcppV9OR9n"


web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["always include sources"],
    show_tool_calls=True,
    markdown=True,
    )

financial_agent=Agent(
    name="Financial Agent",
    role="Get financial data",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,key_financial_ratios=True,company_news=True)],
    instructions=["Give the results in table format"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent=Agent(
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    team=[web_search_agent,financial_agent],
    instructions=["always include sources","Give the results in table format"],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("share the latest news and stock price for Tesla", stream=True)