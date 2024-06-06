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
   
print("Have a good day")
   
#EX2. 
#If name is less than 3 characters long
      #name must be at least 3 characters
#otherwise if it's more than 50 characters long
      #name can be a maximum of 50 characters
#otherwise
     #name looks good!


name = input("What is your name? ")
name_characters = len(name)
#me name = len(input("What is your name? "))

if name_characters < 3:
    print("Name must be atleast 3 characters")
elif name_characters > 50:
    print("Name can only be a maximum of 50 characters")
else:
    print("Name looks good!")

