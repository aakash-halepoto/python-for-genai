# "The Usage Dashboard"
# Your team lead's ticket: "Users file is a JSON dump. Build a small analytics module: load it, compute stats safely (data is messy — fields are missing), and save a summary report as JSON."

import json
users_data = [
    {"name": "Ali", "plan": "pro", "queries": 120, "city": "Hyderabad"},
    {"name": "Sara", "queries": 45},
    {"name": "Bilal", "plan": "free", "city": "Karachi"},
    {"name": "Zara", "plan": "pro", "queries": 300, "city": "Hyderabad"},
    {"name": "Omar", "plan": "free", "queries": 15},
]
with open("day02_Dictionaries_JSON/users.json", "w") as f:
    json.dump(users_data, f, indent=2)

# TODO

# load_users(path) → returns the list from the JSON file
def load_users(path):
    with open(path,"r") as f:
        restored_users  = json.load(f)
    return restored_users    
# total_queries(users) → sum of all queries, missing counts as 0
def total_queries(users):
    return sum(user.get('queries', 0) for user in users)

# count_plans(users) → dict like {"pro": 2, "free": 2} — Task 3's pattern, missing plan counts as "free"
def count_plans(users):
    counts = {}
    for user in users:
        plan = user.get('plan','free')
        counts[plan] =  counts.get(plan,0) + 1
    return counts


# top_user(users) → name of the user with the most queries (lambda + safe get inside it)
def top_user(users):
    return max(users, key= lambda user:user.get('queries',0))["name"]

# city_report(users) → dict counting users per city, missing city counts as "unknown"

def city_report(users):
    user_per_city = {}
    for user in users:
        city = user.get('city','unknown')
        user_per_city[city] = user_per_city.get(city,0) + 1
    return user_per_city

# save_summary(path, **stats) → collects everything passed and dumps it as JSON (yesterday's **kwargs meets today's json.dump)
def save_summary(path,**stats):
    with open(path,"w") as file:
        json.dump(stats,file,indent=2)

# Main pipeline:
users = load_users("day02_Dictionaries_JSON/users.json")
summary_stats = {
    "total_queries": total_queries(users),
    "plans": count_plans(users),
    "top_user": top_user(users),
    "cities": city_report(users),
}

save_summary("day02_Dictionaries_JSON/summary.json", **summary_stats)
print("Report saved")

# Expected summary.json:

# json
# {
#   "total_queries": 480,
#   "plans": {"pro": 2, "free": 3},
#   "top_user": "Zara",
#   "cities": {"Hyderabad": 2, "unknown": 2, "Karachi": 1}
# }