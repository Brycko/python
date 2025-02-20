def resetmenu2():
    time1D = 0
    time1H = 0
    time1M = 0
    
def resetmenu3():
    timeDtotal = 0
    timeHtotal = 0
    timeMtotal = 0

def anythingtotime():
    global timeMtotal
    global timeHtotal
    global timeDtotal
    
    while timeMtotal >= 60:
        timeMtotal = timeMtotal - 60
        timeHtotal = timeHtotal +1
            
    while timeHtotal >= 24:
        timeHtotal = timeHtotal - 24
        timeDtotal = timeDtotal + 1
            
    print(timeDtotal,":",timeHtotal,":",timeMtotal)
def input1():
    global time1D 
    global time1H 
    global time1M 
    global time2D 
    global time2H 
    global time2M
    
    time1D = int(input("From your first time, enter the amount of days: "))
    time1H = int(input("From your first time, enter the amount of hours: "))
    time1M = int(input("From your first time, enter the amount of minutes: "))
    time2D = int(input("From your second time, enter the amount of days: "))
    time2H = int(input("From your second time, enter the amount of hours: "))
    time2M = int(input("From your second time, enter the amount of minutes: "))
    
def input2():
    global time1D 
    global time1H 
    global time1M
    
    time1D = int(input("Enter the amount of days: "))
    time1H = int(input("Enter the amount of hours: "))
    time1M = int(input("Enter the amount of minutes: "))

while True:
    print("Time Calculator - Arithmetic Mode")
    print("1 - Add 2 times")
    print("2 - Find the difference between 2 times")
    print("8 - Conversion mode")
    print("9 - Exit")

    menu = int(input("Enter an option: "))

    if menu == 1:
        input1()

        timeDtotal = time1D + time2D
        timeHtotal = time1H + time2H
        timeMtotal = time1M + time2M

        anythingtotime()

        resetmenu2()
        

    if menu == 2:
        input1()

        timeDtotal = time1D - time2D
        timeHtotal = time1H - time2H
        timeMtotal = time1M - time2M

        anythingtotime()

        resetmenu2()

    if menu == 8:
        while True:
            print("Time Calculator - Conversion Mode")
            print("1 - Convert Time to Days")
            print("2 - Convert Time to Hours")
            print("3 - Convert Time to Minutes")
            print("4 - Convert Minutes to Time")
            print("5 - Convert Hours to Time")
            print("6 - Convert Days to Time")
            print("8 - Conversion mode")
            print("9 - Exit")

            menu2 = int(input("Enter an option: "))

            if menu2 == 1:
                input2()
                print("Number of days:",time1D + (time1H/24) + ((time1M/60)/24))
                resetmenu2()
                
            if menu2 == 2:
                input2()
                print("Number of Hours:",(time1D*24) + time1H + (time1M/60))
                resetmenu2()
                
            if menu2 == 3:
                input2()
                print("Number of days:",((time1D*24)*60)+ (time1H*60) + time1M)
                resetmenu2()

            if menu2 == 4:
                timeMtotal = int(input("Enter the amount of minutes: "))
                timeDtotal = 0
                timeHtotal = 0
                
                anythingtotime()
                resetmenu3()
                
            if menu2 == 5:
                timeHtotal = int(input("Enter the amount of hours: "))
                timeDtotal = 0
                timeMtotal = 0
                
                anythingtotime()
                resetmenu3()
                
            if menu2 == 6:
                timeDtotal = int(input("Enter the amount of days: "))
                timeHtotal = 0
                timeMtotal = 0
                
                anythingtotime()
                resetmenu3()
                
            if menu2 == 8:
                print("Returning to main menu...")
                break
            if menu2 == 9:
                quit()
            
        if menu == 9:
            quit()
