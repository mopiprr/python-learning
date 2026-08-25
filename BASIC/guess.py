# Create a simple guessing game using while loop

secret = 9
guess_att = 0
guess_limit = 3

while guess_att < guess_limit:
    num = int(input("Guess a number : "))
    guess_att = guess_att + 1
    if num == secret:
        print("Correct")
        break
    else:
        print("Wrong, guess again")
else:
    print("You failed, sucker")