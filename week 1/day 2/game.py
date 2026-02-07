import random

secret_number=45

print("===GUESS THE NUMBER GAME===")
print("I'm thinking of a number between 1 and 100")

attempts=0
guessed=False

while not guessed:
    guess=int(input("\nENTER YOUR GUESS: "))
    attempts=attempts+1

    if guess<secret_number:
        print("TOO LOW!,TRY again")
    elif guess>secret_number:
        print("TOO HIGH,TRY AGAIN")
    else:
        print("CORRECT,YOU GUESSED IT IN",attempts,"attempts")
        guessed=True

