#The not logical operator is used in programming and logic to invert a boolean value. It converts 
#True to False and False to True. This can be useful in various scenarios, such as condition 
#checking, loop control, and ensuring certain conditions are not met. 
#Here are some common use cases and examples:

#1. Conditional Statements : When you want to execute a block of code only if a certain condition is not true.

is_raining = False

if not is_raining:
    print("You don't need an umbrella today.")




#2. Loop Control: To continue or break out of a loop based on a condition that should not be true.

password_correct = False

while not password_correct:
    password = input("Enter the password: ")
    if password == "secret":
        password_correct = True
    else:
        print("Incorrect password, try again.")



#3. Function Return Values :To check if a function returns False or an empty value, and then take action.

def is_user_logged_in():
    # This function returns True if the user is logged in, False otherwise
    return False

if not is_user_logged_in():
    print("Please log in to continue.")




#4. Boolean Algebra :Inverting conditions in complex logical expressions.
a = True
b = False

result = not (a and b)  # True, because (a and b) is False, and not False is True



#5. Ensuring Certain Conditions Are Not Met: To ensure that certain conditions are explicitly not met.
items = ["apple", "banana", "cherry"]

if "orange" not in items:
    print("Orange is not in the list.")



#6. User Input Validation: To check if user input does not meet certain criteria.
user_input = input("Enter a number: ")

if not user_input.isdigit():
    print("Please enter a valid number.")



















#The not logical operator is a versatile tool in programming that helps invert boolean values and 
#conditions. It is widely used for conditional checks, loop controls, function return value checks, 
#and ensuring certain criteria are not met. By understanding and using the not operator effectively,
