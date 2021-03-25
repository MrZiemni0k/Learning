import art
import random
tries = [5,10]
def choose_lvl():
    
    while True:
        
        try:
            lvl = int(input("Choose a difficulty lvl. 0 - Hard, 1 - Normal "))
        except:
            lvl = 2
            print("Wrong input//Please provide a number 0 or 1 ")
        
        if lvl in [0,1]:
            return lvl

def make_guess(goal_number,left_tries):
    
    while True:
        if left_tries == 0:
            print("No avaiable tries left. Game Over!")
            print(f"I was thinking about: {goal_number}")
            _continue = input("Do you want to try one more time? ").lower()
            if _continue[0]=='y':
                break
            else:
                return 'break'
        print(f"You have {left_tries} attemts remaining to guess a number ")
        try:
            player_number = int(input("Make a guess "))
        except:
            player_number = 0
            print("Wrong format! I need a number from 1 to 100.")

        if player_number in range(1,101):
            if player_number == goal_number:
                print("Pin Pon! You guessed correctly! "
                      f"Number was {goal_number}")
                _continue = input("Do you want to try one more time? ").lower()
                if _continue[0]=='y':
                    break
                else:
                    return 'break'
            elif player_number > goal_number:
                print("Too high!")
                left_tries -= 1
            else:
                print("Too low")
                left_tries -= 1
        else:
            print("Wrong format! Choose number from 1 to 100.")


while True:
    print(art.logo)
    print("Welcome to the Guess Number game!!")
    print("I am thinking a number from 1 to 100.")
    thought_number = random.randint(1,100)
    player_tries = tries[choose_lvl()]
    if make_guess(thought_number,player_tries) == 'break':
        break

    
        