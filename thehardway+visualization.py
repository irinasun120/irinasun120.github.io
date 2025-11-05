import csv
import os

#Computing mean, mode, median
values = []
# Put CSV in same folder as this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "COVID-19_Community_Profile_Report_-_County-Level.csv")
with open(CSV_PATH, newline='') as f:
    read_data = csv.DictReader(f)
    for row in read_data:
        try:
            value = float(row['total_cases'])
            values.append(value)
        except: 
            pass # skip missing or bad data

# Mean
mean_manual = sum(values) / len(values)

# Median
values_sorted = sorted(values)
n = len(values)
if n % 2 == 1:
    median_manual = values_sorted[n // 2]
else:
    median_manual = (values_sorted[n // 2 - 1] + values_sorted[n // 2]) / 2

# Mode
mode_manual = max(set(values), key=values.count)

print("Mean of total_cases:", mean_manual)
print("Median of total_cases:", median_manual)
print("Mode of total_cases:", mode_manual)



# Data visualization （Using standard library version)
# Configuration
MAX_BARS = 20          # number of counties to show
BAR_CHAR = "🦠"         # emoji (can change to "*" or anything else)
BAR_WIDTH = 50          # max bar width in characters

# READ DATA
rows = []
with open(CSV_PATH, newline='') as f:
    for r in csv.DictReader(f):
        try:
             # remove commas and spaces, convert total_cases to a number
            v = float(str(r['total_cases']).replace(',', '').strip())
            if v > 0: # skip zeros or missing data
                rows.append((r['county'], v))
        except:
            pass  # skip rows that can’t be converted to numbers

# Keep top 20 and scale
rows.sort(key=lambda x: x[1], reverse=True)  # sort by total_cases, descending
rows = rows[:MAX_BARS]                       # keep only top 20
max_val = max(v for _, v in rows)            # largest number of cases
unit = max(int(max_val / BAR_WIDTH), 1)      # each emoji represents about how many cases
scale = BAR_WIDTH / max_val if max_val else 1  # how wide each bar should be

# Draw

# Alignment width based on the longest county name
name_w = max(len(name) for name, _ in rows)

print("\nCOVID-19 Total Cases (Top Counties) by 2023/5/12\n")
print(f"Each {BAR_CHAR} ≈ {unit:,} cases\n")

# Print aligned bars, no vertical bar
for name, val in rows:    # loop through each county and its total case count
    n = max(1, int(val * scale))    # decide how long the bar should be; at least 1 symbol long
    bar = BAR_CHAR * min(n, BAR_WIDTH)  # make a string of that many emojis but cap the max width
    print(f"{name:<{name_w}}  {bar}")   # print the county name left-aligned, then its bar

#Full data interpretation and analysis is in project1_irina.ipynb