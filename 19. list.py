names = ["John", "Bob", "Mosh", "Sarah", "Amy"]
print(names[2])
print(names[-2])
print(names[2:])
print(names[2:4])


students = ["Mike", "Job", "Posh", "Karah", "zimy"]
students[0]= "Michael"
print(students)

#write a program to find the largest number on a list

numbers = [2,4,5,8,3,0]
largest_number = max(numbers)

print(f"the largest number is {largest_number}")

#Or use for loop

the_number = [3,5,6,7,9,8,]
largest_numb = the_number[0]

for numb in the_number:
    if numb > largest_numb:
        largest_numb = numb
print(largest_numb)
