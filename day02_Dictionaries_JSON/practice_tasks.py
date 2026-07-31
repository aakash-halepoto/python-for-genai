# Task 1 — The user profile
# You're building the user system for your chatbot:

# profile = {"name": "Ali", "queries_today": 3, "plan": "free"}

# TODO
# Adds a key "language" with value "urdu"
# Updates "queries_today" to 4 (he just asked something)
# Safely reads "email" with a fallback of "not provided" — the safe way, no crash
# Checks if "plan" exists in the profile; if yes, print its value
# Prints the final profile with a loop, each line as key: value

print("Task - 01")
profile = {"name": "Ali", "queries_today": 3, "plan": "free"}
profile["language"] = "urdu"
profile["queries_today"] = 4

email = profile.get("email", "not provided")
print(f"Email: {email}")

if 'plan' in profile:
    print(profile['plan'])

for key , value in profile.items():
    print(f"{key} : {value}")


# Task 2 — Nested dicts (the real shape of API data)

# Real data is dicts inside dicts. Here's a realistic response object, very close to what Claude's API actually returns:

# response = {
#     "id": "msg_001",
#     "model": "claude-sonnet-4-5",
#     "content": {
#         "type": "text",
#         "text": "Neural networks are inspired by the human brain..."
#     },
#     "usage": {
#         "input_tokens": 25,
#         "output_tokens": 150
#     }
# }


# TODO

# Print just the model name
# Print the actual text of the response (peel two layers)
# Print total tokens used (input + output — peel and add)
# Safely check for a key "stop_reason" with fallback "unknown" — it doesn't exist in this response, and your code must not crash
# Add a new key "cost" inside the "usage" dict (not top level!) with value 0.003 — think about which layer you're writing into, then print the final response to verify where it landed
print()
print("Task - 02")

response = {
    "id": "msg_001",
    "model": "claude-sonnet-4-5",
    "content": {
        "type": "text",
        "text": "Neural networks are inspired by the human brain..."
    },
    "usage": {
        "input_tokens": 25,
        "output_tokens": 150
    }
}


print(response["model"])
print(response["content"]["text"])
print(f"total tokens used : {response['usage']['input_tokens'] + response['usage']['output_tokens']}")

stop_reason = response.get('stop_reason' ,'unknown')
print(f"Stop reason : {stop_reason}")
response["usage"]["cost"] = 0.003

print(response)

print()
# Task 3 — Conversation analytics
# messages = [
#     {"role": "user", "content": "How do I renew my CNIC?"},
#     {"role": "assistant", "content": "Visit the NADRA website..."},
#     {"role": "user", "content": "What documents do I need?"},
#     {"role": "assistant", "content": "You need your old CNIC and..."},
# ]
# Using the messages list above, TODO:

# Prints the conversation formatted as user: How do I renew my CNIC? etc.
# Counts how many messages came from the user (loop + condition, or a comprehension with sum()... your choice)
# Builds a list of only the user's questions (just the content strings) — comprehension territory, filtering on one key, keeping another
# Finds the longest message content in the conversation — you know the tool (max + lambda peeking into the dict)
# Appends a new user message: "Where is the nearest NADRA office?" — think about what shape the appended item must be
print("Task - 03")
messages = [
    {"role": "user", "content": "How do I renew my CNIC?"},
    {"role": "assistant", "content": "Visit the NADRA website..."},
    {"role": "user", "content": "What documents do I need?"},
    {"role": "assistant", "content": "You need your old CNIC and..."},
]


user_questions = []
messages.append({"role": "user" , "content":"Where is the nearest NADRA office?"})
user_count = sum(1 for m in messages if m["role"] == "user")
for message in messages:
    if message["role"] == 'user':
        user_questions.append(message['content'])
    print(f"{message['role']}: {message['content']}")
    

print(f"Total messages count came from user : {user_count}")
print(f"longest message content : {max(messages, key=lambda item: len(item['content']))['content']}")
print("---Updated Messages---")
print(messages)
print("---User Asked Question--")
print(user_questions)

print()
# Task 4 — Save and restore a conversation (the real thing)
# Every chatbot with history — including the one you'll build — does exactly this: conversation ends → save messages to JSON; user returns → load and continue.

# Using your messages list (with the NADRA question):

# Save it to a file called conversation.json with indent=2
# Open the file in VS Code and look at it — see your dicts as text, the seed form
# In code: load it back into a new variable restored_messages
# Prove the round trip worked: print the number of messages in restored_messages and the content of its last message
# Append one more message to restored_messages: {"role": "assistant", "content": "The nearest office is on Main Road, Latifabad."} — then save it back to the same file, overwriting
# Bonus check: print(restored_messages == messages) before step 5 — are the restored plant and original plant identical?

print("Task - 04")
import json

with open("day02_Dictionaries_JSON/conversation.json" , "w") as f:
    json.dump(messages,f,indent=2)

with open("day02_Dictionaries_JSON/conversation.json" , "r") as f:
    restored_messages = json.load(f)

print(restored_messages == messages)

restored_messages.append({"role": "assistant", "content": "The nearest office is on Main Road, Latifabad."})

print(f"Number of message in restored messages : {len(restored_messages)}")
print(f"Content of last message : {restored_messages[-1]['content']}")

with open("day02_Dictionaries_JSON/conversation.json" , "w") as f:
    json.dump(restored_messages,f,indent=2)

