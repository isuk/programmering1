
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

        list.append[newDictionary]

    #Check if user wants to add another film    
    uInput = input.lower(("Would you like to add another film? y/n"))
    if uInput == "n":
        running = False
        print(filmCol)

#Save user input in variables for the function
nameIn = input("What movie would you like to add?\n")
nameIn.lower()
yearIn = int(input("What year was it released?\n"))
ratingIn = float(input("What was it's ratings?\n"))

addFilm(filmCol, nameIn, yearIn, ratingIn)