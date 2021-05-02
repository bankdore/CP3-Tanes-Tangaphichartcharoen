usernameInput = input("Username :")
passwordInput = input("Password :")

if usernameInput == "admin" and passwordInput == "1234" :
    print("---Wecome to BShop---")
    print("1.Apple = 30 bath")
    print("2.Banana = 25 bath")
    print("3.Mango = 40 bath")
    userselectedInput = int(input("item : "))
    quantityInput = int(input("Please fill quantity : "))
    if userselectedInput == 1 :
        result = int(30*quantityInput)
        print("Apple" , (quantityInput))
        print ("Total" , (result), "bath")
    elif userselectedInput == 2 :
        result = int(25*quantityInput)
        print("Banana", (quantityInput))
        print("Total" , (result), "bath")
    elif userselectedInput == 3 :
        result = int(40*quantityInput)
        print("Mango", (quantityInput))
        print("Total" , (result), "bath")
else:
    print("Error")