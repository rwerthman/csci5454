import networkx as nx 
import matplotlib.pyplot as plt # Draw a graph from networkx
import random

def CreateGraph(n):
  n = 4 # Number of nodes in the graph
  p = 1.0/n # Probability of creating an edge between two vertices
  G = nx.gnp_random_graph(n, p)

  # Create a connected graph
  while not nx.is_connected(G):
    G = nx.gnp_random_graph(n, p)

  return G

def ChooseRandomEdge(G):
  # Get the list of edges in the graph
  edges = nx.edges(G)
  
  # Choose a random edge
  n = len(edges)
  r = random.randint(0, n-1)
  return edges[r]

def ContractGraph(G):
  while nx.number_of_nodes(G) > 2:
    e = ChooseRandomEdge(G)
    G = nx.contracted_edge(G, e)
  
  return G

def main():

  n = 4 # Number of nodes in the graph
  G = CreateGraph(n)

  print 'Number of nodes in graph', G.number_of_nodes()
  print 'Number of edges in graph', G.size()

  print 'Min cut of graph', len(nx.minimum_edge_cut(G))

  G = ContractGraph(G)
  print 'Number of nodes in graph', G.number_of_nodes()
  print 'Number of edges in graph', G.size()

  #G.contracted_edge(G,)
  
  nx.draw(G)
  plt.savefig("ps3_q5.png")

if __name__ == '__main__':
  main()