"""
Day 03 – Number Guessing Game
The loop continues until the user guesses the secret number.
"""

secret_number = 7

while True:
    guess = int(input("Guess the number (1 to 10): "))

    if guess < secret_number:
        print("Too low. Try again!")
    elif guess > secret_number:
        print("Too high. Try again!")
    else:
        print("Correct! You guessed the number.")
        break
