# MeSH Scrapper

MeSH Scrapper uma ferramenta de linha de comando (cli) que faz exatamente o que diz: scrapping na base de dados do MeSH. Ele serve para juntar e formatar corretamente sinônimos de termos que podem ser buscados nessa base de dados, a fim de facilitar, melhorar e ampliar a busca por artigos da área da saúde. MeSH Scrapper aceita nomes, códigos númericos e URLs que levam ao que deseja buscar. Também foi feito para reconhecer "comandos avançados" nos termos de busca (disponível apenas em nomes), como "alzheimer[ti]".

## Instalação e utilização

### Pré-requisitos

Para utilizar essa ferramenta, será necessário ter o [Python](https://www.python.org/downloads/) e o [Pip](https://pip.pypa.io/en/stable/installation/) instalados. Normalmente o Pip será automaticamente baixado caso você faça o download do Python usando o site oficial - que está linkado acima.

### Windows

Se você está no Windows, baixe esse repositório e descompacte-o caso esteja compactado. Então, abra o CMD e navegue até o diretório de onde está a ferramenta usando o comando `cd`. Após isso, para usar o MeSH Scrapper, basta digitar

`pip install -r requirements.txt`

`python main.py <sua_busca1> <sua_busca2>`

### Linux

Caso esteja no Linux, abra o terminal e digite

`git clone https://github.com/Pablo-henrique23/MeSH-Scrapper.git`

`cd MeSH-Scrapper`

`pip install requirements.txt`

`python3 main.py <sua_busca1> <sua_busca2> `

Atenção: é possível que os comandos avançados entrem em conflito com o shell usado. Por exemplo, o `zsh` usa colchetes (`[]`) para encontrar padrões nos nomes de diretórios (globbing) e, então, usar esse tipo de comando pode causar problemas. Para resolver isso, apenas escape os colchetes com `\` ou coloque o termo de busca entre aspas.

## Utilização

Os termos a serem buscados podem ou não estar entre aspas. Em alguns casos, pode ser bom usar aspas para evitar problemas, mas normalmente não será necessário. Não coloque mais de um termo no mesmo par de aspas, isso pode causar comportamento indefinido e o resultado da busca é imprevisível. É importante notar que `<sua_buscaX>` pode ir até 20 caso nenhuma alteração seja feita no código fonte. Caracteres especiais não são permitidos pois podem prejudicar o processo de busca. Usar links que levam direto ao que deseja buscar tende a ser mais rápido.

## Exemplo

Input: `python3 main.py alzheimer`

Output: `("Alzheimer Disease" OR "Alzheimer Syndrome" OR "AlzheimerType Dementia (ATD)" OR "Alzheimer-Type Dementia (ATD)" OR "Alzheimer Type Dementia (ATD)" OR "AlzheimerType Dementia" OR "Alzheimer-Type Dementia" OR "Alzheimer's Diseases" OR "Alzheimer Diseases" OR "Alzheimers Diseases" OR "Alzheimer Dementias" OR "Alzheimer Dementia" OR "Alzheimer's Disease" OR "Senile Dementia" OR "Alzheimer Type Dementia" OR "Alzheimer Type Senile Dementia" OR "Alzheimer Sclerosis" OR "Primary Senile Degenerative Dementia" OR "Presenile Dementia" OR "Acute Confusional Senile Dementia" OR "Early Onset Alzheimer Disease" OR "Presenile Alzheimer Dementia" OR "Late Onset Alzheimer Disease" OR "Focal Onset Alzheimer's Disease" OR "Familial Alzheimer Disease (FAD)" OR "Familial Alzheimer Disease" OR "Familial Alzheimer Diseases (FAD)")                                                              https://pubmed.ncbi.nlm.nih.gov/?term=("Alzheimer+Disease"+OR+"Alzheimer+Syndrome"+OR+"AlzheimerType+Dementia+(ATD)"+OR+"Alzheimer-Type+Dementia+(ATD)"+OR+"Alzheimer+Type+Dementia+(ATD)"+OR+"AlzheimerType+Dementia"+OR+"Alzheimer-Type+Dementia"+OR+"Alzheimer's+Diseases"+OR+"Alzheimer+Diseases"+OR+"Alzheimers+Diseases"+OR+"Alzheimer+Dementias"+OR+"Alzheimer+Dementia"+OR+"Alzheimer's+Disease"+OR+"Senile+Dementia"+OR+"Alzheimer+Type+Dementia"+OR+"Alzheimer+Type+Senile+Dementia"+OR+"Alzheimer+Sclerosis"+OR+"Primary+Senile+Degenerative+Dementia"+OR+"Presenile+Dementia"+OR+"Acute+Confusional+Senile+Dementia"+OR+"Early+Onset+Alzheimer+Disease"+OR+"Presenile+Alzheimer+Dementia"+OR+"Late+Onset+Alzheimer+Disease"+OR+"Focal+Onset+Alzheimer's+Disease"+OR+"Familial+Alzheimer+Disease+FAD)"+OR+"Familial+Alzheimer+Disease"+OR+"Familial+Alzheimer+Diseases+(FAD)")`
