import random

# Heads and Tails Game
print("\n--- Heads or Tails ---")
heads_tails = random.randint(0, 1)
print("Heads" if heads_tails == 0 else "Tails")

# Banker Roulette
print("\n--- Banker Roulette ---")
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(f"{random.choice(friends)} is paying the bill!")

# Rock Paper Scissors Game
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Choices mapping
choices = [rock, paper, scissors]
names = ["Rock", "Paper", "Scissors"]

print("\n--- Rock Paper Scissors ---")
player = int(input("What do you choose? (0) Rock, (1) Paper, (2) Scissors: "))

if player not in [0, 1, 2]:
    print("Invalid choice! Please select 0, 1, or 2.")
    exit()

print(f"\nYou chose:\n{choices[player]}")

# Computer's choice
computer = random.randint(0, 2)
print(f"\nComputer chose:\n{choices[computer]}")

# Determine the winner
if player == computer:
    print("It's a Draw! 🤝")
elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("You Win! 🎉")
else:
    print("You Lose! 😢")
