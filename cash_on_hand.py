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
# print(cash_on_hand)
        

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
    for item in cash_on_hand:
        new_difference = int(item[1]) - previous 
        previous = int(item[1])
        if new_difference < 0:
            day=item[0]
            # deficit_list.append(new_difference)
            deficit_list.append([day, abs(new_difference)])
            print(f'[CASH DEFICIT]Day:{day}, Difference: SGD{abs(new_difference)}')
                # Sort deficit_info by deficit amount in descending order
    deficit_list.sort(key=lambda x: x[1], reverse=True)

    # Print the top 3 highest deficit amounts and their corresponding days
    for i, (day, difference) in enumerate(deficit_list[:3], start=1):
        if i == 1:
            ordinal = ""
        elif i == 2:
            ordinal = "2ND"
        else:
            ordinal = "3RD"
        print(f'[{ordinal} HIGHEST DEFICIT] Day: {day}, Difference: SGD{difference}')
    return ""
print(CashonhandFUC())


    # # Sort deficit_list by deficit amount in ascending order
    # deficit_list.sort()
    # # Get the top 3 highest deficit amounts and their corresponding days
    # top_3_deficits = deficit_list[0:3]
    # for diff in top_3_deficits:
    #     day =item[0]
    #     difference = abs(diff)
    #     print(f'{day}:{difference}')
    
    # print(daylist)
    # print(deficit_list)

    # Print the top 3 highest deficit amounts and their corresponding days
#     return ""

 # daylist.append(day)
            # for things in deficit_list:
            #     diff = things[1]
            #     differncelist.append(diff)
            #     day=things[0] 
            # differncelist.sort()
            # top_3_deficits = differncelist[0:3]
            # for i in top_3_deficits:
            #     if diff == i:
            #         days=day    
            #     print(f'{days}:{i}')   
            # print(differncelist)   

# print(CashonhandFUC())