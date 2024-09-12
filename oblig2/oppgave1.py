
userInput = input("Hva er svaret på det ultimate spørsmålet om livet, universum og alle ting?\n")
userInput = int(userInput)

answerToLife = 42

if userInput == answerToLife:
    print("Det stemmer, meningen med livet er 42!")

elif userInput < 50 and userInput > 30:
    print("Nærme, men feil")

else:
    print("FEIL")
