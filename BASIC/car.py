# Create a simple car game where you can start the car, stiop the car, and exit program

command = ""
started = False
stopped = False

while command.lower() != "quit":
    command = input(">").lower()
    if command == "start":
        if started:
            print("The car already started")
        else:
            started = True
            print("You start the car")
    elif command == "stop":
        if stopped:
            print("The car already stopped")
        else:
            stopped = True
            print("You stopped the car")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit game""")
    elif command == "quit":
        break
    else:
        print("Command unknown")
