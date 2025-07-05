from openai import OpenAI
import os
from duckduckgo_search import DDGS

def call_llm(prompt: str) -> str:
    """Call OpenAI chat completion API."""
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "your-api-key"))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def search_duckduckgo(query: str) -> str:
    """Search the web using DuckDuckGo and return formatted results."""
    results = DDGS().text(query, max_results=5)
    return "\n\n".join(
        f"Title: {r['title']}\nURL: {r['href']}\nSnippet: {r['body']}" for r in results
    )
