Algoritmo Genético para Minimização da Função

Requisitos
Para rodar este código, você precisará de:

Python 3.7+

Bibliotecas Python:

numpy

Você pode instalar o NumPy executando:


pip install numpy



Como Rodar o Código

Clone o repositório ou baixe os arquivos do projeto.

Instale as dependências: Execute o seguinte comando no terminal para garantir que a biblioteca necessária esteja instalada:

pip install numpy


Execute o script: No terminal, navegue até o diretório onde o arquivo Python está localizado e execute:

python genetic_algorithm.py
Isso iniciará a execução do algoritmo genético, e você verá a saída com as informações de cada geração no terminal.

Parâmetros Configuráveis
Dentro do arquivo genetic_algorithm.py, você pode ajustar os seguintes parâmetros:

População Inicial: Defina o número de indivíduos na população (pop_size).
Número de Gerações: Quantidade máxima de gerações que o algoritmo deve rodar (generations).
Taxa de Mutação: Probabilidade de mutação de cada bit (mutation_rate).
Crossover: Escolha entre crossover de 1 ponto ou 2 pontos (num_crossover_points).
Tamanho da Elite: Quantidade de indivíduos que serão mantidos na população sem alterações (elite_size).
Precisão: Defina o número de bits para representar o valor de 𝑥 (num_bits).



Exemplo de configuração:

lower_bound = -10
upper_bound = 10
num_bits = 16  # Precisão da codificação binária
pop_size = 10
generations = 100
mutation_rate = 0.01
num_crossover_points = 1
elite_size = 1


Exemplo de Saída
Ao executar o algoritmo, você verá um log das gerações. A cada geração, o melhor valor encontrado será exibido:

Geração 1, Melhor valor: -9.8765, Aptidão: 3.4567
Geração 2, Melhor valor: -8.2345, Aptidão: 1.2345
...
Melhor solução encontrada: x = -1.732, f(x) = 12.000
Estrutura do Projeto
genetic_algorithm.py: Contém a implementação do algoritmo genético.










Problema da Mochila


Pré-requisitos
Antes de rodar o código, certifique-se de que você tenha o seguinte software instalado:

Python 3.x: O código foi escrito e testado usando Python 3. 

Bibliotecas:
numpy (pode ser instalado via pip)

Instalando dependências
Se você não tiver numpy instalado, execute o seguinte comando para instalá-lo:

pip install numpy
Como Rodar o Código
Passos:
Clone ou Baixe o Projeto:

Você pode clonar este repositório ou baixar os arquivos diretamente.

Execute o Código:

Abra o terminal (ou prompt de comando) na pasta onde o arquivo Python está localizado.

Execute o código com o comando:

python nome_do_arquivo.py
Certifique-se de substituir nome_do_arquivo.py pelo nome do arquivo Python que contém o algoritmo genético.

Resultados:

O código exibirá a evolução do algoritmo ao longo das gerações, mostrando o melhor cromossomo em cada geração, seu valor máximo e a média dos pesos dos itens selecionados.
Exemplo de saída:

markdown
Copiar código
Geração 1:
  Valor máximo: 375
  Média dos pesos dos itens: 20.33
  Cromossomo: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
--------------------------------------------------
Geração 2:
  Valor máximo: 400
  Média dos pesos dos itens: 30.00
  Cromossomo: [0, 0, 0, 0, 1, 0, 1, 1, 1, 1]
--------------------------------------------------
Ao final da execução, o algoritmo exibirá a lista dos melhores cromossomos em cada geração, mostrando qual foi o maior valor encontrado sem ultrapassar o limite de peso.

Personalização
Você pode ajustar os seguintes parâmetros para modificar o comportamento do algoritmo:

Lista de Pesos e Valores:

No código, altere a lista pesos_e_valores para modificar os itens e seus respectivos pesos e valores.
pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], ...]
Peso Máximo:

Modifique a variável peso_maximo para alterar a capacidade máxima da mochila.
peso_maximo = 100
Número de Cromossomos:

A variável numero_de_cromossomos define o tamanho da população de soluções. Aumentar este número pode gerar melhores soluções, mas aumenta o tempo de execução.
numero_de_cromossomos = 150
Gerações:

A variável geracoes define o número máximo de gerações que o algoritmo vai executar.
geracoes = 50
Taxa de Mutação:

A taxa de mutação pode ser ajustada alterando a variável taxa_de_mutacao. Por padrão, é 0.01 (1%).
taxa_de_mutacao = 0.01
