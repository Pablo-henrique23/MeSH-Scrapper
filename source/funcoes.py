import requests
import re
from bs4 import BeautifulSoup
import string

BACKSLASH = '\\'
TIMEOUT = 15
COMANDOS_VALIDOS = ['[ti]']

def caracteres_maliciosos(item):
    especiais = string.punctuation.replace('-','').replace('[','').replace(']','')
    for char in especiais:
        if char in item:
            return True
    return False

def link_malicioso(item):
    especiais = string.punctuation.replace('-','').replace('?','').replace('=','').replace('.','').replace('/','').replace(':','')
    for char in especiais:
        if char in item[item.find('/mesh/'):]:
            return True
    return False
        

def acharURLCorreto(entrada:str) -> str: # acha o url caso o usuario digite o nome da doença
    inicio = requests.get(f"https://www.ncbi.nlm.nih.gov/mesh/?term={entrada.strip()}", timeout=TIMEOUT).content # pega o html
    pattern = re.compile(r'\d{8}$') # o codigo numerico de cada link tem exatamente 8 caracteres -> /mesh/XXXXXXXX
    
    if not temTitulo(inicio):
        inicio = str(inicio)[str(inicio).find(r'id="messagearea"'):] # corta uma parte do html
        sopa = BeautifulSoup(inicio, 'html.parser') # prepara a sopa

        codigo = sopa.find('a').get('href') # codigo no formato /mesh/numeros
        codigo = codigo[codigo.find('/mesh/')+6:] # codigo somente numeros
        if not pattern.match(codigo): # nao e os 8 numeros, entao e invalido
            return None
        else:
            return f'https://www.ncbi.nlm.nih.gov/mesh/{codigo}' # retorna apenas o link do primeiro <a achado
    
    else: # se tiver titulo é porque ja caiu na pagina certa
        return f'https://www.ncbi.nlm.nih.gov/mesh/?term={entrada}'


def confere_URL(string:str) -> bool: #https://www.geeksforgeeks.org/python-check-url-string/
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    
    url = re.findall(regex, string.strip())
    if len(url) == 0:
        return False
    return True # Confere se uma dada string e um link e retorna true se sim

def del_rep(lista:list) -> list:
    for palavra in lista:
        c = lista.count(palavra)
        if c>1:
            for x in range(0,c-1):
                lista.remove(palavra)
    return lista

def temTitulo(req:requests.Response) -> bool: # SE TIVER TITULO, JA TA NA PAGINA CERTA. SENAO, TA NA PAGINA DE LINKS DE BUSCA
    html = BeautifulSoup(req, 'html.parser')
    if html.find("h1", class_="title") != None:
        return True
    return False

def linkErrado(url):
    if r"ncbi.nlm.nih.gov/mesh/" in url: # aqui o link é valido, logo, retorna falso
        return False
    return True

def getTitle(html:BeautifulSoup):
    titulo = html.find("h1", class_="title")
    if titulo != None:
        return titulo.string.replace(BACKSLASH, '')
    
def getFinal(lista:list) -> tuple:
    return ' AND '.join(del_rep(lista))
    #f'https://pubmed.ncbi.nlm.nih.gov/?term={finalString.replace(" ","+")}'

def identificarComando(doenca:str) -> str:
    padrao = r'^(\w+)(\[[a-zçA-ZÇ]+\])$' # palavra[comando]
    match = re.search(padrao,doenca) # lista no formato ['doença', 'comando']
    if match != None: # sem essa condição vai dar ruim por causa do match.groups() poder ser None 
        if len(match.groups()) == 2 and match.group(2) in COMANDOS_VALIDOS: # se tiver comando válido
            return match.group(2) # retorna o comando
    return ''

def listaParaStrSemColchete(lista:list=[]) -> str: # Passa uma lista pra str e tira os colchetes das pontas
    return str(lista)[1:-1]
