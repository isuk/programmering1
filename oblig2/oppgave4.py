bookCollection = ["The Hobbit", "Farmer Giles of Ham", "Lord of the Rings: The Fellowship of the Ring", "Lord of the Rings: The Two Towers",
            "Lord of the Rings: The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf", "The Silmarillion", "Unfinished Tales"]

lotrCollection = []

for i in range(len(bookCollection)):
    if bookCollection[i].startswith("Lord of the Rings:"):
        lotrCollection.append(bookCollection[i])

print(lotrCollection)
