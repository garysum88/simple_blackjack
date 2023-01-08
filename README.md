# Simple Blackjack Game in Python
This simple Blackjack game was created using Python. This game stimulates a typical Blackjack hand against dealer's hand based on the assumptions of rules listed below.

## Assumptions of Blackjack rules
- The goal of the game is to get a hand of cards that’s worth as close to 21 points as possible.

- This game use a single deck of 52 cards:
    -	Number cards are worth their face value (2-10) 
    -	Jacks, queens, and kings are worth 10 each
    -	Aces are worth either 1 or 11 (player chooses if the total point does not exceed 21)
    -	The suit of the card does not matter.
    
- The player is initially dealt two cards.

- The dealer is initially dealt two cards. Only one card will be shown to player before the player has finished making decision.

- The player may then choose to ‘hit’ (draw a card) or ‘stand’ (stop drawing cards.) If they ‘hit’, then the new card’s value is added to the hand total. If this total exceeds 21, the player is ‘bust’, and loses. 

- If the player’s hand goes over 21 points, they have lost even the dealer bust afterwards. 

- Once the player has finished the decision-making process, the dealer will reveal the 2nd card.

- The dealer needs to draw another card if he/she has a total point below 17 and will not draw another card if he/she has a total point of 17 or above.

- If the dealer goes over 21 points, the player wins.

- If both player and dealer has a non-busted hand, the hand which is closer to 21 wins. 

- If both player and dealer has the same total point, it is a stand-off (tie).

- Two-cards hand with a total value of 21 points is a Blackjack. It beats all other non-blackjack hands (3 cards or more) with a total value of 21. If both player and dealer has a Blackjack, it is a tie.
    - e.g. Player (A,K) vs Dealer (10,4,7) => Player wins
    - e.g. Player (A,K) vs Dealer (A,10) => Tie
    - e.g. Player (10,2,9) vs Dealer (A,Q) => Dealer wins