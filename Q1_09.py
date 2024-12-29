v = input("Enter speed in mph: ")

if v.isnumeric():
    v = int(v)
    if v > 0:
        d = input("Enter distance in miles: ")

        if d.isnumeric():
            d = int(d)
            if d > 0:
                f = input("Enter output format (D or M):")

                h = d/v
                m = h *60

                if f == "D":
                    print("At %df mph, it will take" % v)
                    print("%.2f hours to travel %d miles." %(h , d))

                elif f == "M":
                    h_last = m // 60
                    m = m % 60
                    
                    print("At %d mph, it will take" % v)
                    print("%d hours and %d minutes to travel %d miles." %(h_last , m , d))

                else:
                    print("Invalid input")
            else:
                print("Invalid input")
        else:
            print("Invalid input")
else:
    print("Invalid input")