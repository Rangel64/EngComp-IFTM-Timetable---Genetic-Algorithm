import numpy as np
import random

# Parâmetros do algoritmo genético
populacao_size = 1000
generations = 30000
mutation_rate = 0.01

# Definição das disciplinas por turma e quantidade de aulas
turmas_disciplinas = [
    ["Algoritmos e Programação", "Cálculo Diferencial e Integral I", "Eletricidade Experimental", 
     "Geometria Analítica", "Introdução à Engenharia", "Introdução à Lógica Matemática", 
     "Projeto Interdisciplinar de Engenharia I"],
    ["Álgebra Linear", "Cálculo Diferencial e Integral II", "Circuitos Elétricos I", 
     "Estruturas de Dados", "Física Geral e Experimental I", "Probabilidade e Estatística", 
     "Projeto Interdisciplinar de Engenharia II", "Química Tecnológica"],
    ["Arquitetura e Organização de Computadores", "Cálculo Diferencial e Integral III", "Circuitos Elétricos II", 
     "Desenho Técnico", "Física Geral e Experimental II", "Materiais Elétricos e Dispositivos", 
     "Pesquisa e Ordenação", "Projeto Interdisciplinar de Engenharia III"],
    ["Bancos de Dados", "Cálculo Diferencial e Integral IV", "Eletromagnetismo", "Eletrônica I", 
     "Física Geral e Experimental III", "Programação Orientada a Objetos e Visual", 
     "Projeto Interdisciplinar de Engenharia IV"],
    ["Cálculo Numérico", "Conversão de Energia", "Eletrônica II", "Programação Web I", 
     "Projeto Interdisciplinar de Engenharia V", "Sinais e Sistemas", "Sistemas Digitais", 
     "Sistemas Operacionais"],
    ["Engenharia de Software", "Mecânica dos Materiais", "Microprocessadores e Microcontroladores", 
     "Princípios de Comunicação", "Programação Web II", "Projeto Interdisciplinar de Engenharia VI", 
     "Sistemas de Controle"],
    ["Eletrônica de Potência", "Fenômenos de Transporte", "Instalações Elétricas", 
     "Instrumentação e Controle de Processos", "Metodologia de Trabalho Científico", 
     "Programação para Dispositivos Móveis", "Projeto Interdisciplinar de Engenharia VII", 
     "Redes de Comunicação"],
    ["Controladores Programáveis", "Ética e Legislação", "Linguagens Formais e Autômatos", 
     "Processamento Digital de Imagens", "Projeto Interdisciplinar de Engenharia VIII", 
     "Redes Industriais", "Sistemas Distribuídos e de Tempo Real"],
    ["Ciências do Ambiente", "Compiladores", "Gestão Empresarial e Empreendedorismo", 
     "Inteligência Artificial", "Prática de Pesquisa Orientada", 
     "Projeto de Sistemas de Controle", "Projeto Interdisciplinar de Engenharia IX"]
]
quantidade_de_aulas = {
    "Algoritmos e Programação": 7,
    "Cálculo Diferencial e Integral I": 5,
    "Eletricidade Experimental": 3,
    "Geometria Analítica": 4,
    "Introdução à Engenharia": 2,
    "Introdução à Lógica Matemática": 2,
    "Projeto Interdisciplinar de Engenharia I": 1,
    "Álgebra Linear": 4,
    "Cálculo Diferencial e Integral II": 4,
    "Circuitos Elétricos I": 4,
    "Estruturas de Dados": 5,
    "Física Geral e Experimental I": 4,
    "Probabilidade e Estatística": 4,
    "Projeto Interdisciplinar de Engenharia II": 1,
    "Química Tecnológica": 2,
    "Arquitetura e Organização de Computadores": 4,
    "Cálculo Diferencial e Integral III": 4,
    "Circuitos Elétricos II": 4,
    "Desenho Técnico": 3,
    "Física Geral e Experimental II": 4,
    "Materiais Elétricos e Dispositivos": 2,
    "Pesquisa e Ordenação": 5,
    "Projeto Interdisciplinar de Engenharia III": 1,
    "Bancos de Dados": 7,
    "Cálculo Diferencial e Integral IV": 4,
    "Eletromagnetismo": 2,
    "Eletrônica I": 4,
    "Física Geral e Experimental III": 4,
    "Programação Orientada a Objetos e Visual": 6,
    "Projeto Interdisciplinar de Engenharia IV": 1,
    "Cálculo Numérico": 3,
    "Conversão de Energia": 4,
    "Eletrônica II": 4,
    "Programação Web I": 3,
    "Projeto Interdisciplinar de Engenharia V": 1,
    "Sinais e Sistemas": 5,
    "Sistemas Digitais": 4,
    "Sistemas Operacionais": 4,
    "Engenharia de Software": 4,
    "Mecânica dos Materiais": 2,
    "Microprocessadores e Microcontroladores": 6,
    "Princípios de Comunicação": 4,
    "Programação Web II": 5,
    "Projeto Interdisciplinar de Engenharia VI": 1,
    "Sistemas de Controle": 4,
    "Eletrônica de Potência": 4,
    "Fenômenos de Transporte": 2,
    "Instalações Elétricas": 3,
    "Instrumentação e Controle de Processos": 4,
    "Metodologia de Trabalho Científico": 2,
    "Programação para Dispositivos Móveis": 6,
    "Projeto Interdisciplinar de Engenharia VII": 1,
    "Redes de Comunicação": 4,
    "Controladores Programáveis": 3,
    "Ética e Legislação": 1,
    "Linguagens Formais e Autômatos": 4,
    "Processamento Digital de Imagens": 3,
    "Projeto Interdisciplinar de Engenharia VIII": 1,
    "Redes Industriais": 2,
    "Sistemas Distribuídos e de Tempo Real": 4,
    "Ciências do Ambiente": 1,
    "Compiladores": 4,
    "Gestão Empresarial e Empreendedorismo": 2,
    "Inteligência Artificial": 5,
    "Prática de Pesquisa Orientada": 1,
    "Projeto de Sistemas de Controle": 6,
    "Projeto Interdisciplinar de Engenharia IX": 1,
}


professores = [
    "Prof. A", "Prof. B", "Prof. C", "Prof. D", "Prof. E", 
    "Prof. F", "Prof. G", "Prof. H", "Prof. I", "Prof. J", 
    "Prof. K", "Prof. L", "Prof. M", "Prof. N", "Prof. O", 
    "Prof. P", "Prof. Q", "Prof. R", "Prof. S", "Prof. T", 
    "Prof. U", "Prof. V", "Prof. W", "Prof. X", "Prof. Y"
]

# Vinculação dos professores às disciplinas
professores_disciplinas = {
    "Algoritmos e Programação": "Prof. A",
    "Cálculo Diferencial e Integral I": "Prof. B",
    "Eletricidade Experimental": "Prof. C",
    "Geometria Analítica": "Prof. D",
    "Introdução à Engenharia": "Prof. E",
    "Introdução à Lógica Matemática": "Prof. F",
    "Projeto Interdisciplinar de Engenharia I": "Prof. G",
    "Álgebra Linear": "Prof. H",
    "Cálculo Diferencial e Integral II": "Prof. I",
    "Circuitos Elétricos I": "Prof. J",
    "Estruturas de Dados": "Prof. K",
    "Física Geral e Experimental I": "Prof. L",
    "Probabilidade e Estatística": "Prof. M",
    "Projeto Interdisciplinar de Engenharia II": "Prof. N",
    "Química Tecnológica": "Prof. O",
    "Arquitetura e Organização de Computadores": "Prof. P",
    "Cálculo Diferencial e Integral III": "Prof. Q",
    "Circuitos Elétricos II": "Prof. R",
    "Desenho Técnico": "Prof. S",
    "Física Geral e Experimental II": "Prof. T",
    "Materiais Elétricos e Dispositivos": "Prof. U",
    "Pesquisa e Ordenação": "Prof. V",
    "Projeto Interdisciplinar de Engenharia III": "Prof. W",
    "Bancos de Dados": "Prof. X",
    "Cálculo Diferencial e Integral IV": "Prof. Y",
    "Eletromagnetismo": "Prof. A",
    "Eletrônica I": "Prof. B",
    "Física Geral e Experimental III": "Prof. C",
    "Programação Orientada a Objetos e Visual": "Prof. D",
    "Projeto Interdisciplinar de Engenharia IV": "Prof. E",
    "Cálculo Numérico": "Prof. F",
    "Conversão de Energia": "Prof. G",
    "Eletrônica II": "Prof. H",
    "Programação Web I": "Prof. I",
    "Projeto Interdisciplinar de Engenharia V": "Prof. J",
    "Sinais e Sistemas": "Prof. K",
    "Sistemas Digitais": "Prof. L",
    "Sistemas Operacionais": "Prof. M",
    "Engenharia de Software": "Prof. N",
    "Mecânica dos Materiais": "Prof. O",
    "Microprocessadores e Microcontroladores": "Prof. P",
    "Princípios de Comunicação": "Prof. Q",
    "Programação Web II": "Prof. R",
    "Projeto Interdisciplinar de Engenharia VI": "Prof. S",
    "Sistemas de Controle": "Prof. T",
    "Eletrônica de Potência": "Prof. U",
    "Fenômenos de Transporte": "Prof. V",
    "Instalações Elétricas": "Prof. W",
    "Instrumentação e Controle de Processos": "Prof. X",
    "Metodologia de Trabalho Científico": "Prof. Y",
    "Programação para Dispositivos Móveis": "Prof. A",
    "Projeto Interdisciplinar de Engenharia VII": "Prof. B",
    "Redes de Comunicação": "Prof. C",
    "Controladores Programáveis": "Prof. D",
    "Ética e Legislação": "Prof. E",
    "Linguagens Formais e Autômatos": "Prof. F",
    "Processamento Digital de Imagens": "Prof. G",
    "Projeto Interdisciplinar de Engenharia VIII": "Prof. H",
    "Redes Industriais": "Prof. I",
    "Sistemas Distribuídos e de Tempo Real": "Prof. J",
    "Ciências do Ambiente": "Prof. K",
    "Compiladores": "Prof. L",
    "Gestão Empresarial e Empreendedorismo": "Prof. M",
    "Inteligência Artificial": "Prof. N",
    "Prática de Pesquisa Orientada": "Prof. O",
    "Projeto de Sistemas de Controle": "Prof. P",
    "Projeto Interdisciplinar de Engenharia IX": "Prof. Q"
}


# Função para criar um cromossomo
def create_cromossomo():
    cromossomo = np.zeros((9, 5, 12), dtype=object)
    for turma_index, disciplinas in enumerate(turmas_disciplinas):
        for disciplina in disciplinas:
            aulas_restantes = quantidade_de_aulas[disciplina]
            while aulas_restantes > 0:
                dia = random.randint(0, 4)
                periodo = random.randint(0, 11)
                if cromossomo[turma_index, dia, periodo] == 0:
                    cromossomo[turma_index, dia, periodo] = disciplina
                    aulas_restantes -= 1
    return cromossomo

# def fitness(cromossomo, quantidade_de_aulas):
#     score = 0
#     for turma_index in range(9):
#         aulas_por_disciplina = {disciplina: 0 for disciplina in quantidade_de_aulas.keys()}
#         for dia in range(5):
#             dia_aulas = cromossomo[turma_index, dia, :]
#             disciplinas = [disc for disc in dia_aulas if disc != 0]
#             unique_disciplinas = set(disciplinas)

#             # Bonificar horários agrupados da mesma disciplina
#             for disciplina in unique_disciplinas:
#                 contagem = 0
#                 max_contagem = 0
#                 for aula in dia_aulas:
#                     if aula == disciplina:
#                         contagem += 1
#                     else:
#                         if contagem > max_contagem:
#                             max_contagem = contagem
#                         contagem = 0
#                 if contagem > max_contagem:
#                     max_contagem = contagem
#                 score += max_contagem  # Bonificação por agrupamento

#                 # Atualizar contagem de aulas por disciplina
#                 aulas_por_disciplina[disciplina] += dia_aulas.tolist().count(disciplina)

#             # Penalizar horários vagos entre as aulas
#             aula_encontrada = False
#             for i in range(6):
#                 if dia_aulas[i] != 0:
#                     aula_encontrada = True
#                 elif aula_encontrada and dia_aulas[i] == 0:
#                     if any(dia_aulas[j] != 0 for j in range(i + 1, 6)):
#                         score -= 5  # Penalidade por horário vago entre as aulas

#             # Bonificar aulas de manhã/tarde de acordo com o índice da turma
#             for i in range(6):
#                 if turma_index % 2 == 0:  # Turmas com índice par
#                     if dia_aulas[i] != 0 and i >= 6:
#                         score += 10  # Bonificação para aulas à tarde
#                 else:  # Turmas com índice ímpar
#                     if dia_aulas[i] != 0 and i < 6:
#                         score += 10  # Bonificação para aulas de manhã

#         # Penalizar se o número de aulas de uma disciplina ultrapassar o limite semanal
#         for disciplina, aulas in aulas_por_disciplina.items():
#             if aulas > quantidade_de_aulas[disciplina]:
#                 score -= (aulas - quantidade_de_aulas[disciplina]) * 10  # Penalidade

#     return score

def fitness(cromossomo, quantidade_de_aulas, professores_disciplinas):
    score = 0
    for turma_index in range(9):
        aulas_por_disciplina = {disciplina: 0 for disciplina in quantidade_de_aulas.keys()}
        for dia in range(5):
            dia_aulas = cromossomo[turma_index, dia, :]
            disciplinas = [disc for disc in dia_aulas if disc != 0]
            unique_disciplinas = set(disciplinas)
            
            # Bonificar horários agrupados da mesma disciplina
            for disciplina in unique_disciplinas:
                contagem = 0
                max_contagem = 0
                for aula in dia_aulas:
                    if aula == disciplina:
                        contagem += 1
                    else:
                        if contagem > max_contagem:
                            max_contagem = contagem
                        contagem = 0
                if contagem > max_contagem:
                    max_contagem = contagem
                score += max_contagem  # Bonificação por agrupamento
                
                # Atualizar contagem de aulas por disciplina
                aulas_por_disciplina[disciplina] += dia_aulas.tolist().count(disciplina)

            # Penalizar horários vagos entre as aulas
            aula_encontrada = False
            for i in range(6):
                if dia_aulas[i] != 0:
                    aula_encontrada = True
                elif aula_encontrada and dia_aulas[i] == 0:
                    if any(dia_aulas[j] != 0 for j in range(i + 1, 6)):
                        score -= 20  # Penalidade por horário vago entre as aulas

            # Verificar conflitos de horário dos professores
            for periodo in range(6):
                if dia_aulas[periodo] != 0:
                    professor = professores_disciplinas[dia_aulas[periodo]]
                    for t in range(9):
                        if t != turma_index and cromossomo[t, dia, periodo] != 0:
                            if professores_disciplinas[cromossomo[t, dia, periodo]] == professor:
                                score -= 50  # Penalidade por conflito de horário do professor

            # Bonificar aulas de manhã/tarde de acordo com o índice da turma
            for i in range(6):
                if turma_index % 2 == 0:  # Turmas com índice par
                    if dia_aulas[i] != 0 and i >= 6:
                        score += 10  # Bonificação para aulas à tarde
                else:  # Turmas com índice ímpar
                    if dia_aulas[i] != 0 and i < 6:
                        score += 15  # Bonificação para aulas de manhã
            
            
        # Penalizar se o número de aulas de uma disciplina ultrapassar o limite semanal
        for disciplina, aulas in aulas_por_disciplina.items():
            if aulas > quantidade_de_aulas[disciplina]:
                score -= (aulas - quantidade_de_aulas[disciplina]) * 100  # Penalidade

    return score

# Seleção
# def selecao(populacao):
#     populacao.sort(key=lambda x: x[1], reverse=True)
#     return populacao[:populacao_size]

# Cruzamento
def crossover(cromossomo1, cromossomo2):
    ponto_corte = random.randint(0, cromossomo1.size - 1)
    flat_cromo1 = cromossomo1.flatten()
    flat_cromo2 = cromossomo2.flatten()
    child1 = np.concatenate((flat_cromo1[:ponto_corte], flat_cromo2[ponto_corte:])).reshape(cromossomo1.shape)
    child2 = np.concatenate((flat_cromo2[:ponto_corte], flat_cromo1[ponto_corte:])).reshape(cromossomo1.shape)
    return child1, child2

# Mutação
def mutacao(cromossomo):
    if random.random() < mutation_rate:
        turma_index = random.randint(0, 8)
        dia = random.randint(0, 4)
        periodo = random.randint(0, 11)
        disciplina = cromossomo[turma_index, dia, periodo]
        novo_periodo = random.randint(0, 11)
        cromossomo[turma_index, dia, periodo], cromossomo[turma_index, dia, novo_periodo] = cromossomo[turma_index, dia, novo_periodo], disciplina
    return (cromossomo,0)

def tournament_selection(population, tournament_size=3):
    
    tournament = random.sample(population, tournament_size)
    
    sorted_population = sorted(tournament, key=lambda x: x[1], reverse=True)

    parents = [chromosome for chromosome, _ in sorted_population[:2]]
    
    return parents

# Inicializando a população
populacao = [(create_cromossomo(), 0) for _ in range(populacao_size)]

for generation in range(generations):
    
    populacao = [(cromossomo, fitness(cromossomo,quantidade_de_aulas,professores_disciplinas)) for cromossomo, _ in populacao]
    
    offspring = []
    while len(offspring) < populacao_size:
        parent1, parent2 = tournament_selection(populacao)
        child1, child2 = crossover(parent1, parent2)
        offspring.append((child1,0))
        offspring.append((child2,0))
        
    populacao = [mutacao(cromossomo) for cromossomo,_ in offspring]

   
    evaluated_population = [(cromossomo, fitness(cromossomo,quantidade_de_aulas,professores_disciplinas)) for cromossomo,_ in populacao]

    # Melhor solução
    best_solution = sorted(evaluated_population, key=lambda x: x[1], reverse=True)[0]
    
    print(f'Generation {generation}: Fitness = {best_solution[1]}')
    
# Melhor solução encontrada
melhor_cromossomo, melhor_fitness = max(populacao, key=lambda x: x[1])
print("Melhor fitness:", melhor_fitness)
print("Melhor grade horária:", melhor_cromossomo)
