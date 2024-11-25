# Análise de Grafos com NetworkX

## Introdução

Este projeto consiste na análise de um grafo não direcionado e sem pesos, utilizando a biblioteca NetworkX. O grafo é criado a partir de um arquivo de entrada que contém as arestas. As seguintes análises são realizadas:

1. Cálculo e impressão do grau de cada vértice.
2. Identificação e impressão de todos os cliques maximais.
3. Cálculo do Coeficiente de Aglomeração de cada vértice.
4. Cálculo do Coeficiente médio de Aglomeração do Grafo.
5. Visualização do grafo com cliques maximais coloridos em png.
6. Visualização do grafo com cliques maximais coloridos em animação.

## Arquivos

- `main.py`: Código principal do projeto.
- `README.md`: Este arquivo de documentação.
- `Figure_1.pn`: Este arquivo é o mesmo gerado durante a execução do programa para visualização dos cliques do grafo em png.
- `cliques_animation2.gif`: Este arquivo é a animação com os cliques maximais sendo mostrados durante a execução do programa.
- `soc-dolphins.mtx`: Arquivo base para a geração do grafo, adquirido em <a href="http://networkrepository.com">NetworkRepository</a>

## Requisitos

- Python 3.x
- Bibliotecas: `networkx`, `pandas`, `matplotlib`

## Instalação

Instale as bibliotecas necessárias utilizando o pip:

```bash
pip install networkx pandas matplotlib
```

## Execução

```bash
python main.py
```
