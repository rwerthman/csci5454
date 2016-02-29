import networkx as nx 
import matplotlib.pyplot as plt # Draw a graph from networkx
import random

def CreateGraph(n):
  p = 1.0/n # Probability of creating an edge between two vertices
  G = nx.gnp_random_graph(n, p)

  # Create a connected graph
  while not nx.is_connected(G):
    G = nx.gnp_random_graph(n, p)

  G = nx.MultiGraph(G)

  return G

def ChooseRandomEdge(G):
  # Get the list of edges in the graph
  edges = nx.edges(G)
  
  # Choose a random edge
  n = len(edges)
  r = random.randint(0, n-1)
  return edges[r]

def RunKarger(G):
  while nx.number_of_nodes(G) > 2:
    e = ChooseRandomEdge(G)
    G = ContractEdge(G,e)
  return G

def ContractEdge(G,e):
  # Get the endpoints of the contracted edge
  u = e[0]
  v = e[1]

  # Remove the contracted edge
  G.remove_edge(u,v)
  
  # Get the edges to the nodes that are
  # the endpoints of the contracted edge
  edges = nx.edges(G,nbunch=[u,v])

  # Add the edges to u and v to u which
  # will be used as the new node
  for edge in edges:
    if u != edge[0]:
      G.add_edge(u,edge[1])

  # Remove one of the endpoints of the contracted edge
  G.remove_node(v)
    
  return G
  
  

def DrawGraph(G, filename):
  pos = nx.shell_layout(G)
  nx.draw_networkx_nodes(G,pos)
  nx.draw_networkx_edges(G,pos)
  nx.draw_networkx_labels(G,pos)
  plt.savefig(filename)
  

def main():

  n = 20 # Number of nodes in the graph
  G = CreateGraph(n)
  plt.figure(1)
  DrawGraph(G, 'ps3_q5.png')

  print 'Number of nodes in graph', G.number_of_nodes()
  print 'Number of edges in graph', G.size()

  print 'Canonical min cut of graph', len(nx.minimum_edge_cut(G))

  G = RunKarger(G)
  plt.figure(2)
  DrawGraph(G, 'ps3_q5_test.png')

  print 'Min cut found by Karger', G.size()

if __name__ == '__main__':
  main()