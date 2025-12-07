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

try:
    df_ordenado = df_movies.sort_values(by="rating", ascending=False)
    print("\nFilmes ordenados pela nota:")
    print(df_ordenado)
except Exception as e:
    print(f"Erro ao ordenar filmes: {e}")

try:
    df_maior_9 = df_movies[df_movies["rating"] > 9.0]
    print("\nFilmes com nota maior que 9.0:")
    print(df_maior_9)
except Exception as e:
    print(f"Erro ao filtrar filmes: {e}")

try:
    print("\nTop 5 filmes com avaliação > 9.0:")
    print(df_maior_9.sort_values(by="rating", ascending=False).head(5))
except Exception as e:
    print(f"Erro ao exibir top 5: {e}")

def salvar_arquivo(df, nome_csv, nome_json):
    try:
        df.to_csv(nome_csv, index=False)
        print(f"Arquivo salvo: {nome_csv}")
    except Exception as e:
        print(f"Erro ao salvar CSV {nome_csv}: {e}")

    try:
        df.to_json(nome_json, orient="records", indent=4, force_ascii=False)
        print(f"Arquivo salvo: {nome_json}")
    except Exception as e:
        print(f"Erro ao salvar JSON {nome_json}: {e}")

salvar_arquivo(df_movies, "movies.csv", "movies.json")
salvar_arquivo(df_series, "series.csv", "series.json")