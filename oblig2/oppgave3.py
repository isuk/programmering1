bookCollection = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring", "The Two Towers",
            "The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf"]

reverseBookList = bookCollection[:]
reverseBookList.reverse()

print("First two books of list: ")
print(bookCollection[0:2])
print("Last two books of list: ")
print(reverseBookList[0:2])

newBooks = ["The Silmarillion", "Unfinished Tales"]

print("List with two new books: ")
bookCollection.extend(newBooks)
print(bookCollection)

print("Lord of the Rings trilogy: ")
bookCollection = [book.replace("The Fellowship of the Ring", "Lord of the Rings: The Fellowship of the Ring") for book in bookCollection]
bookCollection = [book.replace("The Two Towers", "Lord of the Rings: The Two Towers") for book in bookCollection]
bookCollection = [book.replace("The Return of the King", "Lord of the Rings: The Return of the King") for book in bookCollection]

#for i in range(2, 5):
#    print("Lord of the Rings: " + bookList[i])

bookCollection.sort()
print("List sorted alphabetically: ")
print(bookCollection)
