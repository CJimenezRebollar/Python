
money_owed = float(input("How much money do you owe in dollars?\n"))
apr = float(input("What is the annual percentage rate?\n"))
payment = float(input("How much is your monthly payment in dollars?\n"))
months = int(input("How long do you want to pay for in months?\n"))
# Find APR
monthly_rate = apr/100/12
for i in range(months):
# Add Interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid
    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break
# Make payment
    money_owed = money_owed - payment
# Print results
    print("Paid", payment, "of which", interest_paid, "was interest.", end=' ')
    print("Now I owe $", money_owed, sep='')