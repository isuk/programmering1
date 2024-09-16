import random

rounds = 0
#i = 0
#while i <= 2:
#    print(random.randrange(0, 60))
#    i +=1

players = int(input("How many players: "))

while rounds < players:
    print(f"Player {rounds + 1} score: ")
    print(random.randrange(0, 60))
    print(random.randrange(0, 60))
    print(random.randrange(0, 60))
    rounds += 1

exit()
