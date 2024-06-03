#we use comparison operators in situations where we want to compare a variable with a value ef

#ex1. 

#if temperatute is greater than 30
   #It's a hot day
#otherwise if it's less than 10
   #it's a cold day
#otherwise
   #it's neither hot or cold 

#we can define (hardcode) a variable eg temperature = 35
temperature = int(input("what is the temperature? "))
#temperature = int(temperature)

if temperature > 30:
    print("its a hoy day")
 
elif temperature < 10:
    print("it's a cold day")

else:
    print("it's neigher hot not cold") 
   
