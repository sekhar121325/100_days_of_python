print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You arrived at cross roads.: LEFT or RIGHT:: ")
if choice1=="LEFT":
    print("You Entered into a Forest.")
    print("Attacked by wild animals")
    print("Game Over!")
elif choice1=="RIGHT":
    print("You`re walking towards the sea")
    choice2=input("You hear a sound. WAIT or MOVE: ")
    if choice2=="WAIT":
        print("Found a hidden path")
        choice3=input("hidden path leads to a river. SWIM or WAIT")
        if choice3=="SWIM":
            print("Attacked by Hydra")
            print("Game Over")
        elif choice3=="WAIT":
            print("Build a Raft")
            print("Raft takes you into the cave")
            choice4=input("TURN BACK or ENTER CAVE")
            if choice4=="TURN BACK":
                print("Lost Forever")
                print("Game Over")
            elif choice4=="ENTER CAVE":
                print("Three Doors appear.")
                choice5=input("Choose any one| RED, BLUE, YELLOW")
                if choice5=="RED":
                    print("Burned By Fire")
                    print("Game Over")
                elif choice5=="YELLOW":
                    print("Eaten by Beasts")
                    print("Game Over")
                elif choice5=="BLUE":
                    print("You`ve entered Tunnel")
                    print("Tunnel splits into two again!")
                    choice6=input("Choose LEFT OR RIGHT")
                    if choice6=="LEFT":
                        print("Ancient lock found")
                        choice7=input("USE KEY or FORCE DOOR")
                        if choice7=="USE KEY":
                            print("Doors Open")
                            choice8=input("Now Choose. TAKE TREASURES or INSPECT ROOM")
                            if choice8=="TAKE TREASURES":
                                print("YOU WIN!!")
                            elif choice8=="INSPECT ROOM":
                                print("You`ve accidentally stepped on the trap")
                            else:
                                print("Game Over")
                        elif choice7=="FORCE DOOR":
                            print("Trap Activates. You`re Dead!")
                            print("Game Over")
                        else:
                            print("Game Over")
                    elif choice6=="RIGHT":
                        print("Fell into Darkness")
                        print("Game Over")
                    else:
                        print("Game Over")

                else:
                    print("Game Over")
        else:
            print("Game Over")
    elif choice2=="MOVE":
        print("Fell into a quicksand")
        print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")


