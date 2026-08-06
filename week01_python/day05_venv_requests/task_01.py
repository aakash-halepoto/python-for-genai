import requests

# Task - status codes and error handling (the real-world part):

# APIs don't always return 200. The address might be wrong, the server might be down, rate limits hit. Production code never assumes success. Write code that:

# Requests https://api.github.com/users/torvalds (valid) — check if status_code == 200, then print the name

# Requests https://api.github.com/users/thisuserdefinitelydoesnotexist99999 (invalid) — this returns 404. Your code must handle it gracefully: if not 200, print "Request failed with status: 404" instead of crashing

# Wrap the check in an if/else on the status code. This "check before you trust" pattern is exactly what separates production API code from tutorial code — and it's the same defensive mindset as .get() for dicts


response = requests.get("https://api.github.com/users/torvalds")
if response.status_code == 200:
    data = response.json()
    print(data.get("name"))
else:
    print(f"request failed with status: {response.status_code}")


response2 = requests.get("https://api.github.com/users/thisuserdefinitelydoesnotexist99999")
if response2.status_code == 200:
    data = response2.json()
    print(data.get('name'))
else:
    print(f"request failed with status: {response2.status_code}")



print()

