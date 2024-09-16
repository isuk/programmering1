
running = True
backpack = ["dust", "forgotten toothbrush"]

while running:
    print("Traveler's Guide to Packing!")
    uCommand = input("Would you like to add something to your list? (add), Remove? (remove) or Print the list? (print): ")
    uCommand.lower()
    uCommand.strip()
 
    if uCommand == "add" or "remove":
        uItem = input(print("What would you like to add / remove from the backpack?"))
        uItem.lower()
        uItem.strip()

        if uCommand == "add":
            backpack.append(uItem)
            #break

        elif uCommand == "remove":
            backpack.remove(uItem)
            #break
    
    elif uCommand == "print":
        print(backpack)
        #break
    
    else:
        print("You have entered an invalid answer")

    uTerminate = input(print("Would you like to exit the program? (y/n)"))
    if uTerminate == "y":
        running = False
