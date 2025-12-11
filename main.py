import os
from datetime import datetime
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo

# API Key environment se uthayega (Hardcode mat karna!)
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("API Key nahi mili! Github Secrets check kar.")

today_date = datetime.now().strftime("%Y-%m-%d")

agent = Agent(
    model=Gemini(id="gemini-1.5-pro", api_key=api_key),
    tools=[DuckDuckGo()],
    markdown=True,
)

query = f"""
Today is {today_date}.
1. Search for 'latest unmet needs in B2B SaaS' and 'trending finance news'.
2. Generate 10 Unique Startup Ideas based on these trends.
3. Summarize top 5 Finance News.
Output Format:
## 🚀 Startup Ideas ({today_date})
...
## 💰 Finance News
...
"""

print(f"--- Running Report for {today_date} ---")
agent.print_response(query, stream=False)
