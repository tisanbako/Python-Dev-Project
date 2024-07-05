#unlike list, tupple are immutable. if you're building a program with list that you don't want
#to be modified, then use a tuple

numbers = (1,2,3)
#numbers[0] = 10 #this will give an error as we cannot modify it
print(numbers[2])