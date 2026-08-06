# Day 3 — Classes and OOP

## Class vs Object
A class is the blank CNIC form template at NADRA — it defines what
fields exist and what actions are possible.
An object is one person's FILLED form. Same template, thousands of
copies, each with its own data.

class ChatUser:          # the template
user1 = ChatUser("Ali")  # a filled form

## __init__ — the form-filling ceremony
Runs automatically the moment an object is created. Its job: take
incoming data and write it onto the form.

def __init__(self, name, plan='free'):   # defaults work here too (Day 1!)
    self.name = name        # field on the form (permanent)
    self.queries = 0        # field I initialize myself, not from caller

self.name vs name → the form field vs the incoming parameter that
evaporates when __init__ ends. 80% of OOP confusion lives here.

## self — the form currently in my hands
When NADRA processes 500 forms, "write the name HERE" must know WHICH
form. self is that word: THIS particular one.
user1.ask() secretly means ChatUser.ask(user1) — the dot delivers the form.
That's why methods list self but calls don't pass it.

## Each object keeps its own state (the whole point of OOP)
Ali asked twice → his counter says 2. Ahmed asked once → his says 1.
Same class, separate forms, independent data. Proven in my own output.

## Methods = functions living inside a class
All Day 1 rules apply: parameters, defaults, return.
Methods do their job SILENTLY — the caller decides what to print.


## Inheritance — the driving license form
The license form doesn't start from scratch — it reuses all CNIC
fields and adds new ones.

class PremiumUser(ChatUser):        # parentheses = my parent is ChatUser
    def __init__(self, name):
        super().__init__(name, plan="pro")   # run parent's ceremony FIRST
        self.priority_support = True          # then add new fields

Skip super().__init__ and self.name never gets set → crash.

## Overriding
Define ask() again in the child → child's version shadows the parent's.
Zara's ask shows [PRIORITY]; Ali's doesn't. Same method name, different
behavior per class.

## Method lookup climbs the FAMILY LADDER, not the file
premUser.info() → Python checks PremiumUser (not there) → climbs to
ChatUser (found, runs it). The method lives in the parent; the data
comes from self — borrowed machinery, own fuel.


## Dunder methods — teaching objects manners
print(convo) → ugly memory address. len(convo) → TypeError.
Fix by hooking into Python's built-ins:

def __str__(self):   # what print() shows
    return f"Conversation with {len(self.messages)} messages"
def __len__(self):   # what len() returns
    return len(self.messages)

That's why len([1,2]) works — list has __len__ inside. The magic was
always just methods.

## Why this matters for GenAI
client = Anthropic(), model.invoke(), agent.run() — every framework
object is a class instance. I'll WRITE few classes but READ them daily.
My Conversation class IS the miniature of LangChain's chat memory.