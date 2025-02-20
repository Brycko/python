#Filename: Pythagoras Calculator
#Author: Bryce Wagner
#Date: 11/02/2016
#Description:
import math

while True:
    print("Pythagoras' Calculator")
    print("1 - Find a hypotenuse")
    print("2 - Find another side")
    print("9 - Exit")
    homemenu = int(input("Enter an option: "))
    
    if homemenu == 1:
        sidea = int(input("Enter side a: "))
        sideb = int(input("Enter side b: "))
        hypsq = (sidea**2 + sideb**2)
        hyp = math.sqrt(hypsq)
        print("The Hypotenuse is",hyp)

    
    if homemenu == 2:
        sidea = int(input("Enter side a: "))
        hyp = int(input("Enter Hypotenuse: "))
        sidebsq = hyp**2 - sidea**2
        sideb = math.sqrt(sidebsq)
        print("The side is",sideb,"long")

    if homemenu == 9:
        print("Goodbye")
        break

    elif homemenu < 0 or homemenu > 9 or homemenu > 3 and homemenu < 9:
        print("Error: Invalid Value")

