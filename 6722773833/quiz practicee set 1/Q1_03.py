n_customer = float(input("Input (Number of customers):"))
code = input("Input (Discount code):")

if 1 <= n_customer <=3:
    print("%d person x 399.00 baht" % n_customer)
    sub_total = n_customer * 399
    print("A subtotal price is %.2f bath" %sub_total)

if 4 <= n_customer <=6:
    print("%d person x 499.00 baht" % n_customer)
    sub_total = n_customer * 499
    print("A subtotal price is %.2f bath" %sub_total)

if n_customer > 6:
    print("%d person x 599.00 baht" % n_customer)
    sub_total = n_customer * 599
    print("A subtotal price is %.2f bath" %sub_total)

if code == "CASH":
    print("On-top discount 5%")
    total = sub_total - (sub_total * (5/100))
    print("A total price is %.2f baht" % total)
    
if code == "BIRTHDAY":
    print("On-top discount 10%")
    total = sub_total - (sub_total * (10/100))
    print("A total price is %.2f baht" % total)

if code == "COVID":
    print("On-top discount 30%")
    total = sub_total - (sub_total * (30/100))
    print("A total price is %.2f baht" % total)