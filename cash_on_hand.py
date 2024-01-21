from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"cash-on-hand-sgd.csv"

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
        cash_on_hand.append([row[0],row[1]])   
print(cash_on_hand[0])
        

# def CashonhandFUC():
#     previous = 0
#     base_difference = 0 
#     base_day = 0
#     for item in cash_on_hand:
#         new_difference = int(item[1]) - previous 
#         previous = int(item[1])
#         if new_difference > base_difference:
#             base_difference = new_difference 
#             base_day = item[0]
#     print(base_day)
#     print(base_difference)
#     return (f"{base_day}:{base_difference}")

# print (CashonhandFUC())

# print(cash_on_hand[0][1])



def CashonhandFUC():
    previous = 0
    deficit_list = []
    daylist = []
    for item in cash_on_hand:
        new_difference = int(item[1]) - previous 
        previous = int(item[1])
        if new_difference < 0:
            deficit_list.append(new_difference)
    # Sort deficit_list by deficit amount in ascending order
    deficit_list.sort()
    # Get the top 3 highest deficit amounts and their corresponding days
    top_3_deficits = deficit_list[0:3]
    for diff in top_3_deficits:
        difference = abs(diff)
        print(f'{day},{difference}')
    print (daylist)
    # Print the top 3 highest deficit amounts and their corresponding days
    return ""
print(CashonhandFUC())