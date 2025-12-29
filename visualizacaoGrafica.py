from dataclasses import dataclass, field
import matplotlib.pyplot as plt
import math

@dataclass
class Instancia:
    qtd_pontos: int = 0
    conj_pontos: set = field(default_factory=set)
    coords: dict = field(default_factory=dict)

def le_dados(arq_inst):
    dados = Instancia()
    with open(arq_inst, 'r', encoding='utf8') as f:
        linhas = f.readlines()
        i = 0
        linha = linhas[i].strip()
        while linha != "NODE_COORD_SECTION":
            s_valores = linha.split(':')
            if s_valores[0].strip() == "DIMENSION":
                dados.qtd_pontos = int(s_valores[1].strip())
            i += 1
            linha = linhas[i].strip()
        del linhas[:i + 1]
        for i in range(dados.qtd_pontos):
            s_valores = linhas[i].strip().split()
            id_ponto = int(s_valores[0])
            dados.conj_pontos.add(id_ponto)
            cx = float(s_valores[1])  # Alterado para float
            cy = float(s_valores[2])  # Alterado para float
            dados.coords[id_ponto] = (cx, cy)
    return dados

def grafico(nomeInstancia, ordem):
    instancia = le_dados(nomeInstancia)
    pontosCoords = instancia.coords

    plt.figure(figsize=(8, 6))

    x = [coord[0] for coord in pontosCoords.values()]
    y = [coord[1] for coord in pontosCoords.values()]
    plt.scatter(x, y, color='blue', label='Pontos')

    # Adiciona os números dos pontos
    # for id_ponto, coord in pontosCoords.items():
    #     plt.text(coord[0], coord[1], str(id_ponto), fontsize=9, ha='right', color='red')

    if isinstance(ordem[0], list):  # Caso seja uma lista de listas
        for sublista in ordem:
            for i in range(len(sublista) - 1):
                ponto1 = sublista[i]
                ponto2 = sublista[i + 1]
                x1, y1 = pontosCoords[ponto1]
                x2, y2 = pontosCoords[ponto2]
                plt.plot([x1, x2], [y1, y2], color='black', linewidth=1.5)
    else:  # Caso seja uma lista simples
        for i in range(len(ordem) - 1):
            ponto1 = ordem[i]
            ponto2 = ordem[i + 1]
            x1, y1 = pontosCoords[ponto1]
            x2, y2 = pontosCoords[ponto2]
            plt.plot([x1, x2], [y1, y2], color='black', linewidth=1.5)

        x1, y1 = pontosCoords[ordem[-1]]
        x2, y2 = pontosCoords[ordem[0]]
        plt.plot([x1, x2], [y1, y2], color='black', linewidth=1)

    plt.title('Gráfico da instância ' + nomeInstancia, fontsize=16)
    plt.xlabel('Coordenada X', fontsize=14)
    plt.ylabel('Coordenada Y', fontsize=14)
    plt.grid(True)
    plt.legend()
    plt.show()
