import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

try:
    engine = create_engine("sqlite:///imdb.db", echo=False)

    try:
        df_movies = pd.read_sql("SELECT * FROM movies", con=engine)
        print("\nPrimeiras 5 linhas de movies:")
        print(df_movies.head())
    except SQLAlchemyError as e:
        print(f"Erro ao ler tabela movies: {e}")

    try:
        df_series = pd.read_sql("SELECT * FROM series", con=engine)
        print("\nPrimeiras 5 linhas de series:")
        print(df_series.head())
    except SQLAlchemyError as e:
        print(f"Erro ao ler tabela series: {e}")

except SQLAlchemyError as e:
    print(f"Erro ao conectar ao banco: {e}")