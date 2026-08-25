# Practice if else statement in python

score = 89

if score >= 90:
    print("You got an A")
elif score >= 80:
    print("You got a B")
else:
    print("You got a C")



x = 90
if x == 10:
    print(f"Yes, {x} is correct")
else:
    print(f"{x} is the correct answer")

# Practice
# a house price is 1M, if buyer has good gredit, the putdown 10%, otherwise put down 20%. Print the down payment

price = 1000
credit_good = True

if credit_good:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"the price for down payment is : ${down_payment}")