#nested look means adding a loop inside another loop 
numbers = [5,2,5,2,2]
start_count = "x"

# for stars in numbers:
#     start_count2 = stars * start_count
#     print(start_count2)

for stars in numbers:
    for count in start_count:
        print(stars * count)


#Challenge solution from teacher
number = [5,2,5,2,2]
for x_count in number:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)

print("5" + "x")    

