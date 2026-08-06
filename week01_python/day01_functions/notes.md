# Day 1 Functions, args/kwargs, Lambda

## Functions
A function is like a juice machine. Fruits go in (parameters), juice comes out (return).
Build once, use forever.

def clean_prompts(prompts, min_length=0):
    ...
    return cleaned_list

## return vs print
print only shows the juice on the counter.
return actually hands you the glass so you can use it later or pass it to another machine.
Rule: functions return, callers print.

## Default parameters
Factory settings of the machine. min_length=0 means if I say nothing, use 0.
I can override it anytime: clean_prompts(raw, min_length=10)

## Bug I made today (important!)
I wrote return INSIDE the for loop. The function stopped after the first round
and gave back only one batch. return is the emergency exit, the machine shuts down
the moment it runs. Fix: align return with the for, not inside it.

## Lesson about testing
My test data was too small to catch the bug. One batch looked fine even when
the code was broken. Always test with data that can actually prove the code works.

## *args and **kwargs
*args = open wedding hall, any number of guests, stored as a tuple.
**kwargs = guests with name tags, stored as a dictionary.

def log_api_call(*prompts, **options)

This is how LLM libraries accept model="claude", temperature=0.7 etc.

## Lambda
A hand juicer for one time small jobs. Real use is inside sorted/max/min as key.

sorted(responses, key=lambda item: item[1])   # sort by token count
max(responses, key=lambda item: item[1])      # most expensive task

The key answers one question only: which value should Python judge each item by?