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
        return(card)

    # Function for shuffling the deck
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

    # Draw a card, then remove it from the deck
def draw_card(deckToDrawFrom):
    return deckToDrawFrom.pop()


    # Convert face and ace card and then check for bust
def checkForBust(hand):
    handTotal = 0
    aceCount = 0
    for card in hand:
        if card.rank in ["Jack", "Queen", "King"]:
            handTotal += 10
        elif card.rank == "Ace":
            handTotal += 11
            aceCount += 1
        else:
            handTotal += card.rank

        # If you have more than one ace, set the value of it to 1
    for aces in range(aceCount):
        if handTotal > 21:
            handTotal -= 10 
        # Check if you have a bust    
    if handTotal > 21:
        print("Bust!")
        running = False

    # Main program
deck = make_deck()
shuffledDeck = shuffle_deck(deck)

    # Set start chips amount and global values
playerChips = pChips(100)
playerHand = []
dealerHand = []
firstRound = True
gameRound = 0

print("Black Jack!")

    # Give player choise to bet
uInput = input(f"You currently have {playerChips.countChips()} chips. How many would you like to bet? ")
betAmount = playerChips.betChips(int(uInput))
sumAmount = playerChips.countChips()
print(f"You bet {betAmount} and have now {sumAmount} chips left.")
print("")

running = True
while running:
        # Start game
        # Draw two cards on start round
    print(f"Current round: {gameRound}")
    print("")
    if gameRound == 0:
        for i in range(2):
            playerHand.append(draw_card(shuffledDeck))
        # Draw one card on every other round
    else:
        playerHand.append(draw_card(shuffledDeck))

        # Print player hand
    for card in playerHand:
        print(f"You drew: {card}")
        print("------------------------")

    dealerHand.append(draw_card(shuffledDeck))
    for card in dealerHand:
        print("________________________")
        print(f"Dealer drew: {card}")

    checkForBust(playerHand)

    gameRound += 1

    playerHand

    print("")
    running = input("Continue? y/n: ")
    print("")
    if running == "n":
        running = False
