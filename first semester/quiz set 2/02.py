age,name = input("Please enter your information: ").split(",")

if age.isnumeric() and name.isalpha():
    print("Your name is %s." %name)
    print("Your age is %s." %age)
else:
    print("Please enter your complete information.")
