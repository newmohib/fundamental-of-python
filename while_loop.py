
# while Loop

i = 1

while i <= 5:
    print('*' * i)
    i += 1
print("Done")

# Guessing Game

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1

    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry You Failed!")



# car game

command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            print("Car started...")
            started = True
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started =False
            print("Car Stopped.")
    elif command == "quit":
        print("Game is Exit")
        break
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    else:
        print("Sorry I don't understand that! for help type help")



