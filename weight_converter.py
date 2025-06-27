# weight convertor

weight = int(input("weight : "))
unit = input ("L (bs) or K(g) :")
if unit.upper()== "l":
    convertor = weight * 0.45
    print(f"weight{convertor} in kilos")
else:
    convertor = weight / 0.45
    print(f"weight {convertor} in pounds")
