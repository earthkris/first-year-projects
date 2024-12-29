def PrintTriangle(number,size):
    for i in range(1,size + 1):
        print(" " * (size - i) + (number + " ") * i)
while True:
    num = (input("Enter an integer number (0 to exit): "))
    size = int(num)
    if size == 0:
        print("Exit program. Bye!")
        break
    if size in range(10):
        PrintTriangle(num,size)
    else:
        print("Valid value is between 0 and 9!")
