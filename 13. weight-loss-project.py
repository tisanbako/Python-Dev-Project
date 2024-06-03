weight = int(input("What is your weight? "))
weight_unit = input("(L)bs or (K)g:")

if weight_unit.upper() == "L":  #we use upper so that any letter case the user use's will conver it to cap L
    convert_kg = weight*0.45
    print(f"your weight is {convert_kg}Kilos")
else:
    convert_kg = weight/0.45
    print(f"your weight is {convert_kg}Pounds")

