import cardConstructor as cardCons
import playerChips as pChips
import random

def make_deck():
    # Define the suits and ranks
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    # Generate the deck using list comprehension
    deck = [cardCons.card(rank, suit) for suit in suits for rank in ranks]
    return deck

    # Function for printing the deck
def print_deck(deck):
    for card in deck:
        print(card)

    # Function for shuffling the deck
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

    # Main program
deck = make_deck()
shuffledDeck = shuffle_deck(deck)

running = True
while running:
    print("Black Jack!")
    playerChips = pChips(100)
    uInput = input(f"You currently have {playerChips.countChips()} chips. How many would you like to bet?")
    # Add logic to handle the user's input
    bet_amount = int(uInput)
    # Rest of the game logic
