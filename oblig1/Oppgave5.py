
pers1 = 5
pers2 = 9
pers3 = 2.5
pers4 = 21
pers5 = 0

#Create list of all people and how many cookies they ate
personList = [pers1, pers2, pers3, pers4, pers5]

#Use python built-in functions to get necessary data from lists
peopleCount = len(personList)
cookieCount = sum(personList)

#Print and calculate the data from the list
print(f"Amount of people: {peopleCount}")
print(f"Amount of cookies: {cookieCount}")
print(f"Median of cookies per person: {int(cookieCount/peopleCount)}")
