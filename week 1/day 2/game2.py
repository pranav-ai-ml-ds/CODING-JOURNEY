import random

print("=== GUESS THE NUMBER GAME ===")
print("Choose difficulty:")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-500)")

choice=int(input("ENTER CHOICE:"))

if choice==1:
    max_num=50
if choice==2:
    max_num=100
if choice==3:
    max_num=500

secret_num=random.randint(1,max_num)
print(f"I'm thinking of a numbe between {max_num}")

attempts=0
max_attempts=10

while attempts<max_attempts:
    guess=int(input("\nENTER YOUR GUESS: "))
    attempts=attempts+1

    if guess<secret_num:
        print("TOO LOW,TRY AGAIN")
    elif guess>secret_num:
        print("TOO HIGH,TRY AGAIN")
    else:
        print("YOU HAVE GUESSED IT RIGHT IN ",attempts,"ATTEMPTS")
        break

    remaining=max_attempts-attempts
    if remaining>0:
        print(f"ATTEMPTS REMAINING:{remaining}")
    else:
        print(f"GAME OVER")