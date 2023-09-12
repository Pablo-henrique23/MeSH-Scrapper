from bs4 import BeautifulSoup
import requests
from funcoes import *

BACKSLASH = "\\" # constante, nao troque
req = requests.get(input("URL> "))

#req = requests.get('https://www.ncbi.nlm.nih.gov/mesh/68000544')
html = str(req.content)[str(req.content).find('Entry Terms'):]
html = html[:html.find('</ul>')]
soup = BeautifulSoup(html, 'html.parser')
lista_termos = []
for item in soup.find_all('li'):
    lista_termos.append(rf"{item.string.replace(BACKSLASH, '')}")

termos = '('+" OR ".join(formatar(lista_termos))+')'
print(termos)
