# convert a matrix : [[1,2], [3,4], [5,6],[7,8]] into [[1,3,5,7][2,4,6,8]]
def matrix():
 matrix1 = [[1,2], [3,4], [5,6],[7,8]]
 
 for row in matrix1:
  print(row)
  for i in range(2):
    print(row[i])
matrix()