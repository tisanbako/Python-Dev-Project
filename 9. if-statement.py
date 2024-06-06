#if statements are used to set condition for something to happen. they allow us to build programs
#based on some conditions eg to code what is below

#Ex 1.
#if it's hot
     #it's a hot day
     #Drink plenty of water
     #Enjoy your day
#otherwise if it's cold
     #it's a cold day
     #Wear warm clothes
     #Enjoy your day
#otherwise
     #it's a lovely day
     #Enjoy your day

is_hot = False
is_cold = False

if is_hot:
    print("it's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("it's a cold day")    
    print("Wear warm clothes")
else:
    print("it's a lovely day")

print("#Enjoy your day")    


#Ex 2.

#Price of a house is $1M
#if buyer has good credit, they need to put down 10%
#otherwise 
#they need to put down 20%

Home_price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 10/100 * Home_price
else:
    down_payment = 20/100 * Home_price

print(f"your down payment is {down_payment}")
