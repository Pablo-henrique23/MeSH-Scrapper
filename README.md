# MeSH-Entry-Terms-string-generator
Recebe um link de uma doença do MeSH (https://www.ncbi.nlm.nih.gov/mesh/), localiza os entry terms e cria uma string para ser utilizada no PubMed

Exemplo:

      input: 
      https://www.ncbi.nlm.nih.gov/mesh/68003715
      
      output: 
      ("Alzheimer Dementias" OR "Alzheimer Dementia" OR "Alzheimer's Disease" OR "Senile Dementia" OR "AlzheimerType Dementia (ATD)" OR "Alzheimer-Type Dementia (ATD)" OR "Alzheimer Type Dementia (ATD)" OR "AlzheimerType Dementia" OR "Alzheimer Type Dementia" OR "Alzheimer-Type Dementia" OR "Primary Senile Degenerative Dementia" OR "Alzheimer Sclerosis" OR "Alzheimer Syndrome" OR "Alzheimer's Diseases" OR "Alzheimer Diseases" OR "Alzheimers Diseases" OR "Alzheimer Type Senile Dementia" OR "Acute Confusional Senile Dementia" OR "Presenile Dementia" OR "Late Onset Alzheimer Disease" OR "Focal Onset Alzheimer's Disease" OR "Familial Alzheimer Disease (FAD)" OR "Familial Alzheimer Disease" OR "Familial Alzheimer Diseases (FAD)" OR "Early Onset Alzheimer Disease" OR "Presenile Alzheimer Dementia")

## Instalação
Instale o Python 3 e o [pip](https://pip.pypa.io/en/stable/).
Se possível, use ```git clone``` para fazer o download dos arquivos.
```
git clone https://github.com/zecabum/MeSH-Entry-Terms-string-generator.git
```
```
cd MeSH-Entry-Terms-string-generator/
```
E então
```
pip install -r MeSH-Entry-Terms-string-generator/requirements.txt
```
**Ou, alternativamente, mande o GitHub baixar os arquivos para você.**

## Utilização
### Windows
No cmd, digite
```
python main.py
```
### Linux
No terminal, digite
```
python3 main.py
```
