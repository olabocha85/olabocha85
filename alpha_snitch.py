import requests
from datetime import datetime
import re

KEYWORDS = ["token", "airdrop", "launch", "mint", "IDO", "contract", "pre-sale", "whitelist"]
GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"

def search_github_alpha():
    headers = {"Accept": "application/vnd.github+json"}
    query = " ".join([f"{kw} in:description" for kw in KEYWORDS])
    params = {"q": query, "sort": "updated", "order": "desc", "per_page": 10}
    print(f"[{datetime.now()}] Searching GitHub...")
    response = requests.get(GITHUB_SEARCH_URL, headers=headers, params=params)
    data = response.json()

    for item in data.get("items", []):
        print(f"\n🔍 Project: {item['name']}\n📎 Link: {item['html_url']}\n📄 Desc: {item['description']}\n⭐ Stars: {item['stargazers_count']}")

if __name__ == "__main__":
    search_github_alpha()
