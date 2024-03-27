# Import yjr random module
import random
# Generate a random number between 1 and 10
secret_number = random.randint(1,10)
# Maximum aattempts allowed
max_attempts = 3
# Function to display a welcome message
def welcome_message():
    print("\nWelcome to the Number Guesssing Game!")
    print(f"You have {max_attempts} attempts to guess the correct number. ")
# Function for receiving guessing
def guess_recursive (attempts_left):
    #Get user input
    guess = int(input("\nGuess the number(between 1 and 10)"))
# Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number!")
    else:
        print(f"Wrong guess. Attempt left: {attempts_left}")
        if attempts_left >1:
            # Make a recursive call for another guess
            guess_recursive(attempts_left - 1)
        else: print(f"\nSorry, you couldn't guess the number. The correct number was {secret_number}.")
# Calling the function
welcome_message()
guess_recursive(max_attempts)
# Using id() to get mamorary addresses
print(f"Memory adress of Secrete Number {secret_number} is : {id(secret_number)}")


