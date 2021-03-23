import random
import time
import art

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    return random.choice(cards)

#Game loop
while True:
    print(art.logo)
    player_cards = [deal_card(),deal_card()]
    dealer_cards = [deal_card(),deal_card()]

    player_sum = sum(value for value in player_cards)
    dealer_sum = sum(value for value in dealer_cards)
    print(f"Your cards: {player_cards} ")
    print(f"Dealer's card: {dealer_cards[0]}")
        
    #Player wins with 21.
    if player_sum == 21:
        print("Blackjack! Well done.")
        print(f"Dealer's cards: {dealer_cards}")
        _continue = input("Do you want to go once more? ").lower()
        if _continue != 'y':
            break
    
    else: 
            
        while True:   
            _continue = input("Do you want to draw a card? ").lower()
        
            #Drawing player card
            if _continue[0] == 'y':
                player_cards.append(deal_card())
                player_sum += player_cards[-1]
                print(f"Your cards: {player_cards}")
                print(f"Your sum {player_sum}")
                
                #Check if over
                if player_sum > 21:
                    #Chck for ace
                    if 11 in player_cards:
                        player_sum -= 10
                        player_cards[player_cards.index(11)] = 1
                    else:
                        print("Bust!")

                elif player_sum == 21:
                    print("21! Well done.")
                    print(f"Dealer's cards: {dealer_cards}")
                    _continue = input("Do you want to go once more? ").lower()
                    break
            else:
                print("Player holds")
                print(f"Your cards: {player_cards}")
                print(f"Your sum {player_sum}\n\n")
                print(f"Dealer's cards: {dealer_cards}")
                print(f"Dealer's sum: {dealer_sum}\n\n")
                #2xAces
                if dealer_sum > 21:
                    dealer_sum -= 10
                    dealer_cards[player_cards.index(11)] = 1                                     
                while dealer_sum < 17:
                    dealer_cards.append(deal_card())
                    dealer_sum += dealer_cards[-1]
                    time.sleep(1.5)   
                    print(f"Dealer's cards: {dealer_cards}")
                    print(f"Dealer's sum: {dealer_sum}\n\n")
                    
                    if dealer_sum > 21:
                        if 11 in dealer_cards:
                            dealer_sum -= 10
                            dealer_cards[player_cards.index(11)] = 1  
                        else:
                            print("Dealer busts!") 
                            _continue = input("Do you want to go"
                                              " once more? ").lower()
                            break
                if dealer_sum >= 17 and dealer_sum <= 21:
                    if player_sum > dealer_sum:
                        print("Player wins")
                        _continue = input("Do you want to go"
                                              " once more? ").lower()
                        break
                    elif dealer_sum > player_sum:
                        print("Dealer wins")
                        _continue = input("Do you want to go"
                                              " once more? ").lower()
                        break
                    else:
                        print("Push")
                        _continue = input("Do you want to go"
                                              " once more? ").lower()
                        break
                if dealer_sum > 21:
                    break    
    if _continue != 'y':
        break