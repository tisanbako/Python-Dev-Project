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

