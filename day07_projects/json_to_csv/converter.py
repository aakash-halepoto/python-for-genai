# PROJECT JSON to CSV Converter

# Why this is a real tool: data constantly needs format conversion. JSON comes from APIs; CSV goes into spreadsheets/Excel. A converter bridges them — genuinely useful, and it exercises your files + JSON + CSV + dict skills all at once.

# The build: a function that reads a JSON file (a list of dicts), and writes it as a CSV.
# TODO
import json
import csv
path = "day07_projects/json_to_csv/"

# load_json(path) → reads and returns the JSON list 

def load_json(path):
    with open(path,"r") as file:
        return json.load(file)
    
# json_to_csv(json_path, csv_path) → the core function:
# Load the JSON list
# Handle the empty case: if the list is empty, print "No data to convert" and return (guard clause)
# Get the fieldnames from the first dict's keys (hint: list(data[0].keys()) — the columns come from the data itself)
# Write to CSV with DictWriter: writeheader(), then loop and writerow each dict
# Print "Converted {n} rows to {csv_path}"
# Call it: json_to_csv("day07_projects/json_to_csv/data.json", "day07_projects/json_to_csv/output.csv")

def json_to_csv(json_path,csv_path):
    json_data = load_json(json_path)
    if not json_data:                    
        print("No data to convert")
        return
    with open(csv_path,"w",newline="") as outfile:
        writer = csv.DictWriter(outfile,fieldnames=list(json_data[0].keys()))
        writer.writeheader()
        for data in json_data:
            writer.writerow(data)

    print(f"Converted {len(json_data)} rows to {csv_path}")

json_to_csv(f"{path}data.json",f"{path}output.csv")
    