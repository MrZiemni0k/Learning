import os
import Art

#HINT: You can call clear() to clear the output in the console.

print(Art.logo)
player_dict = {}

while True:
    
    name_key = input("What's your name? ")
    
    if name_key in player_dict.keys():
        print("Name already taken. Provide different name")
        
    else:
        name_bid = int(input("How much do you want to bid? "))
        
        switch = input("Is there anyone else to bid?\n"
                    "'no' for No\n'yes for Yes\n").lower()
    
        player_dict[name_key] = name_bid
        if switch[0] == 'n':
            highest_value = 0
            won_names = []
            
            for (_name,_bid) in player_dict.items():
                if _bid > highest_value:
                    won_names = [_name]
                    highest_value = _bid
                    
                elif _bid == highest_value:
                    won_names.append(_name)

            os.system('cls')
            print(f'The winner is {won_names} with {highest_value}!')
            break

                
                
                
        else:
            os.system('cls')
        
    

    

