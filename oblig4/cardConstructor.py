class card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        
    # Using __str__ to represent the string values of the card objects
    def __str__(self):
        return f"{self.rank} of {self.suit}"
