# Day 2 — Dictionaries + JSON

## Dictionaries
A dict is like a contacts app. You don't scroll to position 5,
you search by name (key) and instantly get the number (value).
Lists find by position, dicts find by name.

user = {"name": "Aakash", "city": "Hyderabad"}

## CRUD operations
user["email"] = "a@gmail.com"   # Create
user["name"]                     # Read
user["city"] = "Karachi"         # Update (same syntax as create)
del user["email"]                # Delete

Key exists? overwrite. Doesn't exist? added. Same one line does both.

## .get() vs [] — the crash preventer
user["salary"]           # CRASHES if key missing (KeyError)
user.get("salary")       # returns None, no crash
user.get("salary", 0)    # returns 0 as my chosen fallback

[] is barging into a room shouting. .get() knocks politely and
walks away if nobody answers.

Rule: my own dicts → [] is fine. Data from OUTSIDE (APIs, files,
user input) → always .get(), because I can't trust what arrived.

## Fallback lesson (bug I made)
.get('email') alone still gives None. The fallback goes INSIDE:
.get('email', 'not provided'). Otherwise None leaks into output
like "We'll contact you at None".

## Nested dicts
Dicts inside dicts. Peel layer by layer like batches[0][0] but with keys:
response["usage"]["input_tokens"]
When writing, know WHICH layer: response["usage"]["cost"] = 0.003

## List of dicts — THE most important shape
messages = [
    {"role": "user", "content": "How do I renew my CNIC?"},
    {"role": "assistant", "content": "Visit the NADRA website..."},
]
This is literally the LLM conversation format. Train of contact cards.
messages[0]["content"] → first card, then read it.

## Chaining lookups
max(messages, key=lambda m: len(m['content']))['content']
max returns the whole winning dict → ['content'] opens it right away.
Functions return containers, brackets chain onto results.


## JSON
JSON = dictionaries written down as text. My dict is a living plant,
JSON is its seed — dried, packable, shippable, plantable back.
Dicts live in RAM and die with the program. JSON survives in files.

import json
with open("conversation.json", "w") as f:   # w = write (WIPES file first!)
    json.dump(messages, f, indent=2)         # dump = pour dict into file

with open("conversation.json", "r") as f:   # r = read
    restored = json.load(f)                  # load = scoop it back out

indent=2 → pretty spacing for humans, machines don't need it
f → just a variable holding the opened file (the borrowed book)
Round trip is LOSSLESS: restored == original → True

Also exists: dumps/loads (with s) = same but to/from a STRING not a file.
APIs use the string versions.