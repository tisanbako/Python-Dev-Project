# print("Tisan Bako")
# print("o---")
# print(" ||||")
# print("*" * 10)


# number = [5,2,5,2,2,]
# for x_count in number:
#     output = ""
#     for count in range(x_count):
#         #print(type(count))
#         output = output + "x"
#     print(output)

# numberz = [5,2,5,2,2,3]
# unique_number = []
# for unique in numberz:
#     if unique not in unique_number:
#        unique_number.append(unique)
# print(unique_number)    

#Price of a house is $1M
#if buyer has good credit, they need to put down 10%
#otherwise 
#they need to put down 20%
house_price = 1000000
good_credit = input("Do you have good credit? (Y/N) ").upper()
#good_credit = good_credit.upper()


if good_credit == "Y": 
    down_payment = 10 * 1000000 / 100
    print(f"your Ten percent down payment is {down_payment}")

elif good_credit == "N":
    down_payment = 20 * 1000000 / 100
    print(f"your Ten percent down payment is {down_payment}")
else:
    print("You can only choose Y or N ")

