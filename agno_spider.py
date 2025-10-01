import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.spider import SpiderTools

load_dotenv()

print(" GEMINI_API_KEY:", os.getenv("GEMINI_API_KEY") is not None)
print(" SPIDER_API_KEY:", os.getenv("SPIDER_API_KEY") is not None)

agent = Agent(
    model=Gemini(id="gemini-2.0-flash", api_key=os.getenv("GEMINI_API_KEY")),
    tools=[SpiderTools()]
)

# 1️ Scrape direct d’un site
print("=== Test Scrape avec Gemini + Spider ===")
agent.print_response(
    "Scrape https://www.cnn.com and summarize the main headlines in French",
    markdown=True
)

# 2️ Recherche + scrape + résumé
print("\n=== Test Search + Scrape avec Gemini ===")
agent.print_response(
    'Search for "latest AI news" and scrape the first result, then summarize in 5 bullet points',
    markdown=True
)
