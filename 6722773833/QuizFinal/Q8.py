from operator import itemgetter
d = {}
while True:
    inputt = input("Input: ")
    if inputt == 'done':
        break
    if inputt.isnumeric():
        inputt = int(inputt)
        if 0 < inputt < 1001:
            if inputt in d:
                d[inputt] += 1
            else:
                d[inputt] = 1
        else:print("ERROR")
    else:print("ERROR")
print("----SUMMARY----")
for k,v in sorted(d.items(),key = itemgetter(0)):
    print(k,v)