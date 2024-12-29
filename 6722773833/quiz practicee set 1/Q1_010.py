dna_input = input("DNA: ")
base_input = input("base: ")

count = 0
if not dna_input.isnumeric():
    if not base_input.isnumeric():
        for i in dna_input:
            print("c: %s" %i)
            if i == base_input:
                print("True if test")
                count += 1

        print("There are %d times that the base %s occur in this DNA." %(count , base_input))
    else:
        print("This is not DNA String")
else:
    print("This is not DNA String")