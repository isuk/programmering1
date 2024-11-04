class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    # Using __repr__ to represent the string values of the card objects
    def __repr__(self):
        return f"{self.rank} of {self.suit}"
