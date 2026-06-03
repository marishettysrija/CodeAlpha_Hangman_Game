import random

words = ["python", "coding", "school", "gaming", "laptop"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")

while wrong_guesses < max_attempts:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong!")
        print("Attempts Left:", max_attempts - wrong_guesses)

if wrong_guesses == max_attempts:
    print("\nGame Over!")
    print("The word was:", word)