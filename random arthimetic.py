from random import randint
while True:
    random1 = randint(1, 100)
    random2 = randint(1, 100)
    print(random1+random2)
    print(random1-random2)
    print(random1*random2)
    print(random1/random2)
    choice = input("Would you like to run the program again?: ")
    if choice == "yes" or choice == "y":
        print()
    else:
        break
