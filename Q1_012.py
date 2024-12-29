x = input("Give me a character: ")
y = input("Give me another character: ")
print("Output:")


if x.isalpha() and y.isalpha():
    if x > y:
        for i in range(ord(y), ord(x)+1):
            print(chr(i) , end ="")
    elif x < y :
        for i in range(ord(x), ord(y)+1):
            print(chr(i) , end ="")
    
else:
    print("Output: You need to input two characters.")