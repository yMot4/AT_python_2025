from Ex_02 import filmes
class TV:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"

class Movie(TV):
    def __init__(self, title, year, rating):
        super().__init__(title, year)
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}) - Nota: {self.rating}"

class Series(TV):
    def __init__(self, title, year, seasons, episodes):
        super().__init__(title, year)
        self.seasons = seasons
        self.episodes = episodes

    def __str__(self):
        return (f"{self.title} ({self.year}) - Temporadas: {self.seasons}, "
                f"Episódios: {self.episodes}")

catalog = []
for f in filmes:
    m = Movie(f[0] ,f[1] , f[2])
    catalog.append(m)

s1 = Series("Breaking Bad", 2000, 5, 62)
s2 = Series("The Office", 2005, 9, 201)

catalog.append(s1)
catalog.append(s2)

for i in catalog:
    print(i)