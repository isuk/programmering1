class movies:
    def __init__(self, title, year, score):
        self.title = title
        self.year = year
        self.score = score
    def __str__(self) -> str:
        return f"{self.title.title()} was released in {self.year} and currently has the score of: {self.score}"

m1 = movies("inception", 2010, 8.8)
m2 = movies("the martian", 2015, 8.0)
m3 = movies("joker", 2019, 8.4)

print(m1)
print(m2)
print(m3)
