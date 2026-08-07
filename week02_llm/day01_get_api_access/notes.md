# Week 2, Day 1 — First Real LLM Call (Groq)

## The milestone
My Python code talked to a real language model for the first time.
Sent a prompt → model GENERATED a response → came back to my terminal.
Not stored anywhere — created on demand by the AI.

## Getting set up
1. Signed up at console.groq.com (free, no credit card)
2. Created API key (starts with gsk_) — shown ONCE, copy immediately
3. pip install groq python-dotenv
4. Key goes in .env file, NEVER in code, NEVER committed to git

## API key safety (critical)
- Key lives in .env: GROQ_API_KEY=gsk_...
- .gitignore MUST contain .env (separate from .venv/)
- Verify BEFORE committing: `git status` → .env must NOT appear
- Check history: `git log --all --full-history -- ".env"` → empty = safe
- Bots scrape GitHub for gsk_/sk- keys within minutes. A leaked key = revoke + regenerate.

## The LLM call structure
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()                                     # reads .env
client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # pulls key safely

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "..."}],
)
print(response.choices[0].message.content)

## Everything here is RECOGNITION from Week 1
- messages=[{"role": "user", "content": ...}]  → list-of-dicts (Day 2 + Conversation class)
- response.choices[0].message.content          → nested peeling (batches[0][0])
- load_dotenv() + os.getenv()                  → .env handling (Day 5 seed, now real)
- the whole call                               → an API call (Day 5) with a messages payload
- the model/messages payload                   → same shape as build_request (Day 1)

An LLM call is just an API call with a messages payload. Nothing new conceptually.

## The response object holds more than text
response.choices[0].message.content   → the actual answer
response.model                        → which model ran
response.usage.total_tokens           → TOKENS USED (this is what costs money in paid APIs)
response.choices[0].finish_reason     → why it stopped

Reading token usage = real engineering literacy (cost awareness).

## ask_llm() — my first AI toolkit brick 
def ask_llm(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

Setup (load_dotenv, client) happens ONCE at top — function stays focused.
Function returns, caller prints (Week 1 rule holds).
Every AI tool this week builds on top of this function.

## Note for later (don't do yet)
Model name is hardcoded now — fine for today. Later I'll parameterize:
ask_llm(prompt, model=..., temperature=...) — but add flexibility WHEN a need appears, not before.

## Groq notes
- Free tier: ~30 req/min, 14,400 req/day — plenty for learning
- OpenAI-SDK compatible → patterns transfer to industry standard
- Runs open models only (Llama, Qwen, etc.) — no GPT/Claude/Gemini (it's a complement, not a replacement)