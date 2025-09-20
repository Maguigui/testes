import bs4 #Importando a biblioteca beautiful soup 4
import requests #Importando a biblioteca request

url = "https://quotes.toscrape.com/" #Grava o site em uma variavel
quotes = requests.get(url) #Importa o código do site
soup = bs4.BeautifulSoup (quotes.text, "html.parser") #Converte o quote em HTML 

frase = soup.find_all("div", class_ = "quote")

for div in frase:
    texto = div.find("span", class_="text")
    print(texto)