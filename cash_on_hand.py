from pathlib import Path
import csv

fp = Path.cwd()/"csv_report"/"cashonhand.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for delivery record
    cash_on_hand=[] 

    # append delivery record into the deliveryRecords list
    for row in reader:
        #get the driver id, sales, distance, and event type for each record
        #and append to the deliveryRecords list
        cash_on_hand.append([row[0],row[1],row[2],row[3]])   
# print(cash_on_hand)
        
