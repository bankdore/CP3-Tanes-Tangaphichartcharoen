totalPrice = int(input("total : "))
def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

print("include vat : " , vatCalculate(totalPrice))