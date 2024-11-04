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
