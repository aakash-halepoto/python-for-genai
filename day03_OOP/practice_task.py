import json

# Task 1
# Build the user system for the chatbot, properly this time:
# class ChatUser:
# Requirements:
# __init__ takes name and plan — with plan defaulting to "free"
# Also inside __init__, set self.queries = 0 — every new user starts at zero (note: not a parameter — a field you initialize)
# A method ask(self) that adds 1 to the user's queries and returns f"Query #{self.queries} submitted"
# A method info(self) that returns one line: "Ali | plan: free | queries: 3"

class ChatUser:
    def __init__(self, name, plan = 'free'):
        self.name = name
        self.plan = plan
        self.queries = 0

    def ask(self):
        self.queries +=1
        return f"Query #{self.queries} submitted"

    def info(self):
        return f"{self.name} | plan: {self.plan} | queries : {self.queries}"


user1 = ChatUser("Ali")
user2 = ChatUser("Ahmed", plan="pro")

print(user1.ask())      # Query #1 submitted
print(user1.ask())      # Query #2 submitted
print(user2.ask())      # Query #1 submitted  Ahmed's counter, separate form!
print(user1.info())     # Ali | plan: free | queries: 2
print(user2.info())     # Ahmed | plan: pro | queries: 1

print()

# Task 2: The Conversation

# This is the class I promised on planning day: a proper home for the message format you mastered yesterday. This is genuinely what LangChain's memory objects are underneath — a list of dicts wearing a class around it.

# class Conversation:

# Requirements:
# __init__ takes nothing (besides self) — initializes self.messages as an empty list
# add_user(self, content) — appends {"role": "user", "content": content} to the messages
# add_assistant(self, content) — same, role "assistant"
# history(self) — returns (never prints) the formatted conversation as one string, each message on its own line like user: How do I renew my CNIC? — hint: build a list of formatted lines, then "\n".join(lines) glues them with newlines (new tool! try it)
# count_user_messages(self) — returns how many user messages — you own this pattern from yesterday's sum(1 for ...)
# save(self, path) — dumps self.messages to JSON at that path (yesterday's skill, now living as a method)
# load(self, path) — loads JSON from path into self.messages, replacing whatever was there

print("-------Task 02----------")

class Conversation:
    def __init__(self):
        self.messages = []

    def __str__(self):
        return f"Conversation with {len(self.messages)} messages"

    def __len__(self):
        return len(self.messages)

    def add_user(self,content):
        self.messages.append({"role": "user", "content": content})

    def add_assistant(self,content):
            self.messages.append({"role": "assistant", "content": content})

    def history(self):
        lines = []
        for message in self.messages:
              lines.append(f"{message['role']}: {message['content']}")
        return "\n".join(lines)

    def count_user_messages(self):
         return sum(1 for message in self.messages if message['role'] == 'user')

    def save(self,path):
        with open(path,"w") as file:
              json.dump(self.messages,file,indent=2)

    def load(self,path):
        with open(path,"r") as file:
             self.messages = json.load(file)


convo = Conversation()
print(convo)
print(len(convo))
convo.add_user("How do I renew my CNIC?")
convo.add_assistant("Visit the NADRA website...")
convo.add_user("What documents do I need?")

print(convo.history())
print(f"User messages: {convo.count_user_messages()}")
convo.save("day03_OOP/conversation.json")

convo2 = Conversation()                          # fresh, empty object
convo2.load("day03_OOP/conversation.json")       # resurrect the saved chat
print(convo2.history())                          # identical history — persistence + OOP 

print()
# Task 3

# Add __str__ and __len__ to your Conversation class — then test: print(convo) and print(len(convo))
# Build PremiumUser(ChatUser) exactly as sketched — but type it, don't paste
# Test: create one regular ChatUser and one PremiumUser; call ask() on both, info() on both. Observe: different ask outputs (override working), same info format (inheritance working)

print("-----Task 03------")

class PremiumUser(ChatUser):                      # ← inherits everything ChatUser has
    def __init__(self, name):
        super().__init__(name, plan="pro")        # run the parent's ceremony first
        self.priority_support = True              # then add the new field

    def ask(self):                                # OVERRIDE: replace parent's version
        self.queries += 1
        return f"[PRIORITY] Query #{self.queries} submitted"


premUser = PremiumUser("Zara")

print(user1.ask())
print(user1.info())

print(premUser.ask())
print(premUser.info())

