import requests
from bs4 import BeautifulSoup

URL_TOP250 = "https://www.imdb.com/pt/chart/top/"
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(URL_TOP250, headers = headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

titulos = []
for j in soup.select("h3.ipc-title__text"):
    t = j.get_text(strip = True)
    titulos.append(t)

anos = []
for div in soup.select("div.sc-b4f120f6-6"):
    primeiro_span = div.find("span")
    anos.append(primeiro_span.get_text(strip = True))

notas = []
for i in soup.select("span.ipc-rating-star--rating"):
    n = i.get_text(strip = True)
    notas.append(n)

filmes = [[t, a, n] for t, a, n in zip(titulos, anos, notas)]

for f in filmes:
    print(f"{f[0]} ({f[1]}) - Nota: {f[2]}")


