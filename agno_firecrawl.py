import os
from agno.agent import Agent
from agno.tools import tool
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
from agno.models.mistral import MistralChat

# ==========================
# CHARGER LA CONFIG .ENV
# ==========================
load_dotenv()
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

if not FIRECRAWL_API_KEY:
    raise ValueError(" Tu dois définir FIRECRAWL_API_KEY dans ton fichier .env")
if not MISTRAL_API_KEY:
    raise ValueError(" Tu dois définir MISTRAL_API_KEY dans ton fichier .env")

firecrawl_app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

# ==========================
# OUTIL FIRECRAWL POUR AGNO
# ==========================
@tool
def scrape_with_firecrawl(url: str) -> str:
    print(f" Firecrawl est appelé pour : {url}")  
    result = firecrawl_app.scrape(url)
    if "markdown" in result:
        return result["markdown"]
    elif "content" in result:
        return result["content"]
    else:
        return str(result)


# ==========================
# AGENT AGNO
# ==========================
agent = Agent(
    model=MistralChat(id="mistral-large-latest"),
    tools=[scrape_with_firecrawl],
    instructions="Tu es un agent qui aide à scraper et analyser des sites web avec Firecrawl."
)

# ==========================
# TEST
# ==========================
if __name__ == "__main__":
    url_test = "https://en.wikipedia.org/wiki/Web_scraping"
    query = f"Scrape le contenu principal de {url_test} et donne-moi un résumé en 5 points."
    
    print("=== QUESTION POSÉE À L’AGENT ===")
    print(query)
    print("\n=== RÉPONSE DE L’AGENT ===\n")
    
    response = agent.run(query)
    print(response.content)   

