# Practice learning logical operator in python

# Practice, house price is 1M, if applicant has high income or good credit, same down payment as before
good_credit = False
high_income = True
price = 1000

if high_income or good_credit:
    down_payment = price * 0.1
    print("You have good credit and high income")
else:
    down_payment = price * 0.2
    print("You do not have high indcome or good credit")
print(f"Your down payment is : {down_payment}")
