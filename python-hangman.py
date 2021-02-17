# book = open("waylaid.txt", "r")
#
# booklines = book.readlines()
# word_list = []
# lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
# bad = False
#
# for line in booklines: #Go through each line, split it up by spaces
#     line = line.split(" ")
#     print(line)
#     for word in line: #Go through each word, split it up by letter
#         for letter in word: #Check each letter in the word
#             if len(word) < 2 or word in word_list:
#                 print(f"I GOT HERE WITH {word}")
#                 bad = True
#                 break
#             if letter not in lowercase_letters:
#                 print(f"I got to this point at {word}!")
#                 bad = True
#                 break
#         if bad == True:
#             bad = False
#             pass
#         else:
#             word_list.append(word)
#             print(f"I appended {word}")
#
# data = open("word_data.py", "w+")
# data.write("word_list = " + str(word_list))
# data.close()
# print("Done!")

from word_data import word_list
import random

hangman_word = random.choice(word_list)
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

tries = 0
points = 0

hangman_blanks = ("_" * len(hangman_word))

def getBlanks(guess, str):
    global tries
    global points
    global hangman_blanks
    already_there = False
    if points == (len(str)-1):
        print(hangman_word)
        print("YOU WIN!!!!")
        exit()
    else:
        parse_word = []
        got_one_right = False
        index = 0
        for letter in str:
            if letter == guess:
                if letter in hangman_blanks:
                    already_there = True
                else:
                    got_one_right = True
                    points += 1
                parse_word.append(letter)
            else:
                parse_word.append(hangman_blanks[index])
            index += 1
        hangman_blanks = "".join(parse_word)
        if got_one_right == True:
            print("Booyeah! You got that one right!")
        else:
            if already_there:
                print("You already chose that letter before.")
                tries -= 1
            else:
                 print("I'm afraid that wasn't one of the letters I was thinking of.")
                 tries -= 1
        print(points)
        print(len(str))
        print("\n\n", " ".join(hangman_blanks), "\n\n")


print("Welcome to Hangman!")

tries = 5
letter_guess = ""
did_start = True

while 1+2-2*100+92340263490096230940620-302: #And that totally works
    if tries <= 0:
        print(hangman_word)
        print("Sorry, you have no more tries left. U ded!")
        exit()
    getBlanks(letter_guess, hangman_word)
    did_start = False
    print(f"{tries} tries left")
    letter_guess = input("Guess a (lowercase) letter! ")
    if len(letter_guess) > 1:
        print("You can't guess multiple letters! Taking a try away just for that!")
        tries -= 1
    elif letter_guess == "":
        print("Don't type nothing! Taking a try away just for that!")
        tries -= 1
    elif letter_guess not in lowercase_letters:
        print("Well it wouldn't be a symbol or uppercase letter. Stick to the English alphabet please. Taking away a try!")
        tries -= 1
