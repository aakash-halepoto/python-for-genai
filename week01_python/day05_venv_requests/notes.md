# Day 5 — venv, pip, requirements.txt + requests

## Virtual environment = a separate kitchen per project
Each project needs different package versions. Global install = they
collide (dependency hell). A venv isolates each project's packages.

python3 -m venv .venv          # create the kitchen (Linux: python3, not python)
source .venv/bin/activate      # activate → prompt shows (.venv)
pip install requests           # installs INTO this venv only
pip freeze > requirements.txt  # save exact versions (the recipe)

Linux note: Ubuntu needs `sudo apt install python3.x-venv` first.

## requirements.txt = the recipe, .venv = the kitchen
Commit requirements.txt (small, shareable). NEVER commit .venv (huge,
machine-specific). Anyone can rebuild the kitchen from the recipe:
pip install -r requirements.txt

One package (requests) pulled in 5 — its dependencies (urllib3, certifi...).
==2.34.2 pins the EXACT version → reproducible.

## .gitignore
A note on the project's front door telling git which folders to skip.
Lives in the REPO ROOT, contains: .venv/
(venv auto-creates its OWN .gitignore inside .venv — different file, leave it.)

## requests = talking to the internet (sending a letter)
requests.get(url) = mail a letter, get a reply.
response = the reply. status_code = the postal stamp.
200 = delivered ✅   404 = address not found   500 = server broke

import requests
response = requests.get("https://api.github.com/users/torvalds")
print(response.status_code)     # 200
data = response.json()          # JSON reply → Python DICT!

.json() turns the reply into a dict → every Day 2 skill works on live data.

## Verify before you trust (production vs tutorial)
NEVER assume success. Guard on the status:

if response.status_code == 200:
    data = response.json()
    ...
else:
    print(f"Request failed with status: {response.status_code}")

Same "verify before use" instinct as .get() for dicts and is None for
objects. Now in 4 contexts: .get(), is None, status codes, None-in-a-loop.

## POST = sending data (THE LLM shape)
GET fetches. POST sends data and gets a reply — this is how you call an LLM.

payload = {"model": "claude", "prompt": "...", "temperature": 0.7}
response = requests.post(url, json=payload)   # json= converts dict → JSON, ships it

That payload dict IS my build_request from Day 1. An LLM call = this exact
pattern: build payload → POST as JSON → parse reply → extract the field.
Real Claude reply is nested like response["content"][0]["text"] — same
peeling as batches[0][0]. All the nested-access training pays off here.



## The full API pipeline (GitHub analyzer)
fetch (guard on status) → check None → extract clean subset → persist JSON.
This is the shape of EVERY real data-fetching job. Swap the URL for an LLM's
endpoint + add a key → same skeleton calls a model.

## continue keyword
Inside a loop: "stop THIS iteration, jump to the next."
Used for skip-on-failure: if fetch failed → print skip → continue (append never runs).