import re, requests
from bs4 import BeautifulSoup

def linha():
    print('-'*60)

def formatar(lista_termos:list) -> list:
    newList = []
    for palavra in lista_termos:
        if ',' in palavra:
            pre = palavra[:palavra.find(',')+1].replace(',','').strip()
            if '(' in palavra:
                pos = palavra[palavra.find(',')+1:palavra.find('(')]
            else:
                pos = palavra[palavra.find(',')+1:]
            palavra = f'{pos.strip()} {pre}'

        if ' ' in palavra:
            palavra = palavra.replace(palavra, fr'"{palavra}"')

        if '-' in palavra:
            newList.append(palavra.replace('-',''))
            newList.append(palavra.replace('-',' '))

        newList.append(palavra)

    return del_rep(newList)

def del_rep(lista:list) -> list:
    for palavra in lista:
        c = lista.count(palavra)
        if c>1:
            for x in range(0,c-1):
                lista.remove(palavra)
    return lista

def identificar_url(string:str) -> bool: #https://www.geeksforgeeks.org/python-check-url-string/
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string.strip())
    if len(url) == 0:
        return False
    return True # Checa se uma dada string e um link e retorna true se sim
    
def acharURLCorreto(entrada:str) -> str:
    inicio = requests.get(f"https://www.ncbi.nlm.nih.gov/mesh/?term={entrada}").content # pega o html
    inicio = str(inicio)[str(inicio).find(r'id="messagearea"'):] # corta uma parte do html
    sopa = BeautifulSoup(inicio, 'html.parser') # prepara a sopa
    return f'https://www.ncbi.nlm.nih.gov{sopa.find("a").get("href")}' # retorna apenas o link do primeiro <a achado

