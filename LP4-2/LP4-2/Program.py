weight = int(input("Enter weight of package in kilograms:"))
length = int(input("Enter length of package in centimeters:"))
width = int(input("Enter width of package in centimeters:"))
height = int(input("Enter height of package in centimeters:"))
cubiccentimeters = length * width * height

if cubiccentimeters > 100000 and weight < 27:
    print("Package is too large")
elif cubiccentimeters > 100000 and weight > 27:
    print("Package is too large and heavy")
elif cubiccentimeters < 100000 and weight > 27:
    print("Package is too heavy")
else:
    print("Package can be shipped :)")
    
input()   