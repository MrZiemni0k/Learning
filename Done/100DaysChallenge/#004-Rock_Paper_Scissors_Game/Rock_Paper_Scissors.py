import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Asking player for choice
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper\
 or 2 for Scissors. "))

computer_choice = random.randint(0,2)
print(computer_choice)

#Player
if player_choice == 0:
    p_choice = rock
elif player_choice == 1:
    p_choice = paper
else:
    p_choice = scissors
    
#Computer
if computer_choice == 0:
    c_choice = rock
elif computer_choice == 1:
    c_choice = paper
else:
    c_choice = scissors

#Visualisation for choises      
print(f"Player choice:\n{p_choice}\n")
print(f"Computer choice:\n{c_choice}")

#Results
#Draw
if player_choice == computer_choice:
    print("It's a draw.")
#Player Rock:
elif player_choice == 0:
    if computer_choice == 1:
        print("Computer wins")
    else:
        print("Player wins")
#Player Paper:
elif player_choice == 1:
    if computer_choice == 2:
        print("Computer wins")
    else:
        print("Player wins")
#Player Scissors:
else:
    if computer_choice == 2:
        print("Computer wins")
    else:
        print("Player wins")






    
