# Task 1 — Write and read a log
# Your chatbot needs to log queries to a file. Write code that:
# Opens query_log.txt in write mode and writes these three lines (each on its own line — remember \n):
#    Ali: How do I renew my CNIC?
#    Zara: What are FBR deadlines?
#    Bilal: Where is NADRA office?
# Then opens the same file in read mode and prints its entire contents with .read()
# Then opens it again, looping line by line, printing each with its line number using enumerate (start=1) — and .strip() each line to kill the double-spacing

path = "day04_file_handling_csv/"

with open(f"{path}query_log.txt", "w") as f:
    f.write("Ali: How do I renew my CNIC?\n")
    f.write("Zara: What are FBR deadlines?\n")
    f.write("Bilal: Where is NADRA office?\n")


with open(f"{path}query_log.txt", "r") as f:
    print(f.read())

with open(f"{path}query_log.txt", "r") as f:
    for index, line in enumerate(f,start=1):
        print(f"{index}. {line.strip()}")



print()
print("Task 02 - CSV")

import csv

with open(f"{path}users.csv","r") as f:
    reader = csv.DictReader(f)
    total_queries = 0
    for user in reader:
        total_queries += int(user['queries'])
        print(f"{user['name']} from {user['city']} - {user['queries']} queries")
    print(f"Total Queries: {total_queries}")

print()

print("Task - 03")

# Write a CSV (the DictWriter side):

# Using the same data you just read, write a new file report.csv that adds a computed column. For each user, write: name, city, queries, and a new "status" column — "active" if queries ≥ 50, else "inactive".

# Steps:
# Read users.csv with DictReader (you've got this)
# For each row, compute the status
# Write to report.csv with DictWriter — fieldnames ["name", "city", "queries", "status"], remember writeheader() first, and newline="" in the open 

with open(f"{path}users.csv", "r") as infile, open(f"{path}report.csv", "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=["name", "city", "queries", "status"])
    writer.writeheader()

    for user in reader:
        user["status"] = "active" if int(user["queries"]) >= 50 else "inactive"
        writer.writerow(user)

# with open(f"{path}users.csv","r") as f:
#     reader = csv.DictReader(f)

#     with open(f"{path}report.csv", "w",newline="") as f:
#             writer = csv.DictWriter(f,fieldnames=["name","city","queries","status"])
#             writer.writeheader()
#             for user in reader:
#                 status = "active" if int(user["queries"]) >= 50 else "inactive"
#                 if int(user["queries"]) >= 50:
#                     writer.writerow({
#                         "name":user['name'],
#                         "city":user['city'],
#                         "queries":user['queries'],
#                         "status":status})

               


# The interesting bit: you're reading one file and writing another in the same program — the read-transform-write pipeline, which is the actual shape of every real data-processing job.

# Expected report.csv:

# csv
# name,city,queries,status
# Ali,Hyderabad,45,inactive
# Zara,Karachi,120,active
# Bilal,Lahore,30,inactive
# Omar,Hyderabad,75,active