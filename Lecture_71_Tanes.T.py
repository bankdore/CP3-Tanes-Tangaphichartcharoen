menuList = []
priceList = []

def showBill():
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
    totalprice = priceList[0]+priceList[1]+priceList[2]
    print(totalprice)

while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()