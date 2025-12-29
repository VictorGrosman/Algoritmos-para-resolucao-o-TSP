import copy
import algorithm_helpers
import visualizacaoGrafica as vg

def Solver(caminhoInstancias, solucaoInicial):
    instancia = algorithm_helpers.le_dados(caminhoInstancias)
    qtd_pontos, mat_dist , coords = instancia.qtd_pontos, instancia.mat_dist, instancia.coords
    custo_inicial = algorithm_helpers.calcula_custo(mat_dist, solucaoInicial)

    solucao = copy.deepcopy(solucaoInicial)
    menor_distancia = custo_inicial
    n = len(solucaoInicial)

    while True:
        melhoria = False
        for i in range(n - 1):
            for j in range(i + 2, n):
                # Cria uma nova solução aplicando a troca 2-opt
                parte1 = solucao[:i + 1]  # Mantemos a primeira parte (de 0 até i)
                parte2 = solucao[i + 1:j + 1][::-1]  # Invertendo a subsequência de i+1 até j
                parte3 = solucao[j + 1:]  # Mantemos o restante após j

                nova_solucao = parte1 + parte2 + parte3

                custo = algorithm_helpers.calcula_custo(mat_dist, nova_solucao)

                if custo < menor_distancia:
                    menor_distancia = custo
                    solucao = nova_solucao[:]
                    melhoria = True
        if not melhoria:
            break

    custo_final = algorithm_helpers.calcula_custo(mat_dist, solucao)
    custo = round(custo_final, 2)
    return custo, solucao