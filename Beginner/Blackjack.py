import os
import random
import Blackjack_art

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

continue_game = True

print(Blackjack_art.logo)

if input("Would you like to play a game of Blackjack? Type 'y' or 'n':") == "n":
        continue_game = False


def game():

    def calculate_score(deck):
        return sum(deck)

    def add_cards(num, deck):
        while num > 0:
            deck.append(random.choice(cards))
            num -= 1

    def change_ace(deck):
        ace = deck.index(11)
        deck[ace] = 1

    User_deck = []

    Computer_deck = []

    continue_game = True

    while continue_game:
        add_cards(2, User_deck)
        add_cards(1, Computer_deck)

        print(f"Your cards: {User_deck}, current score: {calculate_score(User_deck)}")
        print(f"Computer's first card : {Computer_deck}")

        more_cards = True
            
        while more_cards:   
            if input("Type 'y' to get another card, type 'n' to pass:") == 'y':
                add_cards(1, User_deck)
            else:
                more_cards = False

            if calculate_score(User_deck) == 21:
                more_cards = False

            elif calculate_score(User_deck) > 21 and 11 in User_deck:
                change_ace(User_deck)
            elif calculate_score(User_deck) > 21:
                print(f"Your cards: {User_deck} \n Your score is {calculate_score(User_deck)}! You Bust!")
                if input("Would you like to play again? Type 'y' or 'n':") == 'y':
                    os.system('cls')
                    game()
            print(f"Your cards: {User_deck} \n Current score: {calculate_score(User_deck)}")
        
        add_cards(1, Computer_deck)
        
        while calculate_score(Computer_deck) < calculate_score(User_deck) and calculate_score(Computer_deck) < 21:
            add_cards(1, Computer_deck)
            if calculate_score(Computer_deck) > 21 and 11 in Computer_deck:
                change_ace(Computer_deck)
        
        if calculate_score(Computer_deck) > 21:
            print(f"Dealer Deck: {Computer_deck} Dealer score: {calculate_score(Computer_deck)} \n You Win!")
            if input("Would you like to play again? Type 'y' or 'n':") == 'y':
                    os.system('cls')
                    game()
        elif calculate_score(Computer_deck) == 21 and calculate_score(User_deck) == 21:
            print(f"Dealer Deck: {Computer_deck} Dealer score: {calculate_score(Computer_deck)} \n You Tie!")
            if input("Would you like to play again? Type 'y' or 'n':") == 'y':
                    os.system('cls')
                    game()
        else:
            print(f"Dealer Deck: {Computer_deck} Dealer score: {calculate_score(Computer_deck)} \n You Lose!")
            if input("Would you like to play again? Type 'y' or 'n':") == 'y':
                    os.system('cls')
                    game()

        continue_game = False



while continue_game:
    game()