#we use function to break our code to smaller reusable chunck

def greet_user1():
    print("Hi there!")
    print("Welcome aboard")


#to call the function
greet_user1()    

#Parameters: this are place holders for receiving information
def greet_user2(name):
    print(f"Hi {name}")
    print("Welcome aboard")

greet_user2("John")
greet_user2("Mary")  

#"Parameters" are the placeholders(name) while "arguments" (John, Mary) are the value or piece 
#of information for the parameter

#Whenever we define a parameter in our functions, we have to supply the value when calling it.
#If the parameter we defines is one, when calling we nned to provide one value, if it's 2, we need
#to provide two values, if not we will get an error
def greet_user3(first_name, last_name):
    print(f"Hi {first_name, last_name}")
    print("Welcome aboard")

greet_user3("John", "Carey")
greet_user3("Mary", "Mathew") 
print("nice to meet you")

#Positional & keyword arguments: 