# Scenario: The Prompt Processing Engine

# You've just joined a small AI startup as a junior engineer. The team has a chatbot, and every day users submit hundreds of prompts. The data comes in messy, and your team lead assigns you your first real ticket:

# "Build our prompt processing module. We need to clean incoming prompts, batch them for the API, apply per-request settings, log everything, and report daily usage stats. Make it reusable functions — this runs every day."

# The incoming data (today's dump):
print("The Prompt Processing Engine")
raw_prompts = [
    "  Translate this to Urdu  ",
    "",
    "SUMMARIZE my meeting notes",
    "   ",
    "hi",
    "  Write Python code for sorting  ",
    "ok",
    "Explain how neural networks work",
    "  DRAFT an email to my boss ",
]

#  (prompt, tokens_used) from yesterday — for the usage report
usage_log = [
    ("translate this to urdu", 380),
    ("summarize my meeting notes", 1200),
    ("write python code for sorting", 850),
    ("explain how neural networks work", 2100),
    ("draft an email to my boss", 640),
]

# build these 5 functions:

# 1. clean_prompts(prompts, min_length=5) → returns stripped, lowercased prompts, dropping empties and anything ≤ min_length (kills "hi" and "ok" — too short to be real requests)

def clean_prompts(prompts,min_length=5):
    cleaned = [prompt.strip().lower() for prompt in prompts if len(prompt.strip()) >= min_length]
    return cleaned

# 2. make_batches(items, batch_size=3) → returns list of batches (you have this — reuse it, that's the point of functions)

def make_batches(items,batch_size=3):
    batches = []
    for item in range(0,len(items),batch_size):
        batches.append(items[item:item + batch_size])
    return batches


# 3. build_request(prompt, **settings) → starts from base config {"prompt": prompt, "model": "claude", "temperature": 1.0}, overrides with whatever settings arrive, returns the final dict

def build_request(prompt,**settings):
    base = {"prompt" : prompt, "model" : "claude", "temperature" : 1.0}

    for key , value in settings.items():
        base[key] =  value
    return base

# 4. log_requests(*prompts, **info) → prints how many prompts, each one numbered, then each info item as key = value

def log_requests(*prompts, **info):
    prompt_count = len(prompts)
    print(f"Received {prompt_count} prompts")

    for index , prompt in enumerate(prompts,start=1):
        print(f"{index}. {prompt}")

    for key , value in info.items():
        print(f"{key} = {value}")
    

# 5. usage_report(log) → using lambdas, prints: the most expensive prompt, the cheapest, and the log sorted by tokens (highest first). Returns nothing — it's a reporting function (the legitimate exception, remember)

def usage_report(log):
    print(f"The most expensive prompt : {max(log ,key=lambda item: item[1])}")
    print(f"The cheapest prompt : {min(log ,key=lambda item: item[1])}")
    print(f"Log sorted by highest first tokens: {sorted(log ,key=lambda item: item[1], reverse=True)}")


# --- Main Pipeline ---
cleaned = clean_prompts(raw_prompts)
batches = make_batches(cleaned, batch_size=3)
print(f"Prepared {len(batches)} batches")

request = build_request(batches[0][0], temperature=0.3)
print(request)

log_requests(*batches[0], model="claude", status="queued")

usage_report(usage_log)