import random
import numpy as np

# Função objetivo a ser minimizada
def f(x):
    """
    Função que calcula o valor de f(x) = x^3 - 6x + 14.
    O objetivo do algoritmo genético é encontrar o valor de x que minimiza essa função.
    """
    return x**3 - 6*x + 14

# Função para converter um vetor binário em um número real
def bin_to_real(binary, lower_bound, upper_bound, num_bits):
    """
    Converte um vetor binário para um número real dentro de um intervalo especificado.

    Args:
    binary: Vetor binário representando o número.
    lower_bound: Limite inferior do intervalo.
    upper_bound: Limite superior do intervalo.
    num_bits: Número de bits usados para codificar o número.

    Retorna:
    O número real correspondente ao vetor binário.
    """
    max_int = 2**num_bits - 1  # Valor máximo que pode ser representado com o número de bits
    integer_value = int(''.join(map(str, binary)), 2)  # Converte binário para inteiro
    return lower_bound + (integer_value / max_int) * (upper_bound - lower_bound)  # Mapeia o inteiro para o intervalo real

# Função de aptidão que determina quão "boa" é uma solução
def fitness(individual, lower_bound, upper_bound, num_bits):
    """
    Calcula a aptidão de um indivíduo (quanto menor o valor da função objetivo, melhor).

    Args:
    individual: Vetor binário representando uma solução.
    lower_bound: Limite inferior do intervalo de x.
    upper_bound: Limite superior do intervalo de x.
    num_bits: Número de bits usados para codificar x.

    Retorna:
    Valor da função objetivo f(x) para a solução representada pelo indivíduo.
    """
    x = bin_to_real(individual, lower_bound, upper_bound, num_bits)  # Converte o indivíduo binário para número real
    return f(x)

# Função para inicializar a população aleatoriamente
def init_population(pop_size, num_bits):
    """
    Inicializa uma população de indivíduos aleatórios.

    Args:
    pop_size: Tamanho da população (número de indivíduos).
    num_bits: Número de bits usados para representar cada indivíduo.

    Retorna:
    Lista de indivíduos, onde cada indivíduo é representado por um vetor binário.
    """
    return [np.random.randint(2, size=num_bits).tolist() for _ in range(pop_size)]

# Função de seleção por torneio
def tournament_selection(population, scores, k=3):
    """
    Seleciona um indivíduo da população usando a seleção por torneio.

    Args:
    population: Lista de indivíduos.
    scores: Lista de aptidões correspondentes aos indivíduos.
    k: Número de indivíduos selecionados aleatoriamente para o torneio.

    Retorna:
    O melhor indivíduo dentre os selecionados.
    """
    selected = random.sample(range(len(population)), k)  # Seleciona k indivíduos aleatoriamente
    best = min(selected, key=lambda idx: scores[idx])  # Retorna o indivíduo com a melhor aptidão
    return population[best]

# Função de crossover (1 ou 2 pontos)
def crossover(parent1, parent2, num_crossover_points=1):
    """
    Realiza crossover entre dois pais para gerar dois filhos.

    Args:
    parent1: Primeiro indivíduo (pai).
    parent2: Segundo indivíduo (pai).
    num_crossover_points: Número de pontos de corte para o crossover (1 ou 2).

    Retorna:
    Dois novos indivíduos gerados a partir do crossover.
    """
    if num_crossover_points == 1:
        point = random.randint(1, len(parent1) - 1)  # Ponto de corte para o crossover de 1 ponto
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    elif num_crossover_points == 2:
        point1, point2 = sorted(random.sample(range(1, len(parent1)), 2))  # Dois pontos de corte para o crossover de 2 pontos
        return (parent1[:point1] + parent2[point1:point2] + parent1[point2:],
                parent2[:point1] + parent1[point1:point2] + parent2[point2:])

# Função de mutação
def mutation(individual, mutation_rate):
    """
    Realiza mutação em um indivíduo, invertendo bits aleatoriamente.

    Args:
    individual: Indivíduo representado por um vetor binário.
    mutation_rate: Taxa de mutação (probabilidade de cada bit ser mutado).

    Retorna:
    Indivíduo mutado.
    """
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Inverte o bit
    return individual

# Função de elitismo
def elitism(population, scores, elite_size):
    """
    Implementa o elitismo, preservando os melhores indivíduos.

    Args:
    population: Lista de indivíduos.
    scores: Lista de aptidões correspondentes aos indivíduos.
    elite_size: Quantidade de indivíduos da elite a serem preservados.

    Retorna:
    Lista de indivíduos da elite.
    """
    sorted_pop = sorted(zip(population, scores), key=lambda x: x[1])  # Ordena população pela aptidão (menor valor é melhor)
    return [ind for ind, _ in sorted_pop[:elite_size]]  # Retorna os melhores indivíduos

# Função principal do algoritmo genético
def genetic_algorithm(f, lower_bound, upper_bound, num_bits, pop_size=10, generations=100, 
                      mutation_rate=0.01, num_crossover_points=1, elite_size=1):
    """
    Executa o algoritmo genético para minimizar a função f(x).

    Args:
    f: Função objetivo a ser minimizada.
    lower_bound: Limite inferior do intervalo de x.
    upper_bound: Limite superior do intervalo de x.
    num_bits: Número de bits usados para codificar x.
    pop_size: Tamanho da população.
    generations: Número máximo de gerações.
    mutation_rate: Taxa de mutação.
    num_crossover_points: Número de pontos de corte no crossover.
    elite_size: Quantidade de indivíduos da elite.

    Retorna:
    Melhor valor de x encontrado e o valor correspondente da função f(x).
    """
    # Inicializar a população
    population = init_population(pop_size, num_bits)
    best_solution = None
    
    for gen in range(generations):
        # Avaliar a população
        scores = [fitness(ind, lower_bound, upper_bound, num_bits) for ind in population]
        
        # Elitismo: preserva os melhores indivíduos
        elite = elitism(population, scores, elite_size)
        
        # Gerar nova população
        new_population = elite.copy()
        while len(new_population) < pop_size:
            # Seleção
            parent1 = tournament_selection(population, scores)
            parent2 = tournament_selection(population, scores)
            
            # Crossover
            child1, child2 = crossover(parent1, parent2, num_crossover_points)
            
            # Mutação
            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)
            
            new_population.extend([child1, child2])
        
        # Atualizar população
        population = new_population[:pop_size]
        
        # Atualizar a melhor solução
        best_index = np.argmin(scores)
        best_solution = population[best_index]
        best_fitness = scores[best_index]
        
        print(f"Geração {gen + 1}, Melhor valor: {bin_to_real(best_solution, lower_bound, upper_bound, num_bits)}, Aptidão: {best_fitness}")
    
    # Retornar melhor indivíduo
    return bin_to_real(best_solution, lower_bound, upper_bound, num_bits), best_fitness

# Parâmetros do algoritmo
lower_bound = -10  # Limite inferior de x
upper_bound = 10   # Limite superior de x
num_bits = 16      # Número de bits para codificação binária
pop_size = 10      # Tamanho da população
generations = 100  # Número máximo de gerações
mutation_rate = 0.01  # Taxa de mutação
num_crossover_points = 1  # Número de pontos de corte para crossover
elite_size = 1  # Tamanho da elite

# Executar o algoritmo genético
best_x, best_fitness = genetic_algorithm(f, lower_bound, upper_bound, num_bits, pop_size, generations, mutation_rate, num_crossover_points, elite_size)
print(f"Melhor solução encontrada: x = {best_x}, f(x) = {best_fitness}")
