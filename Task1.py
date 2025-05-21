import random

def hangman():
    words = ["python", "hangman", "challenge", "programming", "artificial", "openai"]
    word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6  # limit on incorrect guesses
    display_word = ["_"] * len(word)

    print(" Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have", attempts, "incorrect guesses allowed.")

    while attempts > 0 and "_" in display_word:
        print("\nCurrent word:", " ".join(display_word))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    display_word[i] = guess
        else:
            attempts -= 1
            print("❌ Wrong guess. Attempts left:", attempts)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The word was:", word)

# Run the game
hangman()
