correct = 1234
count = 0
while count != 3:
    password = int(input("Enter PIN: "))
    if password == correct:
        print("Access granted")
#The PIN code is in an if statement, so if it is incorrect 3 times, it moves down to the else part of the statement at the bottom
        balance = 67.14
        withdrawl = 0
        terminator = 0
#Balance is defined outside the loop. Withdrawl is for the maxiumu withdrawl amount, which is 1000. If terminator is set to 1, the loop will be skipped.
        while terminator == 0:
            while 0 != 1: #My way of doing an infinite loop. Could also use "while true:". 
                print("Welcome to Northern Frock")
                print("1 - Display balance")
                print("2 - Withdraw funds")
                print("3 - Deposit funds")
                print("9 - Return card")
#Prints inital menu
                next = int(input())
#Input. 
                if next == 1:
                    print("Your balance is", balance, ".")
                    print("Maxiumum withdrawl 1000£")
#Displays balance.
                if next == 2:
                        print("How much would you like to withdraw?")
                        print("1 - 10£")
                        print("2 - 20£")
                        print("3 - 40£")
                        print("4 - 60£")
                        print("5 - 80£")
                        print("6 - 100£")
                        print("7 - Other amount")
                        print("9 - Return to main menu")
                        print("0 - Return Card")
#Prints the second menu for withdrawl
                        next2 = 10
                        next2 = int(input())
                        if withdrawl >= 1000: #Checks to make sure if the maxiumum daily withdrawl (1000$) has been reached. If it is more than 1000, it print an error.
                            print("Error. Maximum daily withdrawl reached. ")
                        else: 
                            if next2 == 1:
                                if 10 > balance:
                                    print("You cannot withdraw this amount of money") #Checks to make sure that you are not withdrawing more than you have in your account.
                                else:
                                    print("Money withdrawn") 
                                    print("Your new balance is", balance - 10) 
                                    balance = balance - 10  #Adjusts new balance
                                    withdrawl = withdrawl + 10 #Adds 10 to the withdrawl value, then updates withdrawl value.
                            if next2 == 2:
                                if 20 > balance:
                                    print("You cannot withdraw this amount of money")
                                else:
                                    print("Money withdrawn")
                                    print("Your new balance is", balance - 20)
                                    balance = balance - 20
                                    withdrawl = withdrawl + 20
                            if next2 == 3:
                                if 40 > balance:
                                    print("You cannot withdraw this amount of money")
                                else:
                                    print("Money withdrawn")
                                    print("Your new balance is", balance - 40)
                                    balance = balance - 40
                                    withdrawl = withdrawl + 40
                            if next2 == 4:
                                if 60 > balance:
                                    print("You cannot withdraw this amount of money")
                                else:
                                    print("Money withdrawn")
                                    print("Your new balance is", balance - 60)
                                    balance = balance - 60
                                    withdrawl = withdrawl + 60
                            if next2 == 5:
                                if 80 > balance:
                                    print("You cannot withdraw this amount of money")
                                else:
                                    print("Money withdrawn")
                                    print("Your new balance is", balance - 80)
                                    balance = balance - 80
                                    withdrawl = withdrawl + 80
                            if next2 == 6:
                                if 100 > balance:
                                    print("You cannot withdraw this amount of money")
                                else:
                                    print("Money withdrawn")
                                    print("Your new balance is", balance - 100)
                                    balance = balance - 100
                                    withdrawl = withdrawl + 100
                            if next2 == 7:
                                while 0 != 1: #infinite loop
                                    otheramount = int(input("Enter withdrawl amount: "))
                                    if otheramount > balance or withdrawl > 1000: #Makes sure are not withdrawing more than what's in your balance. Also checks to make sure the maximum withdrawl value is not breached.
                                        print("You cannot withdraw this amount of money")
                                    elif otheramount%10 == 0: #Checks to make sure the value entered is a multiple of 10. 
                                        print("Money withdrawn")
                                        print("Your new balance is", balance - otheramount)
                                        balance = balance - otheramount #Updates balance.
                                        withdrawl = withdrawl + otheramount #Updates withdrawl.
                                        break 
                                    else:
                                        print("Error: Must be a multiple of 10")
                            if next2 == 9:
                                print("Returning to Main Menu") #Breaks loop, therefore retunring to main menu.
                                break
                            if next2 == 0:
                                print("Returning Card. Goodbye") #This sets the value for terminator to 1. If terminator = 1, the loop will be skipped. Affectivly, this stops the customer from returning to the main menu. Then it breaks out of the loop.
                                terminator = 1
                                break
                            if next2 < 1 or next2 > 9: #Makes sure that any other numbers not on the keypad do not produce an error.
                                print("Error")

                next3 = 10
                if next == 3: #prints menu
                    print("1 - Enter deposit")
                    print("9 - Return to Main Menu")
                    print("0 - Return Card")
                    next3 = int(input())#Input amount
                    if next3 == 1:
                        deposit = int(input("Input amount: "))
                        if deposit < 0:
                            print("Error")#Makes sure deposit is not an negative number.
                        else:
                            print("Deposit added.")
                            print("Your balance is now", balance + deposit, ".")
                            balance = balance + deposit #Updates balance.
                    if next3 == 9:
                        print("Returning to Main Menu")#Returns you to main menu
                        break
                    if next3 == 0:
                        print("Returning Card. Goodbye")#Returns you to PIN entry.
                        terminator = 1
                        break
                    if next3 != 1 or next3 != 9 or next3 != 0: #Makes sure that any other values entered will not produce an error.
                        break

                if next > 3 and next < 9 or next < 0 or next > 9: #Makes sure that any other values entered will not produce an error.
                    print("Error")
                    break


                if next == 9:
                    print("Returning Card. Goodbye")#Returns you to PIN entry.
                    terminator = 1
                    break
               


            
    else:
        print("Pin Incorrect")
        count = count + 1
        if count == 3:
            print("PIN Incorrect too many times. Returning card.")
            break #What happens if the PIN is entered incorrectly too many times. This will simply break the code, "Rejecting" the Credit Card.

   
