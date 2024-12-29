from operator import itemgetter
programD = {'ce':0,
            'che':0,
            'ec':0,
            'ie':0,
            'me':0}
lyai = []
while True:
    l = []
    inputt = input("Input: ")
    if inputt == "done":
        break
    name,pro,gpa = inputt.split()
    gpa = float(gpa)
    if 0 < gpa < 4.00 and pro in programD:
        programD[pro] += 1
        l.append(name)
        l.append(pro)
        l.append(gpa)
        lyai.append(l) 
    else:
        print("ERROR")    
print("----SUMMARY----")
for k,v in programD.items():
    print("%s = %i" %(k,v)) 
print("----LIST----")
if lyai:
    for names,pros,gpas in sorted(lyai,key = itemgetter(2),reverse = True):
        print(names,pro,gpas)
else:
    print("The list is empty.")