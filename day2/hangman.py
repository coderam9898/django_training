# Guess the letter
i = 0
l  = 5
g1 = "letter"
guessed = []
i_phrase = ""
word = 'ram'
def Guess():
    
    print('your life : ',l)
    x = input('guess :')
    if x == g1:
     print(g1,'=',x)
     print('You win')
     iter()
    else:
     change()
     
     iter()


def iter():
    
    i = str(input('Do you want to play again (y/n): '))
    j = 5
    if i == 'y' or i=='Y':
        Guess()
    else:
        print('bye bye')
def change():
    g1 = 'guard'   

def check_word(character, word):
    indexes = []
    for n in range(len(word)):
        if character == word[n]:
            indexes.append(n)
    return indexes 
    print(indexes)
check_word('r', 'ram')



