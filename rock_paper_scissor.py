import random
import os

# Constants for choices
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
choices = (ROCK, PAPER, SCISSORS)

# Emoji representations for each choice
emoji_dict = {ROCK: '🗿', PAPER: '📄', SCISSORS: '✂️'}

LEADERBOARD_FILE = "leaderboard.txt"

def show_leaderboard():
    print("\n🏆 Leaderboard 🏆")
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            scores = f.read().strip()
            if scores:
                print(scores)
            else:
                print("No winners yet!")
    else:
        print("No winners yet!")
    print("-" * 30)

def get_player_name():
    name = input("Enter your name: ").strip()
    return name if name else "Player"

def get_user_choice():
    """
    Prompt the user to enter their choice.
    Keeps asking until a valid choice ('r', 'p', or 's') is entered.
    Returns the user's choice.
    """
    while True:
        user_choice = input('Rock, Paper, or Scissors? (r/p/s): ').strip().lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice. Please choose r, p, or s.')

def display_choices(player_name, user_choice, computer_choice):
    """
    Display the user's and computer's choices with emojis.
    """
    print(f'{player_name} chose {emoji_dict[user_choice]}')
    print(f'Computer chose {emoji_dict[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    """
    Determine and return the result of the game (win, lose, tie).
    """
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == PAPER and computer_choice == ROCK) or
        (user_choice == SCISSORS and computer_choice == PAPER)
    ):
        return "user"
    else:
        return "computer"

def update_leaderboard(winner_name):
    with open(LEADERBOARD_FILE, "a") as f:
        f.write(f"{winner_name}\n")

def play_game():
    """
    Main game loop. Best of 5 mode, tracks scores, rounds, and leaderboard.
    """
    show_leaderboard()
    player_name = get_player_name()
    user_score = 0
    computer_score = 0
    round_num = 1

    print("\nBest of 5 mode: First to 3 wins is the champion!\n")

    while user_score < 3 and computer_score < 3:
        print(f"\n---- ROUND {round_num} ----")
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choices(player_name, user_choice, computer_choice)
        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print(f"{player_name} wins this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score: {player_name} {user_score} - Computer {computer_score}")
        round_num += 1

    print("\n" + "=" * 30)
    if user_score > computer_score:
        print(f"🏆 {player_name} is the champion! 🏆")
        update_leaderboard(player_name)
    else:
        print("🏆 Computer is the champion! 🏆")
        update_leaderboard("Computer")
    print("=" * 30)

    print("\nFinal Leaderboard:")
    show_leaderboard()

# Start the game
play_game()

