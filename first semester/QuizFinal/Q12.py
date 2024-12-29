print("Welcome to coin deposit machine")
c = 0
l = {1:0,
     2:0,
     5:0,
     10:0}
while True:
    inputt = input("Please insert coin: ")
    if inputt == 'done':
        break
    inputt = int(inputt)
    if inputt in [1,2,5,10]:
        if inputt in l:
            l[inputt] += 1
        else:
            l[inputt] = 1
        print("You inserted %i baht coin" %inputt)
        c += inputt
        print("Current Balance: %i baht"%c)
    else:
        print("Only 1,2,5 and 10 baht coin are allowed")
print("<-----Deposit Summary----->")
print("1 baht coins ->",l[1])
print("2 baht coins ->",l[2])
print("5 baht coins ->",l[5])
print("10 baht coins ->",l[10])
print("Deposit Amount: %i baht" %c)