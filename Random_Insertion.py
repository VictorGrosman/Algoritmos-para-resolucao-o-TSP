import algorithm_helpers
import random
import visualizacaoGrafica as vg

def Solver(caminhoInstancias):
    solucao = []
    suporte = []
    menor_distancia = float('inf')

    instancia = algorithm_helpers.le_dados(caminhoInstancias)
    qtd_pontos, mat_dist , coords= instancia.qtd_pontos, instancia.mat_dist, instancia.coords

    pontosDisponiveis = []
    for i in range(qtd_pontos):
        pontosDisponiveis.append(i + 1) #Criando uma variável que controla quais pontos ainda não foram inseridos na solucao

    for par, distancia in mat_dist.items():
        if distancia < menor_distancia and distancia != 0:
            suporte = par
            menor_distancia = distancia
    solucao.append(suporte[0])
    solucao.append(suporte[1])
    pontosDisponiveis.remove(suporte[0])
    pontosDisponiveis.remove(suporte[1])

    for i in range(len(pontosDisponiveis)):
        ponto = random.choice(pontosDisponiveis)
        solucao = algorithm_helpers.encontra_melhor_vizinho(ponto, solucao, mat_dist)
        pontosDisponiveis.remove(ponto)
        # vg.grafico(caminhoInstancias, solucao)
    custo = algorithm_helpers.calcula_custo(mat_dist, solucao)
    print("Random Insertion - Distancia total:", round(custo, 2))
    # print("Solucao:", solucao)
    return solucao