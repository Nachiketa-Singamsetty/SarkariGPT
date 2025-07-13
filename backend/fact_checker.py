"""
Retrieval-Augmented Fact Checker for SarkariGPT
- Uses SerpAPI (Google Search API, free tier) for retrieval
- Uses HuggingFace Transformers LLM (Gemma-2B-IT) for verdict
- Returns: verdict (✅ True / ❌ False / 🤷 Unverified), rationale, and links

Note: Serper.dev and SerpAPI are different services. This code uses SerpAPI because you have a SERPAPI_KEY.
"""
import os
import requests
from transformers.pipelines import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")
SERPAPI_URL = "https://serpapi.com/search"

# 1. Web Search via SerpAPI
def web_search(query, num_results=5):
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google",
        "num": num_results,
        "hl": "en",
        "gl": "in"
    }
    resp = requests.get(SERPAPI_URL, params=params, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    results = data.get("organic_results", [])
    return [{"title": r.get("title", ""), "link": r.get("link", ""), "snippet": r.get("snippet", "") or r.get("snippet_highlighted_words", [""])[0]} for r in results[:num_results]]

# 2. Load LLM (Gemma-2B-IT, open-access)
def load_llm():
    model_id = "google/gemma-2b-it"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    return pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512)

llm = None

def fact_check_claim(claim):
    global llm
    if llm is None:
        llm = load_llm()
    # Step 1: Search the web
    articles = web_search(claim, num_results=5)
    evidence = "\n".join([f"- {a['title']}: {a['snippet']} ({a['link']})" for a in articles])
    # Step 2: Compose LLM prompt
    prompt = (
        f"Claim: {claim}\n"
        f"Recent news articles:\n{evidence}\n\n"
        "Based on the above, is the claim TRUE, FALSE, or UNVERIFIED? "
        "Reply with one of: ✅ True, ❌ False, 🤷 Unverified. "
        "Give a 1-2 sentence rationale and cite the most relevant links."
    )
    # Step 3: Get LLM verdict
    response = llm(prompt)[0]["generated_text"].replace(prompt, "").strip()
    return {
        "claim": claim,
        "verdict": response,
        "evidence": articles
    }

if __name__ == "__main__":
    claim = "PM Modi inaugurated Chenab Bridge, world's highest rail arch bridge in Jammu and Kashmir"
    result = fact_check_claim(claim)
    print(result)
