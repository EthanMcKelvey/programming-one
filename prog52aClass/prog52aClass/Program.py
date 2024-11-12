class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width  = width
    
    def area(self):
        return self.length * self.Width
    
    def perimiter(self):
        return 2 * self.length + 2 * self.width
    
    
length = int(input("Enter length: "))
width  = int(input("Enter width:  "))
r = Rectangle(lenght, width)  
print("Area:", r.area())
print("Perimiter:", r.perimiter())
r.length *= 2
print("Length * 2:", r.length)

input()