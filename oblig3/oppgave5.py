
from time import sleep
from random import uniform
import sys

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

#Function to calculate average rating for movies inside list
def ratingAverage(dicList):
    sumRating = 0
    for key in dicList:
        mRating  = key.get("rating")
        sumRating = sumRating + mRating
    print(f"The average rating is: {round(sumRating / len(dicList), 3)}")

#Prints movies released after user specified year
def checkReleaseYear(dicList):
    uYear = int(input("From what year would you like to see the latest released filmes from? "))
    for key in dicList:
        if key.get("year") >= uYear:
            print(key)

#Function that writes out the movies in a file
def writeFile(dicList):
    mFile = open("movies.txt", "w")
    #mFile.write(showFilmsInList(dicList))
    mFile.write("The movies inside the list:\n")

    for key in dicList:
        mName = key.get("name")
        mYear = key.get("year")
        mRating = key.get("rating")
        mFile.write("==========================================\n")
        mFile.write(f"{mName} - {mYear} has a rating of {mRating}\n")

    #print("A file called 'movies.txt has been created in the same directory as this program!' like a type-writer!!!")
    message = "A file called 'movies.txt has been created in the same directory as this program!"
    for c in message:
        print(c, end="")
        sys.stdout.flush()
        sleep(uniform(0.01, 0.06))

    mFile.close()

def readFile():
    mfile = open("movies.txt", "r")
    for line in mfile:
        for c in line:
            print(c, end="")
            sys.stdout.flush()
            sleep(0.01)

#Runns program in a while loop as long as the user wants to
while programRunning:
    userAction = int(input("\n'1' add movie.\n'2' print movies.\n'3' print average rating for all movies.\n'4' find movies released after specified year.\
                            \n'5' write movie list .txt file. \n'6' read content of movie list file. \n'7' exit.\nYour choise: "))
    if userAction == 1:
        #Save user input in variables for the function
        nameIn = input("What movie would you like to add?\n")
        nameIn.lower()
        yearIn = int(input("What year was it released?\n"))
        ratingIn = float(input("What was it's ratings?\n"))

        if ratingIn == "":
            ratingIn = 5.0
        
        addFilm(filmCol, nameIn, yearIn, ratingIn)

    elif userAction == 2:
        showFilmsInList(filmCol)
    elif userAction == 3:
        ratingAverage(filmCol)
    elif userAction == 4:
        checkReleaseYear(filmCol)
    elif userAction == 5:
        writeFile(filmCol)
    elif userAction == 6:
        readFile()
    else:
        programRunning = False
