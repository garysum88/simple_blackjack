import random

player_on = True
dealer_on = True

# Creation of deck of card
# - Single deck of 52 cards
# - All cards are inserted in a list
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A','J', 'Q', 'K', 'A','J', 'Q', 'K', 'A']


# Creation of dealer and player hand
# - Both hands are created as an empty list
dealer_hand = []
player_hand = []

# Check if the deck consists of 52 cards
while len(deck) != 52:
    print("Error! Please make sure there are 52 cards in the shoe!")
    exit()

# Welcome message
print(" *****************************************")
print(" * Welcome to the Simple Blackjack Game! *") 
print(" *****************************************\n")
print(f"This game uses a single deck of playing cards consisting of {len(deck)} cards!\n")

# Deal the game
# - This function takes one argument : a list from dealer/player
# - Used Python's random module to draw a card from the 'deck', add the card drawn to the player/dealer's hand and remove the card from the 'deck'
def dealing(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)


# Calculate the total of each hand and return the point
def total(turn):
    point = 0
    ace = 0

    for card in turn:
        # Take the numberic value if the card is between 2 to 10 (A,K,Q,J not included)
        if card in range(2,11):
            point += card
        # Take the value of face card (J,Q,K) as 10
        elif card in ['J','Q','K']:
            point += 10
        # Take the value of Ace (wildcard)
        else:
            # - For each Ace, we put 11 points first and we record the number of Ace received
            point += 11
            ace +=1
            # - If there us any Ace card received in the hand AND the total point exceeded 21, we take out 10 points
        while ace and point > 21:
            point -= 10
            ace -= 1
    return point


# Start of the app
# - we run a for loop twice so that player and dealer can receive two cards
for _ in range(2):
    dealing(dealer_hand)
    dealing(player_hand)

# - while player or dealer are still ON (active)
while player_on or dealer_on:
    print(f"Dealer's up card is {dealer_hand[0]}")
    print(f"You have {player_hand} for a total of {total(player_hand)}")


    if player_on:
        # if player is dealt a Blackjack while the dealer is not, the break clause is triggered immediately
        # - note : Blackjack is a hand of 21 with only initial 2 cards
        if total(player_hand) == 21 and len(player_hand) == 2 and total(dealer_hand) != 21 and len(dealer_hand) ==2:
            break
        else:
        # if player is not dealt a Blackjack, he/she is given a chance to make a decision
            decision = input("1. Hit\n2. Stand \n")

    if total(dealer_hand) >16:
        # dealer should stop drawing new cards if the total point is 17 or above
        dealer_on = False
    else:
        # in other words, dealer should keep drawing cards when the total point is 16 or below
        dealing(dealer_hand)



    if decision == '2':
        # when the player entered '2' in the terminal, we draw no further card (STAY)
        player_on = False
    else:
        # deal one more card to player if he/she chooses to HIT
        if decision == '1':
            dealing(player_hand)
        else:
            # warning message for invalid input
            decision = input("Invalid input. Please only enter 1 or 2. Try again!\n1. Hit\n2. Stand \n")

    
    # No more action if player's non-BJ hand achieved 21 points (max point) or higher (22 or higher, busted)
    if total(player_hand) >= 21:
        break
    # After player decided to make no further action, No more action on dealer if dealer's achieved 21 points (max point) or higher (22 or higher, busted)
    elif total(dealer_hand) >=  21 and player_on == False:
        break


# Determination of the game result
# - Player has a BJ while dealer has 21 points with 3 or more cards). Player won.
if total(player_hand) == 21 and len(player_hand) == 2 and total(dealer_hand) == 21 and len(dealer_hand) != 2:
    print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("You have a Blackjack while Dealer does not. You won!")

# - Dealer has a BJ while player has 21 points with 3 or more cards. Dealer won.
elif total(dealer_hand) == 21 and len(dealer_hand) == 2 and total(player_hand) == 21 and len(player_hand) != 2:
    print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Dealer has a Blackjack while you do not. Dealer won!")

# - Both player and dealer has a BJ hand. It is a stand-off.
elif total(dealer_hand) == 21 and len(dealer_hand) == 2 and total(player_hand) == 21 and len(player_hand) == 2:
    print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Both you and the dealer got a Blackjack. Stand off!")

# - Player exceeded 21 points. Player lost.
elif total(player_hand) > 21:
    print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("You have too many! You busted")

# - Dealer exceeded 21 points while player has a valid hand (not busted). Player won.
elif total(dealer_hand) > 21:
    print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Dealer busted. Winner winner, chicken dinner!")

# - Both dealer and player did not exceed 21. Player's point is closer to 21. Player won.
elif 21 - total(player_hand) < 21 - total(dealer_hand):
    print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("You won!")

# - Both dealer and player did not exceed 21. Dealer's point is closer to 21. Dealer won.
elif 21 - total(player_hand) > 21 - total(dealer_hand):
    print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Dealer won!")

# - Both dealer and player got the same point (not two BJ hands). It is a stand-off
else :
    print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("It is a tie!")

# Ending message
print(f"\nGame finished. Card remaining :  {len(deck)}\n")
