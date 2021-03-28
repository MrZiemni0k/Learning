import art
import data
import random
import os
import time
player_score = 0

while True:
 
    os.system('cls')
    print(art.logo)
    print(f"Your score: {player_score}")
    a_choice = data.data[random.randint(0,len(data.data)-1)]
    b_choice = a_choice
    while a_choice == b_choice:
        b_choice = data.data[random.randint(0,len(data.data)-1)]
    print(f"Compare A: {a_choice['name']} / {a_choice['description']}"
                        f" from {a_choice['country']}.")
    print(art.vs)
    print(f"\nCompare B: {b_choice['name']} / {b_choice['description']}"
                        f" from {b_choice['country']}.")
    while True:
        p_choice = input("Who has more followers? Type 'A' or 'B'" ).lower()
        if p_choice[0] in ['a','b']:
            break
        else:
            print("I only accept 'A' or 'B' inputs. Try again")
    
    if p_choice[0] == 'a':
        p_choice = a_choice['follower_count']
        if p_choice > b_choice['follower_count']:
            player_score += 1
            print("You are right!")     
            print(f"{a_choice['name']} has {a_choice['follower_count']}"
                " followers")  
            print(f"{b_choice['name']} has {b_choice['follower_count']}"
                " followers") 
            time.sleep(2)   
        else:
            print("Wrong!")
            print(f"{a_choice['name']} has {a_choice['follower_count']}"
                " followers")  
            print(f"{b_choice['name']} has {b_choice['follower_count']}"
                " followers")  
            break
    else:
        p_choice = b_choice['follower_count']
        if p_choice > a_choice['follower_count']:
            player_score += 1
            print("You are right!")     
            print(f"{a_choice['name']} has {a_choice['follower_count']}"
                " followers")  
            print(f"{b_choice['name']} has {b_choice['follower_count']}"
                " followers")
            time.sleep(2)  
        else:
            print("Wrong!")
            print(f"{a_choice['name']} has {a_choice['follower_count']}"
                " followers")  
            print(f"{b_choice['name']} has {b_choice['follower_count']}"
                " followers")  
            break

print(f"You've got {player_score} answers correct!")        

