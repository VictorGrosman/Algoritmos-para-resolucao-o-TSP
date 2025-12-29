import algorithm_helpers
import visualizacaoGrafica as vg

def Solver(caminhoInstancias):
    instancia = algorithm_helpers.le_dados(caminhoInstancias)
    qtd_pontos, mat_dist , coords= instancia.qtd_pontos, instancia.mat_dist, instancia.coords

    pontosDisponiveis = []
    for i in range(qtd_pontos):
        pontosDisponiveis.append(i + 1) #Criando uma variável que controla quais pontos ainda não foram inseridos na solucao

    solucao = []
    suporte = []
    menor_distancia = float('inf')

    for par, distancia in mat_dist.items():
        if distancia < menor_distancia and distancia != 0:
            suporte = par
            menor_distancia = distancia
    solucao.append(suporte[0])
    solucao.append(suporte[1])
    pontosDisponiveis.remove(suporte[0])
    pontosDisponiveis.remove(suporte[1])

    while pontosDisponiveis:
        menor_custo = float('inf')
        ponto = None
        for i in range(len(pontosDisponiveis)):
            ponto = pontosDisponiveis[i]
            solucao_temporaria = algorithm_helpers.encontra_melhor_vizinho(ponto, solucao, mat_dist)
            custo = algorithm_helpers.calcula_custo(mat_dist, solucao_temporaria)
            if custo < menor_custo:
                menor_custo = custo
                melhor_solucao = solucao_temporaria[:]
                melhor_ponto = ponto
        # print("menor_custo", round(menor_custo, 2))
        solucao = melhor_solucao[:]
        pontosDisponiveis.remove(melhor_ponto)
        # vg.grafico(caminhoInstancias, solucao)
    custo = algorithm_helpers.calcula_custo(mat_dist, solucao)
    print("Cheapest Insertion - Distancia total:", round(custo, 2))
    # print("Solucao:", solucao)
    return solucao