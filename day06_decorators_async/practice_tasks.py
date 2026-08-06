# Build a decorator log_call — think of it as a doorbell camera for your function: the function runs normally, and the decorator "records" (prints) before and after.

# Requirements:

# log_call(func) takes a function
# Inside, define wrapper() that:
# prints "Calling function..." (the camera notices someone approaching)
# runs func() and stores it in result (the door opens — real work happens)
# prints "Done!" (the camera notices they left)
# returns result (the return value passes through unchanged)
# Returns wrapper

# Then apply it with @log_call to a simple function:
def log_call(func):
    def wrapper():
        print("Calling function...")
        result = func()
        print("Done!")
        return result
    return wrapper

@log_call
def say_hello():
    return "Hello, Aakash!"

print(say_hello())

print()

# decorators that work on ANY function (the *args upgrade):

# Your wrapper() takes no arguments — so it only wraps argument-free functions. Try decorating a function that takes arguments and it crashes. Real decorators must handle any function, so the wrapper uses the collector


def log_call(func):
    def wrapper(*args, **kwargs):        
        print(f"Calling {func.__name__}...")   # he function's own name!
        result = func(*args, **kwargs)         # spread them into the real call
        print("Done!")
        return result
    return wrapper


@log_call
def add(a, b):
    return a + b


print(add(5, 3))

print()

import asyncio

async def brew_coffee():
    print("Coffee brewing...")
    await asyncio.sleep(2)
    print("Coffee ready!")
    return "☕"

async def toast_bread():
    print("Toast toasting...")
    await asyncio.sleep(1)
    print("Toast ready!")
    return "🍞"

async def make_breakfast():
    # run BOTH at the same time instead of waiting one-by-one
    results = await asyncio.gather(brew_coffee(), toast_bread())
    print("Breakfast:", results)

asyncio.run(make_breakfast())