import art
import game_data
import random

# Initialize score
score = 0

def game_start(score):
    """
    Starts the Higher-Lower game with two random options from the game data.
    The user guesses who has more followers.
    """

    # Randomly choose two different options
    first_option = random.choice(game_data.data)
    second_option = random.choice(game_data.data)

    # Ensure both options are not the same
    while second_option == first_option:
        second_option = random.choice(game_data.data)

    # Display game logo
    print(art.logo)

    # Display both options
    print(f"Compare A: {first_option['name']}, a {first_option['description']}, from {first_option['country']}.")
    print(art.vs)
    print(f"Compare B: {second_option['name']}, a {second_option['description']}, from {second_option['country']}.")

    # Ask user for input
    try:
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    except:
        print("That is not a correct choice.")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if the user guessed correctly
    if choice == 'a' and first_option["follower_count"] > second_option["follower_count"]:
        score += 1
        print(score)
        game_start(score)  # Recursively continue the game

    elif choice == 'b' and second_option["follower_count"] > first_option["follower_count"]:
        score += 1
        print(score)
        game_start(score)

    else:
        # Game ends if user guessed incorrectly
        print("Game over")
        print(f"Final Score: {score}")

# Start the game
game_start(score)
