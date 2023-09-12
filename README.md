# MeSH-Entry-Terms-string-generator
Recebe um link de uma doença do MeSH (https://www.ncbi.nlm.nih.gov/mesh/), localiza os entry terms e cria uma string para ser utilizada no PubMed

Exemplo:

      input: 
      https://www.ncbi.nlm.nih.gov/mesh/68003715
      
      output: 
      [+][Entry terms] ("Alzheimer Disease" OR "Alzheimer Dementias" OR "Alzheimer Dementia" OR "Alzheimer's Disease" OR "Senile Dementia" OR "AlzheimerType Dementia (ATD)" OR "Alzheimer-Type Dementia (ATD)" OR "Alzheimer Type Dementia (ATD)" OR "AlzheimerType Dementia" OR "Alzheimer Type Dementia" OR "Alzheimer-Type Dementia" OR "Primary Senile Degenerative Dementia" OR "Alzheimer Sclerosis" OR "Alzheimer Syndrome" OR "Alzheimer's Diseases" OR "Alzheimer Diseases" OR "Alzheimers Diseases" OR "Alzheimer Type Senile Dementia" OR "Acute Confusional Senile Dementia" OR "Presenile Dementia" OR "Late Onset Alzheimer Disease" OR "Focal Onset Alzheimer's Disease" OR "Familial Alzheimer Disease (FAD)" OR "Familial Alzheimer Disease" OR "Familial Alzheimer Diseases (FAD)" OR "Early Onset Alzheimer Disease" OR "Presenile Alzheimer Dementia")
      
      [+][Link]        https://pubmed.ncbi.nlm.nih.gov/?term=("Alzheimer+Disease"+OR+"Alzheimer+Dementias"+OR+"Alzheimer+Dementia"+OR+"Alzheimer's+Disease"+OR+"Senile+Dementia"+OR+"AlzheimerType+Dementia+(ATD)"+OR+"Alzheimer-Type+Dementia+(ATD)"+OR+"Alzheimer+Type+Dementia+(ATD)"+OR+"AlzheimerType+Dementia"+OR+"Alzheimer+Type+Dementia"+OR+"Alzheimer-Type+Dementia"+OR+"Primary+Senile+Degenerative+Dementia"+OR+"Alzheimer+Sclerosis"+OR+"Alzheimer+Syndrome"+OR+"Alzheimer's+Diseases"+OR+"Alzheimer+Diseases"+OR+"Alzheimers+Diseases"+OR+"Alzheimer+Type+Senile+Dementia"+OR+"Acute+Confusional+Senile+Dementia"+OR+"Presenile+Dementia"+OR+"Late+Onset+Alzheimer+Disease"+OR+"Focal+Onset+Alzheimer's+Disease"+OR+"Familial+Alzheimer+Disease+(FAD)"+OR+"Familial+Alzheimer+Disease"+OR+"Familial+Alzheimer+Diseases+(FAD)"+OR+"Early+Onset+Alzheimer+Disease"+OR+"Presenile+Alzheimer+Dementia")

## Instalação

Instale o Python 3 e o [pip](https://pip.pypa.io/en/stable/).

### Windows
Baixe os arquivos pelo link a seguir e extraia-os numa pasta https://www.github.com/zecabum/MeSH-Entry-Terms-string-generator/archive/refs/heads/main.zip

Depois disso, abra o CMD e use o comando ```cd``` seguido do caminho até a pasta em que os arquivos foram extraídos
### Linux
Use ```git clone``` para fazer o download dos arquivos
```
git clone https://github.com/zecabum/MeSH-Entry-Terms-string-generator.git
```
```
cd MeSH-Entry-Terms-string-generator/
```
## Pip
Depois de baixar os arquivos **e entrar na pasta deles no terminal**, use o ```pip``` para instalar os pacotes necessários 
```
pip install -r requirements.txt
```


## Utilização
### Windows
```
python main.py
```
### Linux

```
python3 main.py
```
## Erros
Durante a execução do script, pode ocorrer um erro de conexão devido à requisição que ele precisa fazer. Caso isso ocorra, apenas execute-o novamente, pois o erro deve sumir automaticamente após 1 ou 2 tentativas a mais.
