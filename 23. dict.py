#used for key value pairs. in dict you cannot have duplicate key
customer = {"Name": "John Smith", "age":30, "is_verified":True}

print(customer["Name"])

#we can add and modify dictionary like this 

customer["birthdate"] = "April 16 1990"
print(customer)

#we can change the value of a key
customer["Name"] = "Tisan Bako"
print(customer)