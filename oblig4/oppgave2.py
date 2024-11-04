'''class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    # Using __repr__ to represent the string values of the card objects
    def __repr__(self):
        return f"{self.rank} of {self.suit}"
   ''' 
import cardConstructor as card
class playerChips:
    def __init__(self, starterChips):
        self.sumChips = starterChips
    
    def betChips(self, amount):
        if amount > self.sumChips:
            print("You don't have enough chips to bet that much.")
        else:
            self.sumChips -= amount
            print(f"You bet {amount} chips. You now have {self.sumChips} chips.")

    def winChips(self, amount):
        self.sumChips += amount
        print(f"You won {amount} chips. You now have {self.sumChips} chips.")

    def countChips(self):
        return self.sumChips

def makeDeck():
    # Define the suits and ranks
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    # Generate the deck using list comprehension
    deck = [card(rank, suit) for suit in suits for rank in ranks]
    return deck

    # Function for printing the deck
def print_deck(deck):
    for card in deck:
        print(card)

print_deck(makeDeck())
