import argparse
import threading
from source import processador

LIMITE = 20
BACKSLASH = '\\'
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("args",nargs='+',help="Lista de termos a serem buscados.")
    args = parser.parse_args()

    argumentos = args.args

    if len(argumentos) > LIMITE:
        print("[ERROR] Número muito grande de argumentos. Limite = 20.")
        return
    
    threads = []
    results = []
    reps = []

    for j in range(0,len(argumentos)):
        if(argumentos[j].upper()) in reps:
            continue
        thread = threading.Thread(target=lambda arg=argumentos[j]: results.append((processador.use(j,argumentos[j]))))
        thread.start()
        threads.append(thread)

        reps.append(argumentos[j].upper())

    for thread in threads:
        thread.join()
    
    query = ''

    for c in results:
        if c.query == '':
            continue
    
        query += c.query
        
        if c != results[-1]:
            query += ' AND '

    if query == '':
        print("[ERROR] A query não pôde ser gerada.")
        return
    query = query.replace(BACKSLASH,'')
    link = f'https://pubmed.ncbi.nlm.nih.gov/?term={query.replace(" ","+")}'
 
    print(f'\n{query}\n')
    print(f'{link}\n')

if __name__ == "__main__":
    main()
