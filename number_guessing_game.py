

# Import the random module to generate a random number
import random

def play_game():
    # Generate a random number between 1 and 100
    Correct_number = random.randint(1, 100)
    # Set the maximum number of attempts allowed
    max_attempts = 5
    # Initialize the attempt counter
    attempts = 0

    # Loop until the user reaches the maximum number of attempts
    while attempts < max_attempts:
        # Ask the user to guess the number
        user_input = input(f'Guess the number between 1 and 100 (Attempt {attempts + 1} of {max_attempts}): ')
        # Check if the input is a valid number
        if not user_input.isdigit():
            # If not a number, prompt the user again
            print("Please enter a valid number.")
            continue
        # Convert the input to an integer
        Guessed_number = int(user_input)
        # Increment the attempt counter
        attempts += 1
        # Check if the guessed number is higher than the correct number
        if Guessed_number > Correct_number:
            print("Too high!")
        # Check if the guessed number is lower than the correct number
        elif Guessed_number < Correct_number:
            print('Too low!')
        # Check if the guessed number is correct
        elif Guessed_number == Correct_number:
            print('Congratulations! You guessed the number correctly!')
            break
    # If the user runs out of attempts, show the correct number
    else:
        print(f'Sorry, you have used all {max_attempts} attempts. The correct number was {Correct_number}.')

    # Ask the player if they want to play again after either win or lose
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again == 'y':
        print("\nStarting a new game...")
        return True
    else:
        print("Thanks for playing!")
        return False

# Main loop to repeatedly play the game and ask the player if they want to play again
while True:
    # Run one round of the guessing game and check if the player wants to play again
    if not play_game():
        break

