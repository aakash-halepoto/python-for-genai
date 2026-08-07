import os
from dotenv import load_dotenv
from groq import Groq
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def ask_llm(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user", "content": prompt}]
    )
    return response.choices[0].message.content

#"The Study Buddy CLI"

# Build a small interactive tool. Team lead's ticket: "Build a study helper that takes a topic, generates an explanation, a real-world example, and a quiz question about it — then saves the study note to a file."

# Build these functions (all wrapping ask_llm):

# get_explanation(topic) → asks for a simple explanation
def get_explanation(topic):
    return ask_llm(f"Explain {topic} in simple words")
# get_example(topic) → asks for one real-world example
def get_example(topic):
    return ask_llm(f"Givee me a one real-word example for {topic}")
# get_quiz_question(topic) → asks for one quiz question (no answer) about the topic
def get_quiz_question(topic):
    return ask_llm(f"Give me one quiz question only an only question not the answer on explanation of {topic}")
# create_study_note(topic) → calls all three, bundles into a dict:
def create_study_note(topic):
    note = {
        "topic": topic,
        "explanation": get_explanation(topic),
        "example": get_example(topic),
        "quiz":get_quiz_question(topic)
    }
    print(note)
    with open(f"week02_llm/day01_get_api_access/{topic}_study_note.json" , "w") as outfile:
        json.dump(note,outfile,indent=2)


#    {
#        "topic": topic,
#        "explanation": ...,
#        "example": ...,
#        "quiz": ...,
#    }

# Prints it nicely AND saves it to {topic}_study_note.json

# Main:

create_study_note("federated learning")

# Why this is the real deal: it's multiple LLM calls composed into one tool, structured into a dict, persisted to disk — the exact shape of a real AI feature. Every skill converges: functions, composition, dicts, JSON, and now live LLM calls 🎯 And it's genuinely useful — you could study from the output.