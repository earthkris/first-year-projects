l = {}
while True:
    inputt = input("Input: ")
    if inputt == 'done':
        if not l:
            print("Empty List")
        break
    x,y = inputt.split()
    y = int(y)
    if x in l:
        l[x] += y
    else:
        l[x] = y
print("###Summary###")
for k,v in l.items():
    print("Total Number of %s : %i" %(k,v))