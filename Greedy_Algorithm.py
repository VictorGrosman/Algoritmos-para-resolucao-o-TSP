import copy
from visualizacaoGrafica import grafico
import algorithm_helpers

def procuraValor(lista, valor):
    for i, item in enumerate(lista):
        if isinstance(item, (list, tuple)) and valor in item:  # Verifica se é uma lista ou tupla e se contém o valor
            return i
    return None  # Retorna None se o valor não for encontrado

def verificar_pontas(lista_principal, valor_procurado):
    position = None  # Inicializa a posição como None
    for sublista in lista_principal:
        if sublista[0] == valor_procurado:
            position = 0  # Está no início da sublista
            break  # Sai do loop após encontrar a primeira ocorrência
        elif sublista[-1] == valor_procurado:
            position = 1  # Está no final da sublista
            break  # Sai do loop após encontrar a primeira ocorrência
        else:
            position = 2  # Não está nas pontas da sublista
    return position

def Solver(caminhoInstancias):
    instancia = algorithm_helpers.le_dados(caminhoInstancias)
    qtd_pontos, mat_dist = instancia.qtd_pontos, instancia.mat_dist
    copia_mat_dist = copy.deepcopy(mat_dist)
    pontos = []
    pares = []

    for i in range(qtd_pontos):
        pontos.append([i + 1, 0]) # a ideia é que se o ponto estiver entre dois outros, então o segundo valor será o 2
    # se tiver o 0, este ponto não foi selecionado e se tiver 1, ele está na ponta

    for i in range(qtd_pontos):
        menor_distancia = float('inf')
        pares_menor_distancia = []
        parMexido = []

        for par, distancia in mat_dist.items():
            if pares:
                indicePar0 = par[0] - 1
                indicePar1 = par[1] - 1
                if pontos[indicePar0][1] == 0 and pontos[indicePar1][1] == 0:
                    if par[0] != par[1]:
                        if distancia < menor_distancia:
                            menor_distancia = distancia
                            pares_menor_distancia = [par[0], par[1]]  # Substitui a lista com o novo par
                            parMexido = [par[0], par[1]]
            elif distancia > 0:  # Ignorar distâncias iguais a 0
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    pares_menor_distancia = [par[0], par[1]]  # Substitui a lista com o novo par
                    parMexido = [par[0], par[1]]
                else: continue
        if pares and len(pares) >= 2:
            resultado = [item for item in pontos if item[1] == 1]
            for i in range(len(resultado)):
                quebra = False
                for k in range(len(resultado)):
                    suporte = []
                    suporte2 = []
                    position1 = None
                    position2 = None
                    if procuraValor(pares, resultado[i][0]) != procuraValor(pares, resultado[k][0]):
                        if mat_dist[resultado[i][0], resultado[k][0]] < menor_distancia and mat_dist[resultado[i][0], resultado[k][0]] > 0:
                            menor_distancia = mat_dist[resultado[i][0], resultado[k][0]]
                            position1 = verificar_pontas(pares, resultado[i][0])
                            position2 = verificar_pontas(pares, resultado[k][0])
                            par = [resultado[i][0], resultado[k][0]]
                            pares_menor_distancia = []
                            parMexido = [par[0], par[1]]
                            if position1 == 0 and position2 == 0:
                                quebra = True
                                for z in reversed(range(len(pares[procuraValor(pares, resultado[i][0])]))):
                                    suporte.append(pares[procuraValor(pares, resultado[i][0])][z])
                                for z in range(len(pares[procuraValor(pares, resultado[k][0])])):
                                    suporte.append(pares[procuraValor(pares, resultado[k][0])][z])
                                for z in range(len(suporte)):
                                    pares_menor_distancia.append(suporte[z])
                                del pares[procuraValor(pares, par[0])]
                                del pares[procuraValor(pares, par[1])]
                            elif position1 == 1 and position2 == 0:
                                quebra = True
                                for z in range(len(pares[procuraValor(pares, resultado[i][0])])):
                                    suporte.append(pares[procuraValor(pares, resultado[i][0])][z])
                                for z in range(len(pares[procuraValor(pares, resultado[k][0])])):
                                    suporte.append(pares[procuraValor(pares, resultado[k][0])][z])
                                for z in range(len(suporte)):
                                    pares_menor_distancia.append(suporte[z])
                                del pares[procuraValor(pares, par[0])]
                                del pares[procuraValor(pares, par[1])]
                            elif position1 == 0 and position2 == 1:
                                quebra = True
                                for z in range(len(pares[procuraValor(pares, resultado[k][0])])):
                                    suporte.append(pares[procuraValor(pares, resultado[k][0])][z])
                                for z in range(len(pares[procuraValor(pares, resultado[i][0])])):
                                    suporte.append(pares[procuraValor(pares, resultado[i][0])][z])
                                for z in range(len(suporte)):
                                    pares_menor_distancia.append(suporte[z])
                                del pares[procuraValor(pares, par[0])]
                                del pares[procuraValor(pares, par[1])]
                            elif position1 == 1 and position2 == 1:
                                quebra = True
                                for z in range(len(pares[procuraValor(pares, resultado[i][0])])):
                                    suporte.append(pares[procuraValor(pares, resultado[i][0])][z])
                                for z in reversed(range(len(pares[procuraValor(pares, resultado[k][0])]))):
                                    suporte.append(pares[procuraValor(pares, resultado[k][0])][z])
                                for z in range(len(suporte)):
                                    pares_menor_distancia.append(suporte[z])
                                del pares[procuraValor(pares, par[0])]
                                del pares[procuraValor(pares, par[1])]
                            if quebra == True:
                                break
                            else:
                                continue
                if quebra == True:
                    break
                else: continue
        if parMexido:
            for i in range(len(pontos)):
                if pontos[i][0] == parMexido[0]:
                    pontos[i][1] = pontos[i][1] + 1
                elif pontos[i][0] == parMexido[1]:
                    pontos[i][1] = pontos[i][1] + 1
        if parMexido:
            del mat_dist[parMexido[0], parMexido[1]]
            del mat_dist[parMexido[1], parMexido[0]]
        if pares_menor_distancia:
            pares.append(pares_menor_distancia)
        # grafico(caminhoInstancias, pares)
    solucao = []
    for i in range(len(pares[0])):
        solucao.append(pares[0][i])
    custo = algorithm_helpers.calcula_custo(copia_mat_dist, solucao)
    print("Greedy Algorithm - Distancia total", round(custo, 2))
    print("Solucao:", solucao)
    return solucao