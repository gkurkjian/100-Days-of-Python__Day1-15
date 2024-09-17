## this treasure box founded in https://ascii.co.uk/art. If you want to find more of those, just search ASCII
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
''') ### When you insert these characters, type ''' from begin and the end of print() and paste it to ignore the error


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("Left of Right: ").lower() # ignore uppper/lowercase input

if choice1 == "left":
    choice2 = input('You\'ve come to lake. There is an island in the middle of the lake.\n'
                    'Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
    if choice2 == "wait":
        choice3 = input('You arrived at the island unharmed. There is a house with 3 doors.\n'
                        'One red, on yellow and one blue. Which colour do you choose?\n')
        if choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "blue":
            print("You've entered the room of beasts. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!.")
        else:
            print("Wrong input habibi. You had to insert one of the colours above. Game Over.")
    else:
        print("You get attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game Over.")