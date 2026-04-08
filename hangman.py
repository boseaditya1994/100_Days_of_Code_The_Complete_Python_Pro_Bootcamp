import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create the initial display (e.g., ["_", "_", "_", "_"])
display = []
for _ in range(word_length):
    display.append("_")

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Check each letter in the chosen_word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            # Update the display at the correct index
            display[position] = letter

    # Join the list into a string to show the user
    print(f"{' '.join(display)}")

    # Check if there are no more "_" left in display
    if "_" not in display:
        game_over = True
        print("You win!")