print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#LEVEL 1
choice1 = input("Go left(l) or right(r)? ").lower()

if choice1[0]=='r':
    print("You fell into a hole\nGame Over")
else:
    print("You are at the river bank. You see a boat.")
    choice = input("Do you swim across(s) or wait(w)? ")
    
    #LEVEL 2
    if choice[0]=='w':
        print("You were attacked by a trout.\nGame Over")
    else: 
        print("You got teleported to a room with 3 doors.")
        print("Which doors will you choose?")
        choice = input("Red(r), Blue(b) or maybe Yellow(y)? ")

        #LEVEL 3
        if choice[0]=='r':
            print("What a shame. You got burned by a fire.\nGame Over")
        elif choice[0]=='b':
            print("What a shame. You got eaten by a monster.\nGame Over")
        elif choice[0]=='y':
            print("Yay! Here is the treasure.\nYou Won")
        else:
            print("God punished you for not choosing any doors.\nGame Over")