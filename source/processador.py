import requests
from .funcoes import *
from .meshClass import *
import re

class Retorno:
    def __init__(self, query:str=''):
        self.query = query


LEFTSPACING = 35 

def use(id:int, pesquisa:str) -> Retorno:
    if confere_URL(pesquisa): # É URL
        if not link_malicioso(pesquisa):

            if not linkErrado(pesquisa): # pegou o link errado
                mesh = Mesh(adv_command='', url=pesquisa)
            else:
                return Retorno()

        else:
            return Retorno()
            
    else:   # é palavra/termo, nao é link
        padrao = re.compile(r'^\d{6,8}$') # confere se o usuario forneceu os 6-8 numeros do codigo do link
        if not caracteres_maliciosos(pesquisa):

            if bool(padrao.match(pesquisa)): # vê se sao 8 numeros

                for c in range(0,10): # tenta 10 vezes, vai que a internet ta com problema
                    try:
                        req = requests.get(f'https://www.ncbi.nlm.nih.gov/mesh/{pesquisa}')

                    except Exception:
                        continue

                    else:
                        if req.status_code == 200:
                            mesh = Mesh(adv_command='', url=f'https://www.ncbi.nlm.nih.gov/mesh/{pesquisa}')                        
                        break

            else: # sem caractere malicioso e nao é numero (8 numeros), logo, é uma palavra
                comando = identificarComando(pesquisa) # NOTA: comandos avançados nao sao suportados em URLs ou codigos numericos
                for c in range(0,10): # tenta achar ate 10 vezes o link certo
                    try:
                        url = acharURLCorreto(pesquisa) # item vai de nome pra URL    
                        if url == None: # se for invalido, ja sai do loop pra nao perder tempo
                            return Retorno()

                    except requests.Timeout: # timeout na request -> tenta de novo
                        continue

                    else: # se der tudo certo no Try
                        if url != None:
                            if linkErrado(url): # nessa condiçao, 1 link foi achado mas ta errado
                                return Retorno()

                            else:
                                mesh = Mesh(adv_command=comando, url=url)
                                break

        else:
            return Retorno()

    meshed = '' # Conterá os Entry Terms com OR entre eles
    for c in range(0,10): # Tenta pegar a info de cada link ate 10 vezes
        try:
            req = requests.get(mesh.url, timeout=TIMEOUT)
        
        except requests.Timeout:
            continue

        else:
            meshed = mesh.gen(req) # Meshed recebe a string (Contendo OR) da funçao .gen()
            break
    
    return Retorno(meshed) 
