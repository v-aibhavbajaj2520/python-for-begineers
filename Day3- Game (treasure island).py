print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to treasure island")
print("Your mission is to find the treasure")
direction=input("In which direction you choose to go forward? Left or Right?\n ")
while direction== "Left":
  print ("You lost the Game as you fell into valley")
  break
if direction=="Right":
  print("Good choice! ")
  print("There's a lake how would you choose to move forward (wait for boat to arrive or swim)?")
  water=input("Wait or Swim? ")
  while water=="Swim":
    print("Oops! You were eaten by crocodiles")
    break
  if water=="Wait":
    print("Good Choice!")
    print("There are three doors; Red,Yellow and Blue")
    entry=input("Which door would you like to enter? Red,Yellow or Blue?\n")
    while entry=="Blue":
      print("Oops you were attacked by beasts.")
      break
    while entry=="Red":
     print("Oops you were burned by fire. Game Over!")
     break
    if entry=="Yellow":
     print("YAY!! YOU WON!!")
    else:
     print("Game Over!")
