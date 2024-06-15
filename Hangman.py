import random
import time

# Welcome message
print("\nWelcome to Hangman game by IT SOURCECODE\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)

words_to_guess = ["january","border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]
already_guessed = []

def main():
    global count
    global display
    global word
    global play_game
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = "_" * length
    while True:
        play_game = input("Do You want to play again? y = yes, n = no \n").lower()
        if play_game in ("y", "n"):
            break
        print("Invalid input. Please enter 'y' or 'n'.")

    if play_game == "y":
        main()
    else:
        print("Thanks For Playing! We expect you back again!")
        exit()


def hangman():
    global count
    global display
    global word
    global already_guessed

    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n").lower().strip()

    if not guess.isalpha() or len(guess) != 1:
        print("Invalid Input, Try a single letter\n")
        hangman()

    if guess in word:
        already_guessed.append(guess)
        new_display = ""
        for i in range(length):
            new_display += guess if word[i] == guess else display[i]
        display = new_display
        print(display + "\n")

    elif guess in already_guessed:
        print("You already guessed that letter. Try another.\n")

    else:
        count += 1

        hangman_stages = [ t
            """
  _____ 
 |   \n
 |   \n
 |   \n
 |   \n
 |   \n
 |   \n
"__|__\n""",
            """
  _____ 
 |   | \n
 |   |\n
 |   \n
 |   \n
 |   \n
 |   \n
"__|__\n""",
            """
  _____ 
 |   | \n
 |   |\n
 |   | \n
 |   \n
 |   \n
 |   \n
"__|__\n""",
            """
  _____ 
 |   | \n
 |   |\n
 |   | \n
 |   O \n
 |   \n
 |   \n
"__|__\n""",
            """
  _____ 
 |   | \n
 |   |\n
 |   | \n
 |   O \n
 |  /|\ \n
 |  / \ \n
"__|__\n""",
            """
  _____ 
 |   | \n
 |   |\n
 |   | \n
 |   O \n
 |  /|\ \n
 |  / \ \n
"__|__\n"""
        ]

        if count < limit:
            print(hangman_stages[count - 1]) 
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        else:
            print(hangman_stages[limit - 1])
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", word)

    if display == word:
        print("Congrats! You have guessed the word correctly")
