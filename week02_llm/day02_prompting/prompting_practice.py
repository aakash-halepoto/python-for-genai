from llm_client import ask_llm


print(ask_llm("Tell me about AI") )
print(ask_llm("Explain AI in exactly 2 sentences for a 10-year-old"))

print("-------------------------------------------------")

print(ask_llm("List 3 programming languages"))
print()
print(ask_llm("List exactly 3 programming languages. Respond with ONLY a comma-separated list, no other text."))