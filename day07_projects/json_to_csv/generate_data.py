import json
import random

cities = ["Hyderabad", "Karachi", "Lahore", "Islamabad", "Multan",
          "Peshawar", "Quetta", "Sukkur", "Faisalabad", "Rawalpindi"]
plans = ["free", "pro", "trial"]
names = ["Ali", "Zara", "Bilal", "Sara", "Omar", "Kainat", "Ahmed", "Hina",
         "Usman", "Ayesha", "Kashif", "Nimra", "Salman", "Muhammad", "Tariq"]

data = [
    {
        "name": f"{random.choice(names)}{i}",
        "city": random.choice(cities),
        "queries": random.randint(1, 300),
        "plan": random.choice(plans),
    }
    for i in range(1, 101)         
]

with open("day07_projects/json_to_csv/data.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"Generated {len(data)} rows")