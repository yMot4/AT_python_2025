from Ex_02 import filmes
from Ex_05 import Movie
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError

engine = create_engine("sqlite:///imdb.db", echo=False)

Base = declarative_base()

class MovieModel(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Movie(title='{self.title}', year={self.year}, rating={self.rating})>"

class SeriesModel(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique = True)
    year = Column(Integer, nullable=False)
    seasons = Column(Integer, nullable=False)
    episodes = Column(Integer, nullable=False)

    def __repr__(self):
        return (f"<Series(title='{self.title}', year={self.year}, "
                f"seasons={self.seasons}, episodes={self.episodes})>")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

catalog = []
for f in filmes:
    m = Movie(f[0] ,f[1] , f[2])
    catalog.append(m)

for m in catalog:
    mm = MovieModel(
        title = m.title, 
        year = int(m.year),
        rating = float(m.rating.replace(",", "."))
    )
    try:
        session.add(mm)
        session.flush()
    except IntegrityError:
        session.rollback()

series_list = [
    SeriesModel(title="Breaking Bad", year=2000, seasons=5, episodes=62),
    SeriesModel(title="The Office", year=2005, seasons=9, episodes=201),
    SeriesModel(title="Game of Thrones", year=2011, seasons=8, episodes=73),
    SeriesModel(title="Stranger Things", year=2016, seasons=4, episodes=34),
    SeriesModel(title="Sherlock", year=2010, seasons=4, episodes=13),
    SeriesModel(title="The Mandalorian", year=2019, seasons=3, episodes=24),
    SeriesModel(title="The Witcher", year=2019, seasons=3, episodes=24),
    SeriesModel(title="Peaky Blinders", year=2013, seasons=6, episodes=36),
    SeriesModel(title="The Boys", year=2019, seasons=4, episodes=32),
    SeriesModel(title="Dark", year=2017, seasons=3, episodes=26)
]

for s in series_list:
    try:
        session.add(s)
        session.flush()
    except IntegrityError:
        session.rollback()

session.commit()