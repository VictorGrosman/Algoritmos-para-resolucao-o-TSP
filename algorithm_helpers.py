from dataclasses import dataclass, field
import math
import copy
import concurrent.futures

@dataclass
class Instancia:
    qtd_pontos: int = 0
    conj_pontos: set = field(default_factory=set)
    coords: dict = field(default_factory=dict)  # As coordenadas podem ser ignoradas quando não fornecidas
    mat_dist: dict = field(default_factory=dict)

def le_dados(arq_inst):
    dados = Instancia()

    with open(arq_inst, 'r', encoding='utf8') as f:
        linhas = f.readlines()
        i = 0
        linha = linhas[i].strip()

        # Procurando por DIMENSION e coletando dados até NODE_COORD_SECTION ou EDGE_WEIGHT_SECTION
        while linha != "NODE_COORD_SECTION" and linha != "EDGE_WEIGHT_SECTION":
            s_valores = linha.split(':')
            if s_valores[0].strip() == "DIMENSION":
                dados.qtd_pontos = int(s_valores[1].strip())
            i += 1
            linha = linhas[i].strip()

        # Verificando se estamos lidando com NODE_COORD_SECTION (coordenadas) ou EDGE_WEIGHT_SECTION (matriz de distâncias)
        if linha == "NODE_COORD_SECTION":
            del linhas[:i + 1]
            # Lê as coordenadas
            for i in range(dados.qtd_pontos):
                s_valores = linhas[i].strip().split()
                id_ponto = int(s_valores[0])
                dados.conj_pontos.add(id_ponto)
                cx = float(s_valores[1])
                cy = float(s_valores[2])
                dados.coords[id_ponto] = (cx, cy)

            # Calcula a matriz de distâncias (se as coordenadas foram lidas)
            for p1 in dados.conj_pontos:
                for p2 in dados.conj_pontos:
                    if p1 == p2:
                        dados.mat_dist[p1, p2] = 0.0
                    else:
                        x1, y1 = dados.coords[p1]
                        x2, y2 = dados.coords[p2]
                        distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                        dados.mat_dist[p1, p2] = distancia
                        dados.mat_dist[p2, p1] = distancia

        elif linha == "EDGE_WEIGHT_SECTION":
            del linhas[:i + 1]
            # Lê a matriz de distâncias triangular superior
            for i in range(dados.qtd_pontos - 1):
                s_valores = list(map(float, linhas[i].strip().split()))
                # if len(s_valores) != dados.qtd_pontos - i - 1:
                #     raise ValueError(
                #         f"A linha {i + 1} possui um número incorreto de distâncias. Esperado {dados.qtd_pontos - i - 1}, mas encontrou {len(s_valores)}.")

                # Preenchendo a matriz de distâncias simétrica
                for j in range(len(s_valores)):
                    dist = s_valores[j]
                    dados.mat_dist[i + 1, i + j + 2] = dist  # Preenche a parte superior da diagonal
                    dados.mat_dist[i + j + 2, i + 1] = dist  # Preenche a parte inferior simétrica

    return dados

def calcula_custo(mat_dist, solucao):
    custo = 0
    solucaoCopia = copy.deepcopy(solucao)
    solucaoCopia.append(solucao[0]) #Adicionando o primeiro ponto para que ele seja o ultimo, assim completando um circuito fechado
    for i in range(len(solucaoCopia) - 1):
        custo = custo + mat_dist[solucaoCopia[i], solucaoCopia[i + 1]]
    return custo

def encontra_melhor_vizinho(ponto, solucao, mat_dist):
    melhor_solucao = None
    melhor_custo = float("inf")
    def calcula_candidato(i):
        sol_candidata = copy.deepcopy(solucao)
        sol_candidata.insert(i, ponto)
        custo = calcula_custo(mat_dist, sol_candidata)
        return custo, sol_candidata

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor: #Importante: o computador tem 16 threads, se for rodar em outro pode ser necessário modificar este valor
        resultados = executor.map(calcula_candidato, range(len(solucao) + 1))
        for custo, sol_candidata in resultados:
            if custo < melhor_custo:
                melhor_solucao = sol_candidata
                melhor_custo = custo
    return melhor_solucao