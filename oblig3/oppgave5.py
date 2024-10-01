
programRunning = True

#Create dictionaries with movie info
inception = {
    "name": "Inception",
    "year": 2010,
    "rating": 8.7
}
insideout = {
    "name": "Inside Out",
    "year": 2015,
    "rating": 8.1
}
conair = {
    "name": "Con Air",
    "year": 1997,
    "rating": 6.9
}

#Put dictionaries in a list
filmCol = [inception, insideout, conair]

#Function to add a movie to the list
def addFilm(list, name, year, rating):
    running = True
    while running:
        newDictionary = name.replace(" ", "")
        newDictionary = {
            "name": name.title(),
            "year": year,
            "rating": rating
        }

        list.append(newDictionary)

        #Check if user wants to add another film    
        uInput = input("Would you like to add another film? y/n")
        if uInput == "n":
            running = False

#Function to print the dictionary content out in a prettier way
def showFilmsInList(dicList):
    print("==========================================")
    for key in dicList:
        mName = key.get("name")
        mYear = key.get("year")
        mRating = key.get("rating")
        print(f"{mName} - {mYear} has a rating of {mRating}")
        print("==========================================")

#Runns program in a while loop as long as the user wants to
while programRunning:
    userAction = int(input("Enter '1' to add movie.'2' to print movies. '3' to exit: "))
    if userAction == 1:
        #Save user input in variables for the function
        nameIn = input("What movie would you like to add?\n")
        nameIn.lower()
        yearIn = int(input("What year was it released?\n"))
        ratingIn = input("What was it's ratings?\n")

        if ratingIn == "":
            ratingIn = 5.0
        
        addFilm(filmCol, nameIn, yearIn, ratingIn)

    elif userAction == 2:
        showFilmsInList(filmCol)
    else:
        programRunning = False
