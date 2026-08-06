# Day 4 — File Handling + CSV

## Files = borrowing a library book
open() = take the book. The `with` block = the librarian who
GUARANTEES the book gets returned, even if I faint mid-read.

with open("file.txt", "r") as f:
    ...

## The three modes (know these cold)
"r" → READ   (book must exist, or crash)
"w" → WRITE  (WIPES the file blank first, THEN writes) ⚠️💀
"a" → APPEND (adds to the end, wipes nothing)

"w" is a DESTROYER. Opening a file in "w" empties it instantly.
NEVER open my input file in "w" — it erases my source data.

## Reading: gulp vs sips
f.read()        → whole file as ONE string (one gulp) 🥤
f.readlines()   → list of lines
for line in f:  → line by line (best for HUGE files, memory-safe)

## Newline discipline
Each written line ends with \n. print() ALSO adds \n.
So looping + print without .strip() = double newline = blank lines.
Fix: print(line.strip())  → shaves the trailing \n.
.read() prints clean because it's ONE print, not one-per-line.

## Writing text
f.write("line\n")   → I must add \n myself, write() doesn't auto-newline.

## CSV = a table written as text
First row = headers (column names). Every row after = one record.
name,city,queries
Ali,Hyderabad,45

## csv.DictReader — the magic (week converges here!)
import csv
with open("users.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["name"]   # each row is a DICT, headers become keys!

A CSV loaded this way = my list-of-dicts from Day 2, arriving from disk.
Every dict skill (.get(), [key], .items()) instantly works.

## THE #1 CSV TRAP: everything is a string
row["queries"] is "45" (text), NOT 45.
"45" + 10 → CRASH. Must convert: int(row["queries"]).
Always ask: is this a string or a number RIGHT NOW?

## csv.DictWriter — writing CSV
with open("out.csv", "w", newline="") as f:   # newline="" = known incantation 🪄
    writer = csv.DictWriter(f, fieldnames=["name", "city"])
    writer.writeheader()                       # writes column names row
    writer.writerow({"name": "Ali", "city": "Hyderabad"})

newline="" prevents blank rows on Windows. Always include it for CSV.

## The read-transform-write pipeline
Read one file → transform each row → write a NEW file.
This is the shape of EVERY real data-processing job. 🔄

## Craft upgrades I learned
1. The `or` fallback trick:
   row["category"] or "uncategorized"
   → "use category, but if it's empty (falsy), use fallback"
   One operator replaces a whole ternary.

2. dict(ticket) makes a COPY:
   A cleaning function shouldn't secretly destroy its input.
   new = dict(ticket) → modify new → original stays pristine.
   ("returns a NEW list" means the original must survive.)

3. DRY — Don't Repeat Yourself:
   Compute the varying part once, build the row once.
   Duplication is where bugs breed.




