import random 

w = input("Rectangle width: ")
h = input("Rectangle height: ")
t = input("Border thickness: ")

w = int(w)
h = int(h)
t = int(t)
pattern = ["#" , "$" , "*"]

for i in range(h):
    for j in range(w):
        if j < t or  j >= w - t or i < t or i >= h -t:
            r = random.choice(pattern)
            print(r, end = " ")
        else:
            print("  " , end ="")
    print()