secret_number = 12
attempts = 0
guessed_correctly = False
while attempts < 5 and guessed_correctly == False:
    guess = input("Enter guess: ")
    if not guess.isdigit():
        print("Guess must be numeric")
    else:
        guess = int(guess)
        if guess < 0 or guess > 20:
            print("Guess out of range")
        else:
            attempts = attempts + 1
            if guess == secret_number:
                print("Corret!")
                guessed_correctly = True
            else:
                if guess < secret_number:
                    print("Too low")
                else:
                    print("Too high")
if guessed_correctly == False:
    print(f"The secret number is: {secret_number}")