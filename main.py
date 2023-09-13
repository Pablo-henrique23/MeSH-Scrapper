from bs4 import BeautifulSoup
import requests
from funcoes import *

BACKSLASH = "\\" 
req = requests.get(input("URL> ").strip())

titulo = BeautifulSoup(req.content, 'html.parser')
html = str(req.content)[str(req.content).find('Entry Terms'):]
html = html[:html.find('</ul>')]
lista_termos = []

for item in titulo.find_all("h1", class_="title"):
    lista_termos.append(item.string.replace(BACKSLASH, ''))

soup = BeautifulSoup(html, 'html.parser')
for item in soup.find_all('li'):
    lista_termos.append(rf"{item.string.replace(BACKSLASH, '')}")

termos = '('+" OR ".join(formatar(lista_termos))+')'
print(f"\n[+] {termos}")
print(f'\n[+] https://pubmed.ncbi.nlm.nih.gov/?term={termos.replace(" ", "+")}')
