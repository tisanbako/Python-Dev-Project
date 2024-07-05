numbers = [5,2,1,7,4]
numbers.append(8)   #to add number to the list
print(numbers)

numbers2 = [5,2,1,7,4]
numbers2.insert(2, 3)  #to add 3 to the position of index 2 [5,2,3,1,7,4]
print(numbers2)

numbers3 = [5,2,1,7,4]
numbers3.remove(2)   #to remover number 2
print(numbers3)

numbers4 = [5,2,1,7,4]
numbers4.clear()   #to clear everything from the lisy
print(numbers4)

numbers5 = [5,2,1,7,4]
numbers5.pop()    #to remove the last item on the list
print(numbers5)

numbers5 = [5,2,1,7,4]
print(numbers5.index(2))   #to check the index of 2
print(8 in numbers5)   #to see if an item (8) is in the list


numbers6 = [5,7,2,1,7,4]
print(numbers6.count(7))  #how many time did 7 appear on the list

numbers6 = [5,7,2,1,7,4]
numbers6.sort()  #to arrange the list. we can't wrap this with a print statement. we nned to convert it first
print(numbers6)

numbers6 = [5,7,2,1,7,4]
numbers6.reverse() #to print from 471275
print(numbers6)


name1 = [1,2,3,4,5]
name2 = []
name2.append(name1) #wrapping this in a variable will give us none
print(name2)


#EX - remove the duplicate on the list [2,5,,7,3,4,2,7]

the_list = [2,5,7,3,4,2,7]
uniques= []   #create a new variable and set it to an empty list
for items in the_list:
    if items not in uniques:
        uniques.append(items)
print(uniques)

#ex
do = [3,5,6,2,1,7,4]
do.append(3)
print(do)
