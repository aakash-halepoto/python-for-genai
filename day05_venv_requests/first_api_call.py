import requests

response = requests.get("https://api.github.com/users/torvalds")

print(response.status_code)
data = response.json()

print(data.get('name'))
print(data.get('public_repos'))
print(data.get('followers'))
