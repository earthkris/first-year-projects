c = 0
l = []
while c < 9:
    inputt = input("Input:")
    if inputt in ['o','x']:
        c += 1
        l.append(inputt)
    else:
        print("Wrong input")
        break
r = 0
for i in l:
    print("|%s" %i,end = "")
    r += 1
    if r == 3:
        print("|")
        print("-------")
        r = 0