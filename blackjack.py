global totalplayer
global endgame 
endgame = False
playerbust = False
dealerbust = False
cpu1bust = False
totalplayer = 0
totaldealer = 0
totalcpu1 = 0
import random

play = input("Welcome to Blackjack! Do you want to play?: ")
if play == "Y" or play == "Yes" or play == "yes" or play == "y":
    while True:
        def hit():
            return random.randint(1, 10)
            return hit()

        def dealerscore():
            global totaldealer
            while totaldealer < 17:
                print("-DEALER HITS-")
                nextdeal = hit()
                if nextdeal == 1:
                    print("Dealer got an ACE")
                elif nextdeal == 10:
                    randchoice = random.randint(0,2)
                    if randchoice == 0:
                        print("Dealers card is a JACK")
                    elif randchoice == 1:
                        print("Dealers card is a QUEEN")
                    elif randchoice == 2:
                        print("Dealers card is a KING")
                else:
                    print("Dealers card is a",nextdeal,)
                totaldealer = totaldealer + nextdeal

        def cpu1score():
            global totalcpu1
            while totalcpu1 < 16:
                print("-CPU HITS-")
                nextdeal = hit()
                if nextdeal == 1:
                    print("CPU got an ACE")
                elif nextdeal == 10:
                    randchoice = random.randint(0,2)
                    if randchoice == 0:
                        print("CPU's card is a JACK")
                    elif randchoice == 1:
                        print("CPU's card is a QUEEN")
                    elif randchoice == 2:
                        print("CPU's card is a KING")
                else:
                    print("CPU's card is a",nextdeal,)
                totalcpu1 = totalcpu1 + nextdeal
            
        def playerscore():
            global totalplayer
            nextdeal = hit()
            if nextdeal == 1:
                print("Your next card is an ACE")
            elif nextdeal == 10:
                randchoice = random.randint(0,2)
                if randchoice == 0:
                    print("Your next card is a JACK")
                elif randchoice == 1:
                    print("Your next card is a QUEEN")
                elif randchoice == 2:
                    print("Your next card is a KING")
            else:
                print("Your next card is a",nextdeal,)
            totalplayer = totalplayer + nextdeal

        def playerscoredisplay():
            print("Your total is",totalplayer,)

        def dealerscoredisplay():
            print("Dealer total is",totaldealer,)
        
        def cpu1scoredisplay():
            print("CPU total is",totalcpu1,)

        def checkblackjack():
            if totalplayer == 21:
                print("------BLACKJACK-------")

            elif totalcpu1 == 21:
                print("CPU BLACKJACKED!!!")
            
            elif totaldealer == 21:
                print("Dealer BLACKJACKED")
                
        def checkwin():            
            if totaldealer < 22 and totaldealer > totalplayer and totaldealer > totalcpu1:
                print("DEALER W-O-N")
            elif totalcpu1 < 22 and totalcpu1 > totalplayer and totalcpu1 > totaldealer:
                print("CPU WINS!!!")
            elif totalplayer < 22 and totalplayer > totaldealer and totalplayer > totalcpu1:
                print("YOU WIN (YIPEEE)")
            elif totalplayer < 22 and totaldealer < 22 and totalcpu1 < 22 and totalplayer == totaldealer or totalcpu1 == totaldealer:
                print("DEALER WINS")
            elif totalplayer == totalcpu1 and totaldealer < totalplayer:
                print("SPLIT POT!!!")

        def checkbust():
            if totaldealer > 21:
                print("Dealer B-U-S-T-E-D!")
                global dealerbust
                dealerbust == True
                
            if totalcpu1 > 21:
                print("CPU BUSTED!")
                global cpu1bust
                cpu1bust == True
                
            if totalplayer > 21:
                print("You BUSTED!(TARNATION)")
                global playerbust
                playerbust == True

        def starting_deal():
            global totaldealer
            global totalplayer
            global totalcpu1
            totaldealer = hit() + hit()
            totalplayer = hit() + hit()
            totalcpu1 = hit() + hit()
            print("Your first deal: ",totalplayer)

        def aftergame():
            global endgame
            cpu1scoredisplay()
            dealerscoredisplay()
            playerscoredisplay()
            again = input("Do you want to play again?: ")
            if again == "Y" or again == "yes" or again == "Yes":
                endgame == False
            else:
                exit()

        while endgame == False:
            totalplayer = 0
            totaldealer = 0
            totalcpu1 = 0
            starting_deal()
            while totalplayer < 22:
                choice = input("Hit or Stick?: ")
                if choice == "Hit" or choice == "hit" or choice == "h" or choice == "H":
                    playerscore()
                    playerscoredisplay()
                else:
                    playerscoredisplay()
                    cpu1score()
                    dealerscore()
                    break
                
            checkblackjack()
            checkbust()
            checkwin()
            aftergame()
            break
        
        
        
