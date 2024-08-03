import re
import requests
from bs4 import BeautifulSoup
from .funcoes import *

# NOTA: a validacao de tentar acessar um link ate 10 vezes nao esta sendo feita nesse arquivo.

BACKSLASH = "\\" 
class Mesh:
    def __init__(self, adv_command, url):
        self.adv_command = adv_command
        self.url = url
        self.titulo = ''
        self.lista_termos = []
        self.termos_formatados = []
        
    
    def start(self, req:requests.Response): # pega os termos do html resposta

        tituloHtml = BeautifulSoup(req.content, 'html.parser')
        titulo = getTitle(tituloHtml)
        self.titulo = titulo

        html = str(req.content)[str(req.content).find('Entry Terms'):]
        html = html[:html.find('</ul>')] # duas linhas so cortando o html pra diminuir -> util caso precise ler o html no console

        self.lista_termos.append(titulo)

        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('li'):
            if item.string != None:
                self.lista_termos.append(rf"{item.string.replace(BACKSLASH, '')}")


    def gen(self,req:requests.Response) -> str:
        self.start(req)
        for palavra in self.lista_termos:
            if palavra != None:
                if ',' in palavra:
                    pre = palavra[:palavra.find(',')].strip()
                    if '(' in palavra:
                        pos = palavra[palavra.find(',')+1:palavra.find('(')]
                    else:
                        pos = palavra[palavra.find(',')+1:]
                    palavra = f'{pos.strip()} {pre}'

                if ' ' in palavra:
                    palavra = palavra.replace(palavra, fr'"{palavra}"')

                if '-' in palavra:
                    self.termos_formatados.append(palavra.replace('-','')+self.adv_command)
                    self.termos_formatados.append(palavra.replace('-',' ')+self.adv_command)
                
                palavra += self.adv_command

                self.termos_formatados.append(palavra)
        return '('+' OR '.join(del_rep(self.termos_formatados))+')'
        

