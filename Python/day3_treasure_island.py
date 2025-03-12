print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

# First choice: Left or Right
left_or_right = input("Do you want to go left or right? ").lower()

if left_or_right == "left":
    # Second choice: Swim or Wait
    swim_or_wait = input("Do you want to swim or wait? ").lower()

    if swim_or_wait == "wait":
        # Third choice: Choose a door
        which_door = input("Which door do you choose? Red, Blue, or Yellow? ").lower()

        if which_door == "red":
            print("Burned by fire.\nGame Over.")
        elif which_door == "yellow":
            print("You Win!")
        elif which_door == "blue":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("Invalid choice.\nGame Over.")
    else:
        print("Attacked by a trout.\nGame Over.")
else:
    print("You fell into a hole.\nGame Over.")
