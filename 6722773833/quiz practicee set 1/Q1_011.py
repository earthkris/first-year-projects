a = input("Input: a=? ")
b = input("Input: b=? ")
c = input("Input: c=? ")


if a < b + c and a > b and a > c:
    print("Output: Form a triangle")

elif b < a + c and b > a and b > c:
    print("Output: Form a triangle")

elif c < a + b and c > a and c > b:
    print("Output: Form a triangle")
else:
    print("Output: Can’t form a triangle")