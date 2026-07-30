# Task 1:
# Write a function clean_prompts that:

# Takes two inputs: a list of prompts, and min_length with a default value of 0
# Returns (not prints!) a cleaned list: stripped, lowercased, empties removed, and only prompts longer than min_length

# Test it twice:

# raw = ["  Summarize this article ", "", "TRANSLATE to Urdu", "   ", "write a poem"]
# print(clean_prompts(raw))                  # default: keeps everything non-empty
# print(clean_prompts(raw, min_length=10))   # only prompts longer than 10 chars

# Functions calling functions (the pipeline pattern)
# Write a function make_batches that:

# Takes a list and a batch_size (default 3)
# Returns a list of batches — a list of lists, like [['a','b','c'], ['d','e']]

print("Task 1")
def clean_prompts(prompts,min_length=0):
    cleaned_list = [prompt.strip().lower() for prompt in prompts if len(prompt.strip()) >  min_length]
    return cleaned_list

def make_batches(cleaned,batch_size = 3):
    batch = []
    for start in range(0,len(cleaned),batch_size):
        batch.append(cleaned[start:start+batch_size])
    return batch

# raw = ["  Summarize this article ", "", "TRANSLATE to Urdu", "   ", "write a poem"]
raw = ["  Summarize this ", "", "TRANSLATE text", "  write a poem  ", "explain AI", "  ", "fix my code", "draft email"]

cleaned = clean_prompts(raw)
batches = make_batches(cleaned)
print(batches)

# print(clean_prompts(raw))
# print(clean_prompts(raw, min_length=15))




# Task 2: Write a function log_api_call(*prompts, **options) that:

# Prints how many prompts were passed
# Prints each prompt numbered (you have enumerate for this)
# Prints each option as setting = value (hint: loop over options.items() 
# — a preview of tomorrow: for key, value in options.items():)

print()
print("Task 2")

def log_api_call(*prompts, **options):
    prompt_count = len(prompts)
    print(f"Received {prompt_count} prompts")


    for index,prompt in enumerate(prompts,start=1):
        print(f"{index}. {prompt}")

    for key,value in options.items():
        print(f"{key} = {value}")

# Test with:
log_api_call("summarize this", "translate that", model="claude", temperature=0.7)

print()
print("Task 3")


# Task 3 (last of the day): Given:

# responses = [("summarize", 120), ("translate", 45), ("write code", 200), ("chat", 15)]

# Each tuple is (task_name, tokens_used). Using lambda:

# Sort the list by tokens used (ascending) 
# Find the single most expensive task with max
# Print both results
responses = [("summarize", 120), ("translate", 45), ("write code", 200), ("chat", 15)]
print(sorted(responses , key=lambda item: item[1]))
print(max(responses , key=lambda item: item[1]))