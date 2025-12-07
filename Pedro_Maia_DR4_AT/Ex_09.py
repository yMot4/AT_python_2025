import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

try:
    engine = create_engine("sqlite:///imdb.db", echo=False)

    try:
        df_movies = pd.read_sql("SELECT * FROM movies", con=engine)
    except SQLAlchemyError as e:
        print(f"Erro ao ler tabela movies: {e}")
    try:
        df_series = pd.read_sql("SELECT * FROM series", con=engine)
    except SQLAlchemyError as e:
        print(f"Erro ao ler tabela series: {e}")

except SQLAlchemyError as e:
    print(f"Erro ao conectar ao banco: {e}")

def classificar_nota(nota: float) -> str:
    if nota >= 9.0:
        return "Obra-prima"
    elif 8.0 <= nota < 9.0:
        return "Excelente"
    elif 7.0 <= nota < 8.0:
        return "Bom"
    else:
        return "Mediano"

try:
    df_movies["categoria"] = df_movies["rating"].apply(classificar_nota)

    print(df_movies[["title", "rating", "categoria"]].head(10))

except Exception as e:
    print(f"Erro ao categorizar filmes: {e}")