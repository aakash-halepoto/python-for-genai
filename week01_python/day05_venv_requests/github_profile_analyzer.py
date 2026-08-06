import requests
import json

# The GitHub Profile Analyzer

# Your team lead's ticket: "We're vetting candidates by their GitHub activity. Build a tool that fetches public profiles from the GitHub API, analyzes them, handles failures gracefully, and saves a report. Make it functions — we'll run it on many usernames."
# This is real: fetching live data, guarding against failures, transforming, and persisting — the full API pipeline. And GitHub's API needs no key, so you can build the whole thing today

# TODO

# fetch_user(username) → sends a GET to https://api.github.com/users/{username}. If status is 200, return the parsed dict. If not, return None (the caller will handle the failure — you know this pattern )

def fetch_user(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        data  = response.json()
        return data
    else:
        return None



# extract_profile(user_data) 
# takes the raw API dict, returns a clean smaller dict with just what you need: name, public_repos, followers, location. Use .get() for each — real API data has missing fields (some users have no location). Missing → "unknown" or 0 as sensible fallbacks.
def extract_profile(user_data):
    user = {}
    user['name'] = user_data.get('name','unknown')
    user['public_repos'] = user_data.get('public_repos',0)
    user['followers'] = user_data.get('followers',0)
    user['location'] = user_data.get('location','unknown')
    return user
    


# analyze_users(usernames) → takes a list of usernames. For each: fetch, and if the fetch succeeded (not None), extract the profile and add it to a results list. If a fetch failed, print "Skipping {username} — not found" and move on. Returns the list of clean profiles. (This is the guard pattern in a loop — fetch, check None, proceed or skip)

def analyze_users(usernames):
    profiles = []
    for username in usernames:
        user_data = fetch_user(username)     
        if user_data is None:
            print(f"Skipping {username} not found")
            continue                        
        profiles.append(extract_profile(user_data))
    return profiles
# save_report(path, profiles) → dumps the profiles list to JSON with indent=2

def save_report(path,profiles):
    with open(path,"w") as f:
        json.dump(profiles,f,indent=2)




usernames = ["torvalds", "aakash-halepoto", "thisuserfake99999", "kennethreitz"]

profiles = analyze_users(usernames)

print(f"Successfully analyzed {len(profiles)} of {len(usernames)} users")
save_report("day05_venv_requests/github_report.json", profiles)
print("Report saved")


