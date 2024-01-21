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
# print(overheads)


category = []  
for item in overheads:
    if item[0] not in category:
        category.append(item[0])
print(category)
percentagelist=[]
def overheadfuc(cat):
    total_summary=0
    for things in overheads:
        if things[0] == cat:
            total_summary += float(things[1])
            percentage = round(total_summary/3,2)
            percentagelist.append(percentage)
    return percentage

overalllist = []
for them in category:
    overall=overheadfuc(them)
    overalllist.append(overall)
    Highest = max(overalllist)
print(f"[Highest Overhead]{them}:{Highest}")
    
print(overalllist)





