# MeSH Entry Terms String Generator
Recebe um link de uma doença do [MeSH](https://www.ncbi.nlm.nih.gov/mesh/), localiza os Entry Terms e cria uma string para ser utilizada no PubMed, além do link direto para o site.

NOTA: Tambem pode utilizar o nome da doença (em ingles) ao inves do link direto.

Exemplo:
      
      input: 
      https://www.ncbi.nlm.nih.gov/mesh/68000544 

      output: 
      [+] ("Alzheimer Disease" OR "Alzheimer Dementias" OR "Alzheimer Dementia" OR "Alzheimer's Disease" OR "Senile Dementia" OR "AlzheimerType Dementia (ATD)" OR "Alzheimer-Type Dementia (ATD)" OR "Alzheimer Type Dementia (ATD)" OR "AlzheimerType Dementia" OR "Alzheimer Type Dementia" OR "Alzheimer-Type Dementia" OR "Primary Senile Degenerative Dementia" OR "Alzheimer Sclerosis" OR "Alzheimer Syndrome" OR "Alzheimer's Diseases" OR "Alzheimer Diseases" OR "Alzheimers Diseases" OR "Alzheimer Type Senile Dementia" OR "Acute Confusional Senile Dementia" OR "Presenile Dementia" OR "Late Onset Alzheimer Disease" OR "Focal Onset Alzheimer's Disease" OR "Familial Alzheimer Disease (FAD)" OR "Familial Alzheimer Disease" OR "Familial Alzheimer Diseases (FAD)" OR "Early Onset Alzheimer Disease" OR "Presenile Alzheimer Dementia")
      
      [+] https://pubmed.ncbi.nlm.nih.gov/?term=("Alzheimer+Disease"+OR+"Alzheimer+Dementias"+OR+"Alzheimer+Dementia"+OR+"Alzheimer's+Disease"+OR+"Senile+Dementia"+OR+"AlzheimerType+Dementia+(ATD)"+OR+"Alzheimer-Type+Dementia+(ATD)"+OR+"Alzheimer+Type+Dementia+(ATD)"+OR+"AlzheimerType+Dementia"+OR+"Alzheimer+Type+Dementia"+OR+"Alzheimer-Type+Dementia"+OR+"Primary+Senile+Degenerative+Dementia"+OR+"Alzheimer+Sclerosis"+OR+"Alzheimer+Syndrome"+OR+"Alzheimer's+Diseases"+OR+"Alzheimer+Diseases"+OR+"Alzheimers+Diseases"+OR+"Alzheimer+Type+Senile+Dementia"+OR+"Acute+Confusional+Senile+Dementia"+OR+"Presenile+Dementia"+OR+"Late+Onset+Alzheimer+Disease"+OR+"Focal+Onset+Alzheimer's+Disease"+OR+"Familial+Alzheimer+Disease+(FAD)"+OR+"Familial+Alzheimer+Disease"+OR+"Familial+Alzheimer+Diseases+(FAD)"+OR+"Early+Onset+Alzheimer+Disease"+OR+"Presenile+Alzheimer+Dementia")

Ou:
      
      input: 
      alzheimer

      output: 
      [+] ("Alzheimer Disease" OR "Alzheimer Dementias" OR "Alzheimer Dementia" OR "Alzheimer's Disease" OR "Senile Dementia" OR "AlzheimerType Dementia (ATD)" OR "Alzheimer-Type Dementia (ATD)" OR "Alzheimer Type Dementia (ATD)" OR "AlzheimerType Dementia" OR "Alzheimer Type Dementia" OR "Alzheimer-Type Dementia" OR "Primary Senile Degenerative Dementia" OR "Alzheimer Sclerosis" OR "Alzheimer Syndrome" OR "Alzheimer's Diseases" OR "Alzheimer Diseases" OR "Alzheimers Diseases" OR "Alzheimer Type Senile Dementia" OR "Acute Confusional Senile Dementia" OR "Presenile Dementia" OR "Late Onset Alzheimer Disease" OR "Focal Onset Alzheimer's Disease" OR "Familial Alzheimer Disease (FAD)" OR "Familial Alzheimer Disease" OR "Familial Alzheimer Diseases (FAD)" OR "Early Onset Alzheimer Disease" OR "Presenile Alzheimer Dementia")
      
      [+] https://pubmed.ncbi.nlm.nih.gov/?term=("Alzheimer+Disease"+OR+"Alzheimer+Dementias"+OR+"Alzheimer+Dementia"+OR+"Alzheimer's+Disease"+OR+"Senile+Dementia"+OR+"AlzheimerType+Dementia+(ATD)"+OR+"Alzheimer-Type+Dementia+(ATD)"+OR+"Alzheimer+Type+Dementia+(ATD)"+OR+"AlzheimerType+Dementia"+OR+"Alzheimer+Type+Dementia"+OR+"Alzheimer-Type+Dementia"+OR+"Primary+Senile+Degenerative+Dementia"+OR+"Alzheimer+Sclerosis"+OR+"Alzheimer+Syndrome"+OR+"Alzheimer's+Diseases"+OR+"Alzheimer+Diseases"+OR+"Alzheimers+Diseases"+OR+"Alzheimer+Type+Senile+Dementia"+OR+"Acute+Confusional+Senile+Dementia"+OR+"Presenile+Dementia"+OR+"Late+Onset+Alzheimer+Disease"+OR+"Focal+Onset+Alzheimer's+Disease"+OR+"Familial+Alzheimer+Disease+(FAD)"+OR+"Familial+Alzheimer+Disease"+OR+"Familial+Alzheimer+Diseases+(FAD)"+OR+"Early+Onset+Alzheimer+Disease"+OR+"Presenile+Alzheimer+Dementia")
      


## Requisitos
Python3 e [pip](https://pip.pypa.io/en/stable/)

## Instalação

### Windows
Baixe os arquivos pelo [link](https://www.github.com/zecabum/MeSH-Entry-Terms-string-generator/archive/refs/heads/main.zip) e extraia-os numa pasta

Depois disso, abra o CMD e use o comando ```cd``` seguido do caminho até a pasta em que os arquivos foram extraídos.

E finalmente
```bash
pip install -r requirements.txt
```
### Linux
Use ```git clone``` para fazer o download dos arquivos
```bash
git clone https://github.com/zecabum/MeSH-Entry-Terms-String-Generator.git
```
```bash
cd MeSH-Entry-Terms-String-Generator/
```
```bash
pip install -r requirements.txt
```
## Utilizaçao
### Windows
```bash
python main.py
```
### Linux
```bash
python3 main.py
```
![Captura de tela em 2023-09-21 23-50-40](https://github.com/zecabum/MeSH-Entry-Terms-String-Generator/assets/105394456/43c5d2cc-a37f-4385-aed4-e416d26122b1)

## Erros
Durante a execução do script, pode ocorrer um erro de conexão devido à requisição que ele precisa fazer. Caso isso ocorra, apenas execute-o novamente, pois o erro deve sumir automaticamente após 1 ou 2 tentativas a mais.
