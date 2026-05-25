import random


def play_hangman():
    # 1. Use a small list of 5 predefined words
    word_list = ["mirror", "crochet", "football", "bolling", "apple"]

    # 2. Key Concept: random (to choose a word)
    secret_word = random.choice(word_list)

    # 3. Limit incorrect guesses to 6

    max_incorrect_guesses = 6
    incorrect_guesses = 0

    # Key Concept: lists (to store guessed letters)
    guessed_letters = []

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.")

    # 4. Key Concept: while loop
    while incorrect_guesses < max_incorrect_guesses:

        # Display the current state of the word (Key Concept: strings & loops)
        display_word = ""
        has_won = True

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
                has_won = False

        print(f"\nWord: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")

        # Check if the player has guessed all the letters
        # 5. Key Concept: if-else
        if has_won:
            print(f"\nCongratulations! You guessed the word '{secret_word}' correctly!")
            break

        # Get input from the user (Basic console input/output)
        guess = input("Guess a letter: ").lower()

        # Basic validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        # Add the valid guess to our list of guessed letters
        guessed_letters.append(guess)

        # Check if the guess is incorrect
        if guess not in secret_word:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1
        else:
            print(f"Good job! '{guess}' is in the word.")

    # Check if the loop ended because the player ran out of guesses
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nGame Over! You ran out of guesses. The word was '{secret_word}'.")


# Start the game
if __name__ == "__main__":
    play_hangman()
