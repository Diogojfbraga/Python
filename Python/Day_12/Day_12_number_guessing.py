import art
import random

# Display the ASCII art logo
print(art.logo)
print('\n' * 2)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Main game function
def start_game():
    secret_number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    # Set number of attempts based on difficulty
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Invalid option. Try again.\n")
        return start_game()

    play_round(secret_number, attempts)

# Function that runs one guessing round
def play_round(secret_number, attempts):
    while attempts > 0:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess > secret_number:
            print("Too high.")
        elif guess < secret_number:
            print("Too low.")
        else:
            print(f"You got it! The number was {secret_number}. 🎉")
            return ask_to_restart()

        attempts -= 1
        print(f"You have {attempts} attempt(s) remaining.\n")

    # If the user runs out of attempts
    print(f"You lost. The number was {secret_number}.")
    ask_to_restart()

# Ask the player if they want to play again
def ask_to_restart():
    choice = input("Start again? 'Y' or 'N': ").lower()
    if choice == 'y':
        print('\n' * 3)
        start_game()
    else:
        print("Bye Bye 👋")
        exit()

# Start the game
start_game()
