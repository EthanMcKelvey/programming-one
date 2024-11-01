eggamount = int(input("Enter amount of eggs purchased:"))
dozens = float(eggamount) // 12

totalbill = 1
if float(eggamount) == 0:
    print("Come back when you have some eggs!")
if float(dozens) > 0 and float(dozens) < 4:
    totalbill = float(dozens) * .5
    print("Your total bill is $" + str(totalbill))
elif float(dozens) > 4 and float(dozens) < 6:
    totalbill = float(dozens) * .45
    print("Your total bill is $" + str(totalbill))
elif float(dozens) > 6 and float(dozens) < 11:
    totalbill = float(dozens) * .40
    print("Your total bill is $" + str(totalbill))
elif float(dozens) >= 11:
    totalbill = float(dozens) * .35
    print("Your total bill is $" + str(totalbill))
    
input()   