# Grafo do problema
grafo = {
    'Arad':{'Zerind':75, 'Sibiu':140, 'Timisoara':118},
    'Bucharest':{'Pitesti':101, 'Fagaras':211, 'Urziceni':85, 'Giurgiu':90},
    'Craiova':{'Drobeta':120, 'Rimnicu_Vilcea':146, 'Pitesti':138},
    'Drobeta':{'Mehadia':75, 'Craiova':120},
    'Eforie':{'Hirsova':86},
    'Fagaras':{'Sibiu':99, 'Bucharest':211},
    'Giurgiu':{'Bucharest':90},
    'Hirsova':{'Urziceni':98, 'Eforie':86},
    'Iasi':{'Neamt':87, 'Vaslui':92},
    'Lugoj':{'Timisoara':111, 'Mehadia':70},
    'Mehadia':{'Lugoj':70, 'Drobeta':75},
    'Neamt':{'Iasi':87},
    'Oradea':{'Zerind':71, 'Sibiu':151},
    'Pitesti':{'Rimnicu_Vilcea':97, 'Bucharest':101, 'Craiova':138},
    'Rimnicu_Vilcea':{'Sibiu':80, 'Pitesti':97, 'Craiova':146},
    'Sibiu':{'Arad':140, 'Oradea':151, 'Fagaras':99, 'Rimnicu_Vilcea':80},
    'Timisoara':{'Arad':118, 'Lugoj':111},
    'Urziceni':{'Bucharest':85, 'Vaslui':142, 'Hirsova':98},
    'Vaslui':{'Iasi':92, 'Urziceni':142},
    'Zerind':{'Arad':75, 'Oradea':71}
}

# Distância em linha reta até Bucharest
distancia_bucharest = {
    'Arad':{'Bucharest':366},
    'Bucharest':{'Bucharest':0},
    'Craiova':{'Bucharest':160},
    'Drobeta':{'Bucharest':242},
    'Eforie':{'Bucharest':161},
    'Fagaras':{'Bucharest':176},
    'Giurgiu':{'Bucharest':77},
    'Hirsova':{'Bucharest':151},
    'Iasi':{'Bucharest':226},
    'Lugoj':{'Bucharest':244},

    'Mehadia':{'Bucharest':241},
    'Neamt':{'Bucharest':234},
    'Oradea':{'Bucharest':380},
    'Pitesti':{'Bucharest':100},
    'Rimnicu_Vilcea':{'Bucharest':193},
    'Sibiu':{'Bucharest':253},
    'Timisoara':{'Bucharest':329},
    'Urziceni':{'Bucharest':80},
    'Vaslui':{'Bucharest':199},
    'Zerind':{'Bucharest':374},
}

def busca_gulosa_A(grafo, distancia_bucharest, inicio, objetivo, tipo_de_busca):
    caminho = [inicio]  
    while caminho[-1] != objetivo:  #Forma de pesquisa da direita para esquerda[-3,-2,-1]
        atual = caminho[-1]  
        proximo = None  
        menor_distancia = 99999 # Valor grande para não interferir na primeira passagem
        
        # Percorre os vizinhos do nó atual
        for vizinho, distancia in grafo[atual].items():

            # Verifica se o vizinho não está no caminho atual
            if vizinho not in caminho:
                heuristica = distancia_bucharest[vizinho][objetivo]
                
                # Soma da distância mais heuristica para A*
                if tipo_de_busca == 'A*':
                    heuristica = heuristica + distancia

                # Verifica se a heurística é menor que a menor distância encontrada
                if heuristica < menor_distancia:
                    menor_distancia = heuristica 
                    proximo = vizinho  # Atualiza o próximo nó
        
        if proximo is None:
            # Se não há próximo nó, retorna um caminho vazio indicando falha
            return []
        
        caminho.append(proximo)  # Adiciona o próximo nó ao caminho
    return caminho  # Retorna o caminho encontrado

# Calcula a distância que está dentro dos grafos baseado no caminho percorrido
def calcular_distancia_total(grafo, caminho):
    distancia_total = 0
    for i in range(len(caminho)-1):
        cidade_atual = caminho[i]
        cidade_vizinha = caminho[i+1]
        distancia = grafo[cidade_atual][cidade_vizinha]
        distancia_total += distancia
    return distancia_total

# Começo do código
inicio = 'Arad'
objetivo = 'Bucharest' #Setado baseado na heuristica
distancia_total = 0

# Resultados obtidos da busca Gulosa
caminho = busca_gulosa_A(grafo, distancia_bucharest, inicio, objetivo, 'gulosa')
distancia_total = calcular_distancia_total(grafo, caminho)

if len(caminho) > 0:
    print(f'Caminho de {inicio} até {objetivo} na busca Gulosa {distancia_total} milhas:')
    print(' -> '.join(caminho))
else:
    print(f'Não foi possível encontrar um caminho de {inicio} até {objetivo}.')

print('\n')

# Resultados obtidos da busca A*
caminho = busca_gulosa_A(grafo, distancia_bucharest, inicio, objetivo, 'A*')
distancia_total = calcular_distancia_total(grafo, caminho)
if len(caminho) > 0:
    print(f'Caminho de {inicio} até {objetivo} na busca A* {distancia_total} milhas:')
    print(' -> '.join(caminho))
else:
    print(f'Não foi possível encontrar um caminho de {inicio} até {objetivo}.')
