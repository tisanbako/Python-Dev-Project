#

for item in "python":
    print(item)

for names in ["jerry", "james", "john"]:
    print(names)

for numbers in [1,2,3,4,5]:
    print(numbers)    

#when we have a long list of item, we don't have to write all the item, we use range eg

for numberz in range(10):
    print(numberz)

#lets calculate the prices of thre goods in a shopping cart

prices = [10, 20, 30]
total = 0

for amount in prices:
    total = total + amount
print(total)
        
    