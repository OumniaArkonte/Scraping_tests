import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.tools.scrapegraph import ScrapeGraphTools
from agno.models.google import Gemini  

# -------------------------
# Charger le fichier .env
# -------------------------
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Tu dois définir GEMINI_API_KEY dans ton fichier .env")

# -------------------------
# Instancier le modèle Gemini
# -------------------------
gemini_model = Gemini(
    id="gemini-2.0-flash", 
    api_key=GEMINI_API_KEY
)

# -------------------------
# Instancier ScrapeGraphTools
# -------------------------
scrapegraph = ScrapeGraphTools() 

# -------------------------
# Créer l'agent Agno avec Gemini
# -------------------------
agent = Agent(
    model=gemini_model,   
    tools=[scrapegraph],
    markdown=True,        
    stream=True         
)

# -------------------------
# URL à scraper
# -------------------------
url_test = "https://en.wikipedia.org/wiki/Web_scraping"

# -------------------------
# Question pour l'agent
# -------------------------
query = f"""
Use ScrapeGraph to extract the following from {url_test}:
- Main content
- Headings
- Key points
Summarize the main content in 5 points.
"""

# -------------------------
# Exécuter l'agent
# -------------------------
print("=== QUESTION POSÉE À L’AGENT ===")
print(query)
print("\n=== RÉPONSE DE L’AGENT ===\n")

agent.print_response(query)
