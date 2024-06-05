#this are functions that do something and return a value 

def square(number):
    return number * number 

print(square(3))

#if you remove return and replace with print it will print 9, none when you call it.

#Creating reusable function

#ex1. convert this block of code below to a function 

message = input(">")
words = message.split(" ")
emojis = {
    ":)":"😄",
    ":(":"🙁"
    }

output = " "
for word in words:
    output += emojis.get(word, word) + " "
print(output)

#First we take out the message variable with input as when we are working we might have to get 
#the input from different source including GUI. WE ALSO TAKE AWAY THE PRINT BELOW AS WE DON'T
#KNOW IF WE WILL NEED TO PRINT OR SEND THE VALUR VIA EMAIL. now the function is 

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)":"😄",
        ":(":"🙁"
        }

output = " "
for word in words:
    output += emojis.get(word, word) + " "

#Now to call it, since we creat a variable for input message    
message = input(">")
print(emoji_converter(message))  #we use the message as the argument for the function