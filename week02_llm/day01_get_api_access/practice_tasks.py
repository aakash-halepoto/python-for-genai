import os
from dotenv import load_dotenv
from groq import Groq
import json


load_dotenv()                                    
client = Groq(api_key=os.getenv("GROQ_API_KEY")) 

def ask_llm(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


# print(ask_llm("What is Python in one sentence?"))
# print(ask_llm("Name 3 uses of AI in healthcare."))
# print(ask_llm("Translate 'good morning' to Urdu."))


# Task 1 — A themed helper function

# Build explain_simply(topic) that uses ask_llm internally but wraps the topic in a fuller prompt: "Explain {topic} in simple terms that a 10-year-old could understand, in 2-3 sentences."

# (This is composition — a function calling your function, adding value on top.

def explain_simply(topic):
    return ask_llm(f"Explain {topic} in simple terms that a 10-year-old could understand, in 2-3 sentences")

# Test with: explain_simply("machine learning"), explain_simply("APIs"), explain_simply("neural networks").

print(explain_simply('machine learning'))
print(explain_simply('APIs'))
print(explain_simply('neural networds'))



print()
print("Task 02")
# Task 2 — Multiple prompts in a loop

# You have a list of questions. Loop through them, get an answer for each, and print them numbered:


questions = [
    "What is Python?",
    "What is an API?",
    "What is JSON?",
]

# Print like: Q1: What is Python? then the answer below it.
for index,question in enumerate(questions,start=1):
    print(f"Q{index}: {question}")
    print(ask_llm(question))
    print()

# Task 3 — Token tracker

# Modify a version of ask_llm (call it ask_llm_verbose) that returns BOTH the answer AND the token count as a tuple. Then call it and print both separately.

def ask_llm_verbose(prompt):
    response = client.chat.completions.create(
        model= "llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content,response.usage.total_tokens

answer,token = ask_llm_verbose("How LLM works?")
print(f"Answer: {answer}")
print(f"Token used: {token}")

# (Why: in real work you track token usage to monitor cost. This is the foundation of that.)

# Task 4 — A tiny translator tool

# Build translate(text, language) that prompts: "Translate the following text to {language}. Only return the translation, nothing else: {text}"

def translate(text,language):
    return ask_llm(f"Translate the following text to {language}. Only return the translation, nothing else{text}")

# Test: translate("Hello, how are you?", "Urdu"), translate("Good morning", "French"), translate("Thank you", "Arabic").
print(translate("Hello, how are you?", "Urdu"))
print(translate("Good morning", "French"))
print(translate("Thank you", "Arabic"))

# (Note the "Only return the translation, nothing else" — that's your first taste of prompt control, tomorrow's whole topic. Watch whether the model obeys)

# Task 5 — Save AI responses to a file

responses = []
for question in questions:
    answer = ask_llm(question)
    responses.append({"question": question, "answer": answer})

with open("week02_llm/day01_get_api_access/ai_responses.json", "w") as outfile:     
    json.dump(responses, outfile, indent=2)


with open("week02_llm/day01_get_api_access/ai_responses.json","r") as infile:
    restored_ai_responses = json.load(infile)

print(restored_ai_responses)

# Combine Week 1 + Week 2: ask the LLM 3 questions, collect each as a dict {"question": ..., "answer": ...}, and save the list to ai_responses.json (your Day 2 JSON skills). Then load it back and print to verify the round trip.

# (This is real: logging AI interactions to disk is exactly how you'd build conversation history or audit logs )