
import random
Correct_number = random.randint(1, 100)
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    user_input = input(f'Guess the number between 1 and 100 (Attempt {attempts + 1} of {max_attempts}): ')
    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue
    Guessed_number = int(user_input)
    attempts += 1
    if Guessed_number > Correct_number:
        print("Too high!")
    elif Guessed_number < Correct_number:
        print('Too low!')
    elif Guessed_number == Correct_number:
        print('Congratulations! You guessed the number correctly!')
        break
else:
    print(f'Sorry, you have used all {max_attempts} attempts. The correct number was {Correct_number}.')

