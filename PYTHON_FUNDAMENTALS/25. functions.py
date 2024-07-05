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

#Positional & keyword arguments: in the above calling of functions john is the first_name and Carey
#is the second name. if we write care first while calling the function, that would make carey the 
#first name. if we want to be specific we can use keyword argument (although most times it is
#the positional argument that we use) ex of keyword arguments to call greet_user3

greet_user3(last_name="Carey", first_name="John") #even id i mix the params positions when calling

#Positional argument before ketword argument.
def greet_user4(first_name, last_name):
    print(f"Hi {first_name, last_name}")
    print("Welcome aboard")

greet_user4("James", last_name="Terry") 