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

titulos = soup.select("h3.ipc-title__text")

for t in titulos:
    print(t.get_text(strip = True))

