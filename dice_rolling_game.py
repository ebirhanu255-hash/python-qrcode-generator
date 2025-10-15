import random

def roll_dice():
    """Return a random number between 1 and 6 (like a dice roll)."""
    return random.randint(1, 6)

print("🎲 Welcome to the Dice Rolling Game! 🎲")

while True:
    input("Press Enter to roll the dice...")
    dice_value = roll_dice()
    print(f"You rolled a {dice_value}!")

    # Keep asking until the player gives a valid answer
    while True:
        choice = input("Do you want to roll again? (y/n): ").lower()
        if choice == "y":
            break               # go back to rolling
        elif choice == "n":
            print("Thanks for playing! Goodbye 👋")
            exit()              # stop the program completely
        else:
            print("❌ Invalid input. Please type 'y' or 'n'.")

