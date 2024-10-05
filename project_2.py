import random


def number_gusseing_game():
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess number:"))
            attempts += 1

            if guess < target_number:
                print("Too low!")
            elif guess > target_number:
                print("Too high!")
            else:
                print(f"congratulation ! You 've guessed the number in {attempts} attempts.")
                break
        except ValueError():
            print("Invalid input. Please enter a numeric value.")


number_gusseing_game()
