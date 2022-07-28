import random
from time import sleep

# from hangman import Hangman

phrases = ["python", "test", "spam", "hangman", "anaconda", "something", "random", "more", "Monty Python",
           "Black belt", "Donald Trump", "coding", "snake", "whatever", "You get it"]

# hangman = Hangman()

phrase = phrases[random.randint(0, len(phrases) - 1)]
work_phrase = phrase.lower()
illu_phrase = ""
already_guessed = []

# Now you can have spaces in the phrase
for letter in work_phrase:
    if letter != " ":
        illu_phrase += "_"
    else:
        illu_phrase += " "

lives = 6

while "_" in illu_phrase and lives != 0:
    # aprint(hangman.get_art_str(lives))
    print("\nThe searched phrase has a length of {}: {}".format(len(illu_phrase) - illu_phrase.count(" "), illu_phrase))
    print("Lives left: {}".format(lives))

    guess_letter = ""
    while len(guess_letter) != 1:
        guess_letter = input("Guess a letter: ").lower()
        if len(guess_letter) > 1:
            print("Only one letter at a time!")
            guess_letter = ""
        elif guess_letter in already_guessed:
            print("You already tried this letter. Try again...")
            guess_letter = ""
        else:
            already_guessed.append(guess_letter)

    current_indexes = []

    if guess_letter not in work_phrase.lower():
        lives -= 1
        print("\nYou lost a life...")
        sleep(2)

    while guess_letter in work_phrase.lower():
        guess_index = work_phrase.find(guess_letter)
        work_phrase = work_phrase.replace(guess_letter, "^", 1)
        current_indexes.append(guess_index)

    temp = ""

    for index in range(0, len(illu_phrase)):
        if index in current_indexes:
            temp += guess_letter
        elif illu_phrase[index] != "_":
            temp += illu_phrase[index]
        else:
            temp += "_"
    illu_phrase = temp

if lives > 0:
    print("You have guessed the phrase. It was {}".format(phrase))
else:
    # print(hangman.get_art_str(lives))
    print("\nThe searched phrase has a length of {}: {}".format(len(illu_phrase) - illu_phrase.count(" "), illu_phrase))
    print("You have lost all your liefs. Now you hang! (The searched phrase was {}.)".format(phrase))
