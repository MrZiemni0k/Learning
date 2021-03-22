import random
import Art
import Words as w


player_lives = len(Art.stages)-1
chosen_word = random.choice(w.word_list)  
chosen_word_list = ['_' for letter in chosen_word]
store_letters = []

         
while True:
    
    print(Art.logo)
    if '_' not in chosen_word_list:
        print(f"You won! The word was '{chosen_word}'")
        break
    elif player_lives == 0:
        print(f"No more lives avaiable. You lost!")
        print(f"Hidden word was '{chosen_word}'")
        break
        
    
    print(Art.stages[player_lives])
    print(chosen_word_list)
    guess_letter = input("Guess a letter:  ").lower()
    
    
    if guess_letter in chosen_word:
        if guess_letter[0] in store_letters:
            print(f"Letter '{guess_letter}' was already used.")
        else:
            for index_letter in range(len(chosen_word_list)):
                if guess_letter[0] == chosen_word[index_letter]:
                    chosen_word_list[index_letter] = guess_letter

    else:
        if guess_letter[0] in store_letters:
            print(f"Letter '{guess_letter}' was already used.")
        else:
            print(f"No '{guess_letter[0]}' found in hidden word.")
            player_lives -= 1
    
    store_letters.append(guess_letter[0])
    print(f'Used letters:\n{store_letters}')
                
        
    
