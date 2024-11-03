class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self) -> str:
        return (f"")

def makeDeck():
    '''
    clubs
    spades
    diamond
    hearts
    '''

clubs = [*range(2, 11, 1)]
spades = []
diamond = []
hearts = []

for rank in clubs:
    card(rank, "clubs")


'use list comprehension'
