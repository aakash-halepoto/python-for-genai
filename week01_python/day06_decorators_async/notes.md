# Day 6 — Decorators + async (recognition level)

## Goal today: kill the FEAR, not master these.
Read @decorator and async def without flinching. That's the win.

## Functions are objects you can pass around
def greet(): return "Salam!"
x = greet          # assign the function itself (NO parentheses)
x()                # "Salam!" — x now IS greet

This is the unlock: a function can be handed to another function.

## Decorator = a reusable layer wrapped AROUND a function
It adds behavior before/after the original, WITHOUT editing the original.
Gift analogy: the gift (function) stays as-is; the wrapper adds paper + bow. 🎁

def log_call(func):
    def wrapper(*args, **kwargs):
        print("Calling...")            # extra behavior BEFORE
        result = func(*args, **kwargs) # the ORIGINAL runs here
        print("Done!")                 # extra behavior AFTER
        return result                  # return passes through UNCHANGED
    return wrapper

@log_call
def say_hello():
    return "Hello!"

## The @ is just shorthand — THE key insight
@log_call above say_hello LITERALLY means:
    say_hello = log_call(say_hello)

So say_hello is SECRETLY REPLACED by wrapper. Same name, different function.
The original still exists — trapped inside wrapper as `func`.
Calling say_hello() actually runs wrapper(), which runs the original inside it.



## *args/**kwargs makes a decorator work on ANY function
wrapper(*args, **kwargs)    → COLLECTS any arguments
func(*args, **kwargs)       → SPREADS them into the original
The Day 1 collector+spreader twins, now making decorators universal.
func.__name__ → every function knows its own name (nice for logging).

## Where I'll use decorators (real, near-future)
@timer  → auto-print how long a slow LLM call took
@retry  → auto-retry a failed API call 3 times
@tool   → LangChain wraps my plain function so an AGENT can call it (Week 3!)
I rarely WRITE decorators — I APPLY ones the framework gives me.

---

## async/await = "don't waste the wait"
Normal code WAITS (stares at the pot). Async does other work while waiting.
Cooking analogy: rice boils 15 min → chop veggies meanwhile, don't stare. 🍳

## Where it matters: API calls are slow WAITING
10 LLM calls normally = 10 seconds (one at a time).
Async = fire all, handle as they land = ~time of the slowest. ⚡

## The 3 keywords to RECOGNIZE
async def   → marks a function as "pausable" (a coroutine)
await       → "this line is slow — pause here, let other work run, resume when ready"
asyncio.run(...) → the launcher (async functions can't be called normally)
asyncio.gather(...) → run multiple async things CONCURRENTLY

