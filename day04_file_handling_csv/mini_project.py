import csv
import json
# The Support Ticket Analyzer

# Your team lead's ticket: "Support exported this week's chatbot tickets as a messy CSV. Some rows have missing fields. Build an analyzer: load it safely, compute stats, and export two files — a cleaned CSV and a JSON summary. This runs every week, so make it functions."


# Build these functions:

path = "day04_file_handling_csv/tickets.csv"

# load_tickets(path) → reads the CSV with DictReader, returns a list of dicts (hint: list(reader) converts the reader into a list in one move)
def load_tickets(path):
    with open(path, "r") as infile:
        reader = csv.DictReader(infile)
        return list(reader)


# clean_tickets(tickets) → returns a new list where every missing field is filled: 
# empty category → "uncategorized" 
# empty priority → "normal"
# empty resolved → "unknown"
# (Hint: a missing CSV field comes in as an empty string "", which is falsy — so row["category"] or "uncategorized" is a slick trick: "use category, but if it's empty, use the fallback." Try that pattern)

def clean_tickets(tickets):
    cleaned = []
    for ticket in tickets:
        new_ticket =  dict(ticket)
        new_ticket['category'] = new_ticket['category'] or 'uncategorized'
        new_ticket['priority'] = new_ticket['priority'] or 'normal'
        new_ticket['resolved'] = new_ticket['resolved'] or 'unknown'
        cleaned.append(new_ticket)
    return cleaned


# category_report(tickets) → dict counting tickets per category (your tally pattern from Day 2 — counts.get(cat, 0) + 1), using the cleaned data

def category_report(tickets):
    count = {}
    for ticket in tickets:
        category = ticket['category']
        count[category] =  count.get(category,0)+1
    return count

# resolution_rate(tickets) → percentage of tickets where resolved is "yes", rounded to 1 decimal. (Count the yeses, divide by total, times 100. Watch: round(x, 1))


def resolution_rate(tickets):
    yes_count = 0
    for ticket in tickets:
        if ticket['resolved'] == 'yes':
            yes_count +=1
    return round((yes_count/len(tickets) * 100),1)

# save_clean_csv(path, tickets) → writes the cleaned tickets to a new CSV with DictWriter (fieldnames: ["user", "category", "priority", "resolved"], writeheader(), newline="")

def save_clean_csv(path,tickets):
    with open(path,"w",newline="") as outfile:
        writer = csv.DictWriter(outfile,fieldnames=["user", "category", "priority", "resolved"])
        writer.writeheader()
        for ticket in tickets:
            writer.writerow(ticket)

# save_summary(path, **stats) → dumps the stats as JSON (your Day 2 + kwargs move 🤝)
def save_summary(path,**stats):
    with open(path,"w") as f:
        json.dump(stats,f,indent=2)



raw = load_tickets(path)
clean = clean_tickets(raw)

summary = {
    "total_tickets": len(clean),
    "by_category": category_report(clean),
    "resolution_rate": resolution_rate(clean),
}

save_clean_csv("day04_file_handling_csv/tickets_clean.csv", clean)
save_summary("day04_file_handling_csv/summary.json", **summary)
print("Analysis complete")
print(summary)
