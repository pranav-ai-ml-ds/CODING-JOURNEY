import random

print("=== GUESS THE NUMBER GAME ===")
print("Choose difficulty:")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-500)")

choice = int(input("Enter choice: "))

if choice == 1:
    max_num = 50
elif choice == 2:
    max_num = 100
else:
    max_num = 500

secret_number = random.randint(1, max_num)
print(f"I'm thinking of a number between 1 and {max_num}")

attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess = int(input("\nEnter your guess: "))
    attempts = attempts + 1
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"🎉 CORRECT! You won in {attempts} attempts!")
        break
    
    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"Attempts remaining: {remaining}")
    else:
        print(f"Game Over! The number was {secret_number}")