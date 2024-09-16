
running = True
backpack = ["old socks", "forgotten toothbrush"]

while running:
    print("Traveler's Guide to Packing!")
    uCommand = input("Would you like to add something to your list? (add), Remove? (remove) or Print the list? (print): ")
    uCommand.lower()
    uCommand.strip()
 
    if uCommand == "add" or "remove":
        uItem = input("What would you like to add / remove from the backpack?")
        uItem.lower()
        uItem.strip()

        if uCommand == "add":
            backpack.append(uItem)

        elif uCommand == "remove":
            backpack.remove(uItem)
    
    elif uCommand == "print":
        print(backpack)
    
    else:
        print("You have entered an invalid answer")

    uTerminate = input("Would you like to exit the program? (y/n)")
    if uTerminate == "y":
        running = False
        break
