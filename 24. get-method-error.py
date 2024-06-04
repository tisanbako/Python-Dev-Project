customer = {"Name": "John Smith", "age":30, "is_verified":True}

#Lets say we ask for the print the value of a key that doesnt exist eg print(customer["date of birth"])
#it will show error and stop the program. to avoid our program showing error, we can use the 
#get method to remedy it, now it'll show none (which is the absense of a value)  

print(customer.get("color"))
print(customer.get("Name"))
print(customer.get("name"))
print(customer.get("date_of_birth", "1990")) #This will now have a value of 1990 instead of none. as the value is defined in the get method


#EX1 LETS write a program that ask for our phone number, we write it in digit and it translate to words

phone = input("what is your phone number? ")
#Now lets create a variable of dictionary to map numbers to their spellings(words)
digits_mapping = {
    "0":"Zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
output = ""
for character in phone:
    output += digits_mapping.get(character, "!") + " "
print(output)    


#EX2 LETS CREATE A PROGRAM THAT WHEN WE SAY " I AM SAD" it prints i am sad with a sad smilley face
#
message = input(">")
words = message.split(" ")
emojis = {
    ":)":"😄",
    ":(":"🙁"
    }

output = ""
for word in words:
    output += emojis.get(word, word)