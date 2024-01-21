from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"overheads-day-90.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for overhead
    overheads=[] 

    # append overhead into the overhead list
    for row in reader:
        #get the category and overhead for each record
        #and append to the overhead list
        overheads.append([row[0],row[1]])   
print(overheads)

