import math
area = 0

shape = input("Input a shape T/S/C: ")
l = input("Input a length: ")
if l.isnumeric():
    l =int(l)
if shape == "T" or shape == "S" or shape == "C":
    if l > 0:
        if shape == "T":
            area =(l**2)/4
        elif shape == "S":
            area = (l**2)/2
        elif shape == "C":
            area = math.pi * ((l/2)**2)
        print("The surface area of circle is %.2f" %area)
    else:
        print("Length must be more than or equal to zero.")
else:
    print("Type must be only T/S/C.")