import overhead,cash_on_hand,profit_loss
def main():
    overhead.overheadfuc()
    cash_on_hand.CashonhandFUC()
    profit_loss.profitlossFUC()

main()

with open("Summary_report.txt", "w") as file:
    # Call the overhead function to get the result
    summary = main()

    # Write the result to the file
    file.write(summary)