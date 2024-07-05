#Tis is used mostly in data science and machine learning
#this is like a list in a list eg

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1])  #to acess 2 from the first inner list
matrix[1][2] = 10  #we changing the value of 6 (in the second list) to 10
print (matrix)

#EX2 LETS INTERATE OVER A 2-D LIST
numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in numbers:
    for item in row:
        print(item)