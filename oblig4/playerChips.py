class playerChips:
    def __init__(self, starterChips: int):
        self.sumChips = starterChips
    
    def betChips(self, amount: int):
        if amount > self.sumChips:
            print("You don't have enough chips to bet that much.")
        else:
            self.sumChips -= amount
            return amount

    def winChips(self, amount: int):
        self.sumChips += amount
        return(f"You won {amount} chips. You now have {self.sumChips} chips.")

    def countChips(self):
        return self.sumChips
