### HANGMAN GAME ###

# TODO --> create a list which contains 15 words. The program will randomly choose one word from the list as the
#  hidden word
import random

print("Testing Git-Github")
# initialize the list with the 15 words
word_list = [
    "python",
    "developer",
    "algorithm",
    "variable",
    "function",
    "loop",
    "debugging",
    "syntax",
    "compiler",
    "recursion",
    "parameter",
    "dictionary",
    "exception",
    "iteration",
    "framework",
]

# random choice as the hidden word
hidden_word = random.choice(word_list)

# TODO --> create a repeated loop, which the player will enter a char, this char will be added to a list named
#  'guessed_letters'. A message will be printed which will say to the player how many times this char exists in this
#  hidden word. The hidden word is displayed in this way ---> If the char exists in the hidden word, then this char is
#  printed, otherwise a '_' will be printed

# initialize the list named 'guessed_letters and a variable to count the number of appearance of the char in the hidden
# word and the word to be guessed (empty ___)

# create a list to store the guessed letters in order not to enter them again, if they exist in the hidden word
attempted_letters = []

guessed_letters = ["_" for _ in range(len(hidden_word))]
print(hidden_word)

# initialize the max tries
max_tries = 10

# start the game
while "_" in guessed_letters:
    print(f"You have {max_tries} tries left.")
    char_choice = input("Guess a letter: ").lower()
    if len(char_choice) > 1 or char_choice.isdigit() or not char_choice.isalpha():
        print("Invalid input. Only letters! Try again.")
    else:
        if char_choice not in hidden_word:
            print("Wrong!")
            max_tries -= 1
            if max_tries == 0:
                print("You lose.")
                break
        if char_choice in attempted_letters:
            print("You have already guessed that letter.")
        for index, char in enumerate(hidden_word):
            if char == char_choice:
                guessed_letters[index] = char
                attempted_letters.append(char)
        if "".join(guessed_letters) == hidden_word:
            print("Congrats, you won!")
            break

        print("".join(guessed_letters))
