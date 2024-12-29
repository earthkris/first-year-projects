h , m , s = input("Input : ").split(":")
h , m , s = int(h) , int(m) , int(s)
if 0 <= h <= 24 and  0 <= m <= 59 and  0 <= s <= 59: 
    total = (h*60*60)+(m*60)+s 
    print ("The number of seconds = %d" % total)

else:
    print("invalid time")