lyai = []
while True:
    l = []
    inputt = input("Input: ")
    if inputt == 'end':
        break
    cur,amount = inputt.split()
    amount = float(amount)
    if amount > 1:
        if cur == 'JPY':
            l.append(amount)
            l.append(cur)
            l.append(amount*0.29)
            lyai.append(l)
        elif cur == 'USD':
            l.append(amount)
            l.append(cur)
            l.append(amount*31.99)
            lyai.append(l)
        elif cur == 'EUR':
            l.append(amount)
            l.append(cur)
            l.append(amount*35.62)
            lyai.append(l)
        else:
            print("ERROR")
    else:
        print("ERROR")
for i in lyai:
    print("%.2f %s is %.2f THB" %(i[0],i[1],i[2]))
