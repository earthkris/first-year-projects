input = input("Input: ")
list = ""
for number in input:
    if number.isnumeric():
        list+=number
for i in list:
    i = int(i)
    for j in range(1,i+1):
        j = int(j)
        if j%3 == 0:
            print("#" , end ="")
        else: 
            print("*" , end="")
    print()

    
