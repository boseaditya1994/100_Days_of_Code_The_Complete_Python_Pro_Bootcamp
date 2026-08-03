import random

# Constants for difficulty levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    """Prompt user for difficulty and return the total number of turns."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "hard":
        return HARD_LEVEL_TURNS
    elif level == "easy":
        return EASY_LEVEL_TURNS
    else:
        print("Invalid choice. Defaulting to 'easy'.")
        return EASY_LEVEL_TURNS

def check_answer(guess, number):
    """Compares guess against the random number and returns True if correct."""
    if guess < number:
        print("Too low.")
        return False
    elif guess > number:
        print("Too high.")
        return False
    else:
        print(f"You got it! The answer was {number}.")
        return True

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number = random.randint(1, 100)
    turns = set_difficulty()
    guess = None

    while turns > 0:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        
        # Safely handle non-integer input
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Check the guess
        if check_answer(guess, number):
            return  # End game early on correct guess
        
        turns -= 1
        
        if turns > 0:
            print("Guess again!")

    print(f"\nYou've run out of guesses! The number was {number}. You lose.")

# Start the game
game()