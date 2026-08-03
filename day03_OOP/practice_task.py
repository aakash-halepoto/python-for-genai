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

print()
print("------Extra Tasks-------")

# The counter with a reset

# Build a class TokenCounter:

# __init__ sets self.total = 0
# add(self, amount) — adds to the total
# reset(self) — back to 0
# __str__ — returns "Tokens used: 4500"

# Test: add 1200, add 3300, print the object, reset, print again.

class TokenCounter:
    def __init__(self):
        self.total = 0

    def add(self,amount):
        self.total += amount

    def reset(self):
        self.total = 0

    def __str__(self):
        return f"Tokens used: {self.total}"

token_counter = TokenCounter()

token_counter.add(1200)
token_counter.add(3300)
print(token_counter)
token_counter.reset()
print(token_counter)

print()

# Inheritance with a twist

# You have ChatUser already. Build TrialUser(ChatUser):

# __init__ takes only name, calls the parent ceremony with plan "trial", and sets self.max_queries = 3
# Override ask(self): if self.queries is already at max_queries, return "Trial limit reached — upgrade to pro" without incrementing. Otherwise increment and return the normal f"Query #{self.queries} submitted"

# Test: call ask() five times in a loop, print each result — watch the wall appear after query 3

class TrialUser(ChatUser):
    def __init__(self, name):
        super().__init__(name, plan = 'trial')
        self.max_queries = 3

    def ask(self):
        if self.queries >= self.max_queries:
            return f"Trial limit reached, upgrade to pro"
        self.queries +=1
        return f"Query #{self.queries} submitted"

aakash = TrialUser("aakash")

for i in range(1,6):
    print(aakash.ask())

print()

# The composed class (new idea, small step)

# Classes can contain other classes' objects — no inheritance, just storage. Build Session:

# __init__ takes a ChatUser object and stores it as self.user, plus creates a fresh Conversation() as self.convo
# ask(self, question) — calls self.user.ask(), adds the question via self.convo.add_user(question), and returns the user's ask-result
# summary(self) — returns f"{self.user.name} | messages: {len(self.convo)}" (your __len__ earning its keep!)

class Session:
    def __init__(self,user):
        self.user = user
        self.convo = Conversation()

    def ask(self, question):
        result = self.user.ask()
        self.convo.add_user(question)
        return result

    def summary(self):
        return f"{self.user.name} | messages:{len(self.convo)}"



ali = ChatUser("Ali")
session = Session(ali)

result = session.ask("How do I renew my pssport?")
print(result)
print(session.summary())

print()
print("-----Composed Class Tasks-----")

# One part, one whole

# Build Battery: __init__ sets self.percent = 100; method drain(self, amount) subtracts (but never below 0 — think max(0, ...)); method status(self) returns "Battery: 73%".

# Then build Phone: __init__ manufactures its own Battery (which supply chain is that — receiving or creating?); method use(self, minutes) drains 2% per minute via delegation; method check(self) returns the battery's status — pure relay, one line.

# Test: use the phone 10 minutes, check. Use 45 more, check — should floor at 0, not go negative.

class Battery:
    def __init__(self):
        self.percent = 100

    def drain(self,amount):
        self.percent = max(0,self.percent - amount)

    def status(self):
        return f"Battery: {self.percent}%"


class Phone:
    def __init__(self):
        self.battery = Battery()

    def use(self,minutes):
        usage = minutes * 2
        self.battery.drain(usage)


    def check(self):
        return self.battery.status()


samsung = Phone()

samsung.use(10)
print(samsung.check())
samsung.use(45)
print(samsung.check())

print()

# The whole coordinates two parts

# Build Printer: method print_text(self, text) returns f"PRINTING: {text}".
# Build Scanner: method scan(self) returns "scanned_document.pdf".
# Build Photocopier: __init__ manufactures one of each; method copy(self) — scan first, then print what was scanned, return the print-result. (The scan's return value must travel INTO the printer's method — a value passing between two internal parts, through your coordinating hands. This is the exact ask pattern that leaked on you )

class Printer:

    def print_text(self,text):
        return f"PRINTING: {text}"



class Scanner:
    def scan(self):
        return "scanned_document.pdf"

class Photocopier:
    def __init__(self):
        self.scanner = Scanner()
        self.printer =  Printer()
        pass

    def copy(self):
        scanned = self.scanner.scan()
        return self.printer.print_text(scanned)

photocopier = Photocopier()

print(photocopier.copy())
