class movies:
    def __init__(self, title, year, score):
        self.title = title
        self.year = year
        self.score = score

m1 = movies("inception", 2010, 8.8)
m2 = movies("the martian", 2015, 8.0)
m3 = movies("joker", 2019, 8.4)

print(f"{m1.title} was released in {m1.year} and currently has the score of: {m1.score}")
print(f"{m2.title} was released in {m2.year} and currently has the score of: {m2.score}")
print(f"{m3.title} was released in {m3.year} and currently has the score of: {m3.score}")
