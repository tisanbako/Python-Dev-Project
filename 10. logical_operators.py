#logical operatin is used where we have multiple conditions
#example lets say we r building am application for processing loans. lets say..
#with logical operators we use 
#"and" operator(where all conditions are true), 
#"or"(atleast one condition is true)
#"not" The not logical operator is used in programming and logic to invert a boolean value. 
#It converts True to False and False to True. This can be useful in various scenarios, such as 
#condition checking, loop control, and ensuring certain conditions are not met. Here are some 
#common use cases and examples

#EXAMPLE 1 (and)

#If an applicant has high income AND good credit
    #Eligible for loan


has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")


##If an applicant has high income or good credit
    #You can get the loan

high_income = True
good_credit = False

if high_income or good_credit:
    print("You can get the loan")


#ex3 . (NOT)    