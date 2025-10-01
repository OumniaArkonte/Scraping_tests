import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.mistral import MistralChat
from agno.tools.browserbase import BrowserbaseTools

# Charger les variables d'environnement
load_dotenv()

# Vérifier les clés Browserbase
BROWSERBASE_API_KEY = os.getenv("BROWSERBASE_API_KEY")
BROWSERBASE_PROJECT_ID = os.getenv("BROWSERBASE_PROJECT_ID")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

if not BROWSERBASE_API_KEY or not BROWSERBASE_PROJECT_ID:
    raise ValueError("Tu dois définir BROWSERBASE_API_KEY et BROWSERBASE_PROJECT_ID dans ton fichier .env")
if not MISTRAL_API_KEY:
    raise ValueError("Tu dois définir MISTRAL_API_KEY dans ton fichier .env")

print(" BROWSERBASE_API_KEY:", bool(BROWSERBASE_API_KEY))
print(" BROWSERBASE_PROJECT_ID:", bool(BROWSERBASE_PROJECT_ID))
print(" MISTRAL_API_KEY:", bool(MISTRAL_API_KEY))

# Créer l'agent avec Browserbase et Mistral
agent = Agent(
    model=MistralChat(id="mistral-medium-latest", api_key=MISTRAL_API_KEY),
    name="Browserbase Web Scraper",
    tools=[BrowserbaseTools()],
    instructions=[
        "Extract content clearly and format nicely.",
        "Always close sessions when done."
    ],
    markdown=True
)


task = """
Go to https://quotes.toscrape.com and:
1. Get the first 3 quotes with their authors.
2. Navigate to page 2.
3. Get 2 more quotes from page 2.
4. Summarize the style and tone of these quotes.
"""

print("\n=== Lancement du test Browserbase + Mistral ===\n")
response = agent.run(task)


print("\n=== Résultat du scraping ===\n")
print(response.content)
