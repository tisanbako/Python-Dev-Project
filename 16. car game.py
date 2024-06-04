#we're building a car game that ..

#when you type help it prints a list of botton
   #start - to start the car
   #stop - to stop the car
   #quit - to exit 

#when you type anything else 
    # i don't understand that ...
#when you type start 
    #Car started ... Ready to go!
#when you type stop
    #Car stopped.
#when you type quit the whole program quits.

# command = ""

# while True:    #we can also say while command != "quit"
#     command = input("> ").lower()     #we add .lower()to whatever answer to make whatever input they put to lower case. we could use command.lower() too
#     if command == "help":
#         print("""
# start - to start the car  
# stop - to stop the car
# quit or q - to exit 
#               """)
#     elif command == "start":
#         print("Car started ... Ready to go!")
#     elif command == "stop":
#         print("Car stopped.")
#     elif command == "quit" or command == "q":
#         break    
#     else:
#         print("i don't understand that ...")

#EX.. MAKE THE CODE BETTER.. in the above code, when you press stop twice it will print car stopped twice
#lets elevate the code to say cal ready started or stopped if you press it more than once

#we need to add another variable that will check if the car is started or not, we use boolean
#we create a variable started to check

command = ""
started = False #1. we created a variable to check and set it to false

while True:    
    command = input("> ").lower()     
    if command == "help":
        print("""
start - to start the car  
stop - to stop the car
quit or q - to exit 
              """)
    elif command == "start":
        if started:                 #when it iterate first time its false, to it will set start to true, second time, it will say its atrted
            print("car is already started!")
        else:
            started = True
            print("Car started ... Ready to go!")
    elif command == "stop":
        if not started: 
            print("The car is already stopped! ")    
        else:
            started = False
            print("Car stopped.. ")            
    elif command == "quit" or command == "q":
        break    
    else:
        print("i don't understand that ...")