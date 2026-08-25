# Practice condition in python stuff

# if name is less than 3 char, "name must be longer than 3 char"; if more than 50, "name too long"; else "accepted"

name = input("What is your name : ")

# if len(name) <= 3:
#     print(f"Your name {name} is too short, name must be more than 3 characters")
# elif len(name) >= 50:
#     print(f"Your namme {name} is too long, name mustt be less than 50 caracters")
# else:
#     print(f"Hi {name}, Welcome to Gotham City")

if len(name) <=3 or len(name) >= 50:
    print("Name invalid, must be between 3 to 50")
else:
    print(f"Hi {name}, welcome to Gotham City")