import cardConstructor as cardCons
from playerChips import playerChips as pChips
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

    # Draw a card, then remove it from the deck
def draw_card(deckToDrawFrom):
    return deckToDrawFrom.pop()

    # Main program
deck = make_deck()
shuffledDeck = shuffle_deck(deck)

    # Set start chips amount and global values
playerChips = pChips(100)
playerHand = []
firstRound = True

print("Black Jack!")

    # Give player choise to bet
uInput = input(f"You currently have {playerChips.countChips()} chips. How many would you like to bet? ")
betAmount = playerChips.betChips(int(uInput))
sumAmount = playerChips.countChips()
print(f"You bet {betAmount} and have now {sumAmount} chips left.")

running = True
while running:
        # Start game
        # Draw two cards on start round
    if firstRound == True:
        for i in range(2):
            playerHand.append(draw_card(shuffledDeck))
        # Draw one card on every other round
    else:
        playerHand.append(draw_card(shuffledDeck))

        # Print player hand
    for card in playerHand:
        print(f"You drew: {card}")

        # Stop dealer from drawing two cards in the start
    firstRound = False


    running = input("Continue? y/n: ")
    if running == "n":
        running = False
