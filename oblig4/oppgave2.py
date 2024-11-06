import cardConstructor as cardCons
from playerChips import playerChips as pChips
import random
from colorama import Fore

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
def getHandTotalValue(hand):
    handTotal = 0
    aceCount = 0
    for card in hand:
        if card.rank in ["Jack", "Queen", "King"]:
            handTotal += 10
        elif card.rank == "Ace":
            handTotal += 11
            aceCount += 1
        else:
            handTotal += int(card.rank)

        # If you have more than one ace, set the value of it to 1
    for aces in range(aceCount):
        if handTotal > 21:
            handTotal -= 10 

    return(handTotal)

    # Create deck and shuffle it
deck = make_deck()
shuffledDeck = shuffle_deck(deck)

    # Set start chips amount and global values
playerChips = pChips(100)
playerHand = []
dealerHand = []
gameRound = 1

betValid = True
running = True

print("Let's play Black Jack!")
print("-------------------------")

while running:
        # Give player choise to bet
    if gameRound == 1:
        while betValid:
            betInput = input(f"You currently have {playerChips.countChips()} chips. How many would you like to bet? ")
            betAmount = int(betInput)

                # Check if player has enough chips
            if betAmount > playerChips.countChips():
                print("You don't have that many chips. Try again.")
            else:
                playerChips.betChips(betAmount)
                print(f"You bet {betAmount} and have now {playerChips.countChips()} chips left.")
                print("")
                betValid = False

        # Start game and draw two cards
    print(f"Current round: {gameRound}")
    print("")
    if gameRound == 1:
        for i in range(2):
            playerHand.append(draw_card(shuffledDeck))
        # Draw one card on every other round
    else:
        playerHand.append(draw_card(shuffledDeck))

        # Print player hand
    print("------------------------")
    for card in playerHand:
        print(f"You drew: {card}")

        # The dealer's hand
    if gameRound == 1:
        dealerHand.append(draw_card(shuffledDeck))
    print("------------------------")
    print(f"Dealer drew: {dealerHand[0]}")
    print("------------------------")

        # Check if player got a blackjack
    if getHandTotalValue(playerHand) == 21:
        print("Black Jack! You win!")
        print(playerChips.winChips(betAmount + betAmount * 2))
        playAgain = input("Play another game? y/n")

    gameRound += 1

    # Give the player a choice to hit or stand
    running = input("Hit or stand? h/s: ")
    print("")
    if running == "s":
        print(f"{Fore.GREEN}Your hand total: ", end=" ")
        print(getHandTotalValue(playerHand))
        print("\033[39m")        

            # Check if the dealer has under 14, then draw cards until he does
        while getHandTotalValue(dealerHand) < 17:
            dealerHand.append(draw_card(shuffledDeck))

            # Print dealer's hand
        print("------------------------")
        for card in dealerHand:
            print(f"Dealer drew: {card}")
        
            # Print the dealer's total hand value
        print(f"{Fore.RED}Dealer hand total is: {getHandTotalValue(dealerHand)}")
        print("\033[39m", end="")
        print("------------------------")

            # Check total value of both hands and determine winner
        if getHandTotalValue(playerHand) <= 21 and (getHandTotalValue(playerHand) > getHandTotalValue(dealerHand) or getHandTotalValue(dealerHand) > 21):
            print("You win!")
            print(playerChips.winChips(betAmount * 2))
            playAgain = input("Play another game? y/n")

            # Check if player hand and dealer hand are equal
        elif getHandTotalValue(playerHand) == getHandTotalValue(dealerHand):
            print("It's a Tie! You recieved your bet back.")
            playerChips.winChips(betAmount)
            playAgain = input("Play another game? y/n")

            # If player didn't win, tell them they lost, how much they lost, if they wants to play again
        else:
            print("You lose!")
            print(f"You lost {betAmount} chips.")
            playAgain = input("Play another game? y/n")

            # Check if player wants to play again
        if playAgain == "y":

                # Clear all lists, hands and variables to start a new game
            playerHand.clear()
            dealerHand.clear()
            shuffledDeck.clear()
            deck.clear()

                # Create a new deck and shuffle it, then start a new round
            deck = make_deck()
            shuffledDeck = shuffle_deck(deck)

                #resets round count
            gameRound = 1

            # Close program if player doesn't want to play
        else:
            running = False
