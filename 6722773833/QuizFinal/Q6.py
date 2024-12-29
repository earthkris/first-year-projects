from operator import itemgetter
import numpy as np
studentDic = {}

def RecordScore():
    while True:
        a = input("Enter student name and score: ")
        x,y = a.split()
        if x == 'done':
            break
        y = int(y)
        if x.isnumeric():
            if len(x) == 4:
                if x in studentDic:
                    print("The ID is already recorded!")
                elif 0 < y < 100:
                    studentDic[x] = y
                else:
                    print("Invalid score!")
            else: print("Invalid ID format!")
        else: print("Invalid ID format!")    
RecordScore()

print("List:")
if len(studentDic) > 0:
    for k,v in sorted(studentDic.items(),key = itemgetter(0),reverse=False):
        print("%s\t%i" %(k,v))
    print("There are %i student(s). The average score is %.2f points."%(len(studentDic), (sum(studentDic.values())/len(studentDic))))
else:
    print("> no score is recorded!")