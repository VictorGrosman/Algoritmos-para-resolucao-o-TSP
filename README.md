# 🗺️ Heurísticas para o Problema do Caixeiro Viajante (PCV)

Repositório contendo os códigos e análises desenvolvidos durante meu projeto de **Iniciação Científica** no curso de **Engenharia de Produção** na **Universidade Tecnológica Federal do Paraná (UTFPR) - Campus Londrina**. 

O projeto aborda o estudo e a aplicação de algoritmos de inteligência computacional para resolver o clássico Problema do Caixeiro Viajante (PCV / TSP). A parte de visualização e construção gráfica das rotas foi inspirada pelos modelos do projeto [Animated Algorithms for the Traveling Salesman Problem (Stemlounge)](https://stemlounge.com/animated-algorithms-for-the-traveling-salesman-problem/).

## 🧠 Sobre o Projeto e Metodologia

O PCV é um problema NP-difícil que consiste em encontrar a rota mais curta que visite um conjunto de cidades exatamente uma vez e retorne à origem. O objetivo deste estudo foi realizar uma análise comparativa de diversas heurísticas construtivas combinadas com a técnica de busca local (melhoria) 2-Opt. 

A metodologia consistiu em testar os algoritmos em um conjunto diversificado de 38 instâncias de benchmark da biblioteca TSPLib. O desempenho foi medido considerando duas métricas:
* **Qualidade da Solução:** Avaliada pelo erro percentual (gap) em relação aos valores ótimos globais conhecidos da literatura.
* **Tempo Computacional:** Medido em segundos totais de execução para cada algoritmo rodado.

## ⚙️ Algoritmos Implementados

A lógica dos solvers foi quebrada de forma modular e implementada em Python.

### Heurísticas Construtivas
* **`Nearest_Neighbor.py`**: Algoritmo guloso que constrói a rota selecionando iterativamente a cidade não visitada mais próxima da posição atual.
* **`Nearest_Insertion.py`**: Inicia com um subtour básico e insere iterativamente a cidade não visitada mais próxima que minimize o aumento total do custo da rota.
* **`Cheapest_Insertion.py`**: Busca a cidade e a posição específica de inserção na rota que resultem no menor custo absoluto de acréscimo de distância.
* **`Farthest_Insertion.py`**: Prioriza a inserção do ponto que possua a maior distância em relação ao subtour em formação.
* **`Random_Insertion.py`**: Seleciona um ponto de forma aleatória e calcula sua inserção buscando o melhor vizinho disponível.
* **`Greedy_Algorithm.py`**: Constrói a rota escolhendo as menores distâncias globais na matriz, iterativamente conectando nós de extremidade desde que não formem ciclos prematuros.

### Heurística de Busca Local
* **`Opt2.py`**: Implementa a técnica 2-Opt, que atua realizando a quebra e a troca sistemática de pares de arestas não adjacentes em um ciclo para aprimorar uma solução inicial gerada por outras heurísticas, rodando até convergir para um ótimo local.

### Módulos Auxiliares
* **`algorithm_helpers.py`**: Script base responsável pela leitura padronizada de dados das instâncias (como pesos de arestas e seções de nós), cálculo de custos e busca paralela de melhores vizinhos utilizando `concurrent.futures.ThreadPoolExecutor` para otimizar o tempo computacional.
* **`visualizacaoGrafica.py`**: Utiliza a biblioteca `matplotlib` para gerar gráficos do tipo *scatter plot*, conectando os nós com as rotas geradas pelas heurísticas de forma visual.

## 📊 Principais Resultados

Ao testar e analisar os algoritmos contra as instâncias da TSPLib, os resultados apontaram que:
* Avaliadas isoladamente, a heurística *Nearest Insertion* tendeu a gerar rotas iniciais de melhor qualidade do que a heurística *Nearest Neighbor*.
* A aplicação da heurística 2-Opt foi determinante e essencial para aprimorar as soluções de ambas as rotinas construtivas testadas.
* A execução do *Nearest Neighbor* refinado pelo *2-Opt* conseguiu derrubar o gap (erro) médio de 25,30% para a marca de 7,83%.
* A combinação *Nearest Insertion* + *2-Opt* também demonstrou um excelente equilíbrio prático entre a qualidade do roteamento final e o tempo computacional investido.

> 💡 **Nota sobre a implementação:**
> Este projeto foi desenvolvido com foco no aprendizado acadêmico e na exploração prática da lógica algorítmica. Os códigos de otimização foram escritos e modelados inteiramente **do zero (pure Python)**, priorizando o raciocínio matemático sólido e a compreensão das estruturas de dados aplicadas à Pesquisa Operacional em vez da utilização de bibliotecas e *solvers* prontos.
