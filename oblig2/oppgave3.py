bookList = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring", "The Two Towers",
            "The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf"]

reverseBookList = bookList[:]
reverseBookList.reverse()

print("First two books of list: ")
print(bookList[0:2])
print("Last two books of list: ")
print(reverseBookList[0:2])

newBooks = ["The Silmarillion", "Unfinished Tales"]

print("List with two new books: ")
bookList.extend(newBooks)
print(bookList)

print("Lord of the Rings trilogy: ")
for i in range(2, 5):
    print("Lord of the Rings: " + bookList[i])

bookList.sort()
print("List sorted alphabetically: ")
print(bookList)
