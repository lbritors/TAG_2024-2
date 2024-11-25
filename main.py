import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from networkx.algorithms.clique import find_cliques

def read_graph(file_path):
  df = pd.read_csv(file_path, comment='%', delim_whitespace=True, header=None, names=['source', 'target'])
  return nx.from_pandas_edgelist(df, 'source', 'target')

def print_vertices_degrees(G):
  for node, degree in G.degree():
    print(f'Vertices: {node}, Graus: {degree}')

def print_maximal_cliques(G):
  maximal = list(find_cliques(G))
  for i, clique in enumerate(maximal):
    print(f'Clique {i+1}: {len(clique)} vertices - {clique}')
  return maximal

def print_clustering_coef(G):
  aglomeracao = nx.clustering(G)
  for node, coef in aglomeracao.items():
    print(f'Vertice {node}: Coeficiente de Aglorameração: {coef}')

def print_average_clustering(G):
  coef_medio = nx.average_clustering(G)
  print(f'Coeficiente médio de aglomeração do grafo: {coef_medio}')

def visualize_graf(G, maximal):
  plt.figure(figsize=(10, 10))
  pos = nx.spring_layout(G)
  cores = ['yellow', 'pink', 'green', 'orange', 'blue', 'purple', 'red', 'aquamarine', 'violet']
  for i, clique in enumerate(maximal):
    nx.draw_networkx_nodes(G, pos, nodelist=clique, node_color=cores[i % len(cores)], node_size=500, alpha=0.8, label=f'Clique {i+1}')
  nx.draw_networkx_edges(G, pos, edge_color='black', width=1, alpha=0.5)
  nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
  plt.title("Visualização do Grafo com Cliques Maximais Coloridos")
  plt.show()

def visualize_graf_animation(G, maximal):
  cores = ['yellow', 'pink', 'green', 'orange', 'blue', 'purple', 'red', 'aquamarine', 'violet']
  pos = nx.spring_layout(G)

  fig, ax = plt.subplots(figsize=(10, 10))
  def update(num): 
    ax.clear()
    nx.draw_networkx_edges(G, pos, ax=ax)
    for i, clique in enumerate(maximal[:num+1]):
      nx.draw_networkx_nodes(G, pos, nodelist=clique, node_color=cores[i % len(cores)], ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)
    ax.set_title(f'Cliques até o momento: {num+1}')
  ani = animation.FuncAnimation(fig, update, frames=len(maximal), repeat=False, interval=1000)
  plt.show()

if __name__ == "__main__":
  G = read_graph('soc-dolphins.mtx')
  print_vertices_degrees(G)
  maximal = print_maximal_cliques(G)
  print_clustering_coef(G)
  print_average_clustering(G)
  visualize_graf(G, maximal)
  visualize_graf_animation(G, maximal)
