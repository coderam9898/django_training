# Tasks: Jul 28, 2022 Deadline: Aug 1
# 9. Create a Hangman Game , where the first input can be any string. Then you have 5
# chances to guess the word. For each chance, you get a letter to pick. If the letter is not
# contained in the string, your chance is reduced, if you enter a letter that is in the string,
# fill up the blanks with those letters and continue.
# 10. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
# 11. Write a Python program to get the maximum and minimum value in a
# dictionary.
# my_dict = {&#39;x&#39;:500, &#39;y&#39;:5874, &#39;z&#39;: 560}
# 12. Write a Python program to combine two dictionary adding values for
# common keys. d1 = {&#39;a&#39;: 100, &#39;b&#39;: 200, &#39;c&#39;:300}
# d2 = {&#39;a&#39;: 300, &#39;b&#39;: 200, &#39;d&#39;:400}
# Sample output: {&#39;a&#39;: 400, &#39;b&#39;: 400, &#39;d&#39;: 400, &#39;c&#39;: 300}
# 13. Write a Python program to create and display all combinations of
# letters, selecting each letter from a different key in a dictionary.
# Sample data : {&#39;1&#39;:[&#39;a&#39;,&#39;b&#39;], &#39;2&#39;:[&#39;c&#39;,&#39;d&#39;]}
# Expected Output:
# ac
# ad
# bc
# bd

# 14. Add two lists using map and lambda

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
# Output: [5, 7, 9]

# 15. Sort a list of string values. Once by ascending and then by
# descending according to alphabetical letters.
# a = [‘abc’, ‘def’, ‘avh’, ‘bbb’, ‘ccc’, ‘zed’, ‘zas’]

# 16. TicTacToe Game.
# Note: No need for UI. Use matrix concepts to place your ‘X’ or ‘O’. Input
# turn by turn for two players and one can win by horizontal/vertical or
# diagonal match.
# 17. Li = [‘abc’, ‘def’, ‘ghi’]
# Op = [ [‘a’,’b’,’c], [‘d’,’e’,’f’], [‘g’,’h’,’i’]]. Use map.
# 18. X = [5,10,15]
# Y = [3,6,9]
# Op = [8,16,24]. Use map and lambda
# 19. Dynamically pass parameters in a function which passes multiple positive and neg
# integers. Return sum of all the values passed.
# Eg:
# A(1,2,3) op = 6
# A(1,2,3,4) op = 10
# 20. Convert radian to degree.
# 21. Convert binary number to Decimal
# 22. Check if the first and last element in a list is equal.


#  solutions


#  17 solutions
li = ['abc', 'def' , 'ghi']
res = list(map(list,li))
print(res)