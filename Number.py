import random

# Computer chooses a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("🎮 Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
        break

# This code implements a simple number guessing game where the computer selects a random number between 1 and 100, and the user tries to guess it. The program provides feedback on whether the user's guess is too low, too high, or correct, and keeps track of the number of attempts.
# You can run this code in a Python environment to play the game. Enjoy!
# Feel free to modify the code to add more features, such as a scoring system or a limit on the number of attempts!
# Happy coding! 😊