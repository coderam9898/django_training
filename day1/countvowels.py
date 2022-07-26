vowel = ['a', 'e', 'i', 'o', 'u']
Sentence = input("Enter a phrase: ")
count = 0
for letter in Sentence:
    if letter in vowel:
        count += 1
print(count)