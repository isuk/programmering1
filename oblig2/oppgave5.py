import random

#i = 0
#while i <= 2:
#    print(random.randrange(0, 60))
#    i +=1

rounds = 0
players = int(input("How many players: "))

while rounds < players:
    print(f"Player {rounds + 1} score: ")
    print(random.randrange(0, 60))
    print(random.randrange(0, 60))
    print(random.randrange(0, 60))
    rounds += 1

exit()
