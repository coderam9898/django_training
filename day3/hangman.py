


# need lives

lives = 5
phrase = "github"
guessed = []
temp_phrase = ""

for letter in phrase:
    if letter != " ":
        temp_phrase += "_"
    else:
        temp_phrase = " "

print(temp_phrase)
guess_letter = ""
while len(guess_letter)!=1:
    guess_letter = input(" guess a letter: ").lower()
    if len(guess_letter)>1:
        print(" Enter only one letter at a time!")
        guess_letter = ""
    elif guess_letter in guessed:
        print("already guessed letter")
    else:
        guessed.append(guess_letter)