import algorithm_helpers
import random
import copy

def Solver(nomeInstancia):
    instancia = algorithm_helpers.le_dados(nomeInstancia)
    qtd_pontos, pontos, mat_dist =instancia.qtd_pontos, instancia.conj_pontos, instancia.mat_dist
    copia_mat_dist = copy.deepcopy(mat_dist)

    pontoAleatorio = random.choice(list(pontos)) # Escolhendo um ponto aleatório
    pontos.remove(pontoAleatorio)                # Removendo ele da lista de pontos
    solucao = [pontoAleatorio]
    pontoEscolhido = pontoAleatorio

    for _ in range(qtd_pontos - 1):  # Já temos o ponto inicial, então iteramos qtd_pontos - 1
        menor_distancia = float('inf')
        ponto_mais_proximo = None
        chave_a_remover = None

        # Iterar pela matriz de distâncias para encontrar o ponto mais próximo
        for (p1, p2), distancia in mat_dist.items():
            # Verificar se o ponto atual está no par e ignorar pares inválidos (p1 == p2 ou ponto já usado)
            if p1 == pontoEscolhido and p2 in pontos:
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    ponto_mais_proximo = p2
                    chave_a_remover = (p1, p2)
        # Atualizar a solução e remover o ponto encontrado
        if ponto_mais_proximo is not None:
            solucao.append(ponto_mais_proximo)
            pontos.remove(ponto_mais_proximo)
            # Remover a chave correspondente da matriz de distâncias
            if chave_a_remover:
                mat_dist.pop(chave_a_remover, None)  # Remove a chave, se existir
                # Remover a chave simétrica (p2, p1), se existir
                chave_simetrica = (chave_a_remover[1], chave_a_remover[0])
                mat_dist.pop(chave_simetrica, None)

            # Atualizar o ponto escolhido para o próximo
            pontoEscolhido = ponto_mais_proximo
        else:
            break
    custo = algorithm_helpers.calcula_custo(copia_mat_dist, solucao)
    print("Nearest Neighbor - Distancia total:", round(custo, 2))
    # print("Solucao:", solucao)
    return solucao