# 2-D List
matrix = [[1,2], [3,4], [5,6],[7,8]]

l2 = []
l3 =[]

for sublist in matrix:
	for val in sublist:
		l2.append(val)

odd = [x for x in l2 if x %2!=0]
even = [x for x in l2 if x %2==0]

l3.append(odd)
l3.append(even)
print(matrix)
print(l2)
print(odd)
print(even)
print(l3)




            

