N = input("Input : ")

N = int(N)
count = 0
if 1 <= N <= 15:
    for row in range(N):
        for col in range(N):
            if row > col:
                print("0" , end = ("\t"))
            else:
                count +=1
                print("%d" %count , end = ("\t"))
        print()

else:
    print("Invalid input")