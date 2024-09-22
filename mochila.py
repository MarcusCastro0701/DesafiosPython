import random
import numpy as np

# Dados de entrada (itens com peso e valor)
pesos_e_valores = [
    [2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], 
    [12, 50], [25, 75], [50, 100], [100, 400]
]
peso_maximo = 100  # Limite máximo de peso permitido na mochila
numero_de_cromossomos = 150  # Tamanho da população
geracoes = 100  # Número de gerações
taxa_de_mutacao = 0.01  # Taxa de mutação aplicada aos cromossomos

# Função para calcular o valor total e o peso médio dos itens selecionados em um cromossomo
def calcular_fitness(cromossomo, pesos_e_valores, peso_maximo):
    valor_total = 0
    peso_total = 0
    itens_selecionados = 0
    
    # Soma os pesos e valores dos itens selecionados (genes com valor 1)
    for i, gene in enumerate(cromossomo):
        if gene == 1:
            peso_total += pesos_e_valores[i][0]
            valor_total += pesos_e_valores[i][1]
            itens_selecionados += 1

    # Penaliza o cromossomo se o peso total ultrapassar o limite da mochila
    if peso_total > peso_maximo:
        return 0, 0  # Retorna zero para valor e média de peso como penalidade

    # Calcula a média dos pesos dos itens selecionados
    media_pesos = peso_total / itens_selecionados if itens_selecionados > 0 else 0
    return valor_total, media_pesos

# Função para criar uma população inicial aleatória
def criar_populacao(tamanho, num_itens):
    return [np.random.randint(2, size=num_itens).tolist() for _ in range(tamanho)]

# Função de seleção via roleta, onde cromossomos com maior aptidão têm maior chance de serem escolhidos
def selecao_roleta(populacao, aptidao):
    soma_aptidao = sum(aptidao)
    pick = random.uniform(0, soma_aptidao)
    atual = 0
    for i, valor in enumerate(aptidao):
        atual += valor
        if atual > pick:
            return populacao[i]

# Função de cruzamento que gera dois filhos a partir de dois pais (corte em ponto aleatório)
def cruzamento(pai1, pai2):
    ponto_de_corte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto_de_corte] + pai2[ponto_de_corte:]
    filho2 = pai2[:ponto_de_corte] + pai1[ponto_de_corte:]
    return filho1, filho2

# Função de mutação, que inverte bits aleatórios do cromossomo com base na taxa de mutação
def mutacao(cromossomo, taxa_de_mutacao):
    for i in range(len(cromossomo)):
        if random.random() < taxa_de_mutacao:
            cromossomo[i] = 1 - cromossomo[i]  # Inverte o bit (0 vira 1, 1 vira 0)
    return cromossomo

# Função principal do algoritmo genético
def algoritmo_genetico(pesos_e_valores, peso_maximo, num_cromossomos, geracoes):
    num_itens = len(pesos_e_valores)  # Número de itens disponíveis
    populacao = criar_populacao(num_cromossomos, num_itens)  # Cria a população inicial
    melhor_por_geracao = []  # Lista para armazenar o melhor cromossomo de cada geração

    # Loop principal do algoritmo, que roda por um número pré-determinado de gerações
    for geracao in range(geracoes):
        aptidao = []
        
        # Calcula a aptidão de cada cromossomo na população
        for individuo in populacao:
            valor, media_peso = calcular_fitness(individuo, pesos_e_valores, peso_maximo)
            aptidao.append(valor)

        nova_populacao = []

        # Identifica o melhor indivíduo da geração
        melhor_individuo = populacao[np.argmax(aptidao)]
        melhor_valor, melhor_media_peso = calcular_fitness(melhor_individuo, pesos_e_valores, peso_maximo)
        melhor_por_geracao.append([melhor_valor, melhor_media_peso, melhor_individuo])

        # Gera nova população por cruzamento e mutação
        while len(nova_populacao) < num_cromossomos:
            pai1 = selecao_roleta(populacao, aptidao)
            pai2 = selecao_roleta(populacao, aptidao)
            filho1, filho2 = cruzamento(pai1, pai2)
            nova_populacao.append(mutacao(filho1, taxa_de_mutacao))
            nova_populacao.append(mutacao(filho2, taxa_de_mutacao))

        populacao = nova_populacao  # Atualiza a população para a próxima geração

    # Retorna o melhor cromossomo e sua aptidão ao longo das gerações
    return melhor_por_geracao

# Função para exibir os resultados de cada geração de forma organizada
def exibir_resultados(melhor_por_geracao):
    print("\nResultados do Algoritmo Genético:")
    print("=" * 50)
    for geracao, (valor, media_peso, cromossomo) in enumerate(melhor_por_geracao):
        print(f"Geração {geracao + 1}:")
        print(f"  Valor máximo: {valor}")
        print(f"  Média dos pesos dos itens: {media_peso:.2f}")
        print(f"  Cromossomo: {cromossomo}")
        print("-" * 50)

# Execução do algoritmo genético
melhor_por_geracao = algoritmo_genetico(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes)

# Exibição dos resultados
exibir_resultados(melhor_por_geracao)
