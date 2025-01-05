from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os 
os.environ["GROQ_API_KEY"]="gsk_T1nleOBtK7Bj3zsgjLhdWGF80gDdcXFPMFcppV9OR9n"


web_search_agent=Agent(
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    instructions=["always include sources"],
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
    )

web_search_agent.print_response("Latest news of IBM company shares?",)
