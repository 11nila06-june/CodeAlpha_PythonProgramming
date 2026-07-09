import random

words = ["python", "computer", "apple", "coding", "internship"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("===== Hangman Game =====")

while wrong_guesses < max_guesses:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter.")
        continue

    if guess in guessed_letters:
        print("Letter already guessed.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")
        print("Remaining Attempts:", max_guesses - wrong_guesses)

if wrong_guesses == max_guesses:
    print("\nGame Over!")
    print("The word was:", word)
