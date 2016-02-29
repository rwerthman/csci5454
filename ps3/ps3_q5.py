'''
Robert Werthman
csci 5454, problem set 3, question 5(a)

Create a plot of running Karger's algorithm on
different size random graphs.
'''

import networkx as nx 
import matplotlib.pyplot as plt # Draw a graph from networkx
import random
import csv

def CreateGraph(n):
  '''
  Description:
    Creates a random networkx graph and then
    converts it a multigraph

  Args:
    n number of nodes to be in graph

  Returns:
    a graph with n nodes and random edges
  '''
  p = 1.0/n # Probability of creating an edge between two vertices
  G = nx.gnp_random_graph(n, p)

  # Create a connected graph
  while not nx.is_connected(G):
    G = nx.gnp_random_graph(n, p)

  G = nx.MultiGraph(G)

  return G

def ChooseRandomEdge(G):
  '''
  Description:
    Chooses a random edge from a newtorkx graph

  Args:
    G a networkx graph

  Returns:
    a tuple of endpoints for a randomly selected edge in a graph
  '''
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
  '''
  Description:
    Contracts an edge in a graph by removing it
    and creating a new vertex from one of the 
    endpoints of the edge.  Takes all edges from
    both endpoints and connects them to new vertex.


  Args:
    G graph with edge to contract
    e tuple of endpoints in edge to contract

  Returns:
    G a new graph with an edge contracted
  '''
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
  '''
  Description:
    Used to create a picture of a networkx graph
    for testing

  Args:
    G a networkx graph
    filename file to save picture of graph to

  Returns:
    Creates a picture of a newtorkx graph as output

  '''
  pos = nx.shell_layout(G)
  nx.draw_networkx_nodes(G,pos)
  nx.draw_networkx_edges(G,pos)
  nx.draw_networkx_labels(G,pos)
  plt.savefig(filename)
  
def Write(filename, n, prob):
  '''
  Description:
    Writes output to a file
  
  Args:
    n number of nodes in a graph
    prob probability of find min cut with n-node graph

  Returns:
    Outputs n and prob to a file
  '''
  f = open(filename, 'a')
  f.write('{0},{1}\n'.format(n,prob))
  f.close()

def ReadCSV(filename):
  '''
  Description:
    Reads in csv file row by row and
    calls ProducePlot to create a plot
    of the first column vs second column

  Args:
    filename path to file to read in
    
  Returns:
    Calls ProducePlot 

  '''
  graph_size = []
  probs = []
  with open(filename, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      graph_size.append(int(row[0]))
      probs.append(float(row[1]))

  ProducePlot(graph_size, probs)
        
def ProducePlot(graph_size, probs):
  '''
  Description:
    Creates a graph with matplotlib of the
    number of nodes in a graph vs. the 
    probability of finding a min cut.

  Args:
    graph_size list of the number of nodes in a graph
    probs list of the probabilities of finding min cut 
          with number of nodes in graph

  Returns:
    creates a file with a plot of graph_size vs probs lists
  '''
  plt.figure(1)
  plt.scatter(graph_size, probs)
  plt.title('Number of nodes in graph vs probability of finding min cut')
  plt.xlabel('Number of nodes in the graph')
  plt.ylabel('Probability of finding min cut with 10*n^2 runs')
  plt.savefig('q3_5a.png')
  
  

def main():
  '''
  Description:
    Runs Karger's algorithm on random graphs.
    Creates the plot of the number of nodes in a
    graph vs. the probability of finding a min cut.
  '''
  
  prob_min_cut = {}

  # Create random graphs of 5,...,20 nodes
  for n in range(5, 21):
  
    min_cuts_found = 0.0

    for i in range(1, (10*(n**2))+1):
  
      G = CreateGraph(n)
      #plt.figure(1)
      #DrawGraph(G, 'ps3_q5.png')

      # Get the min cut using a built in method from networkx
      min_edge_cut = len(nx.minimum_edge_cut(G))

      G = RunKarger(G)

      # See if karger's returns the correct min cut
      if G.number_of_edges() == min_edge_cut:
        min_cuts_found += 1

    # For every n node sized graph find the probability 
    # of getting the min cut each time karger's is run
    # for a total of 10*n**2 runs
    prob_min_cut[n] = float('{0:.3f}'.format(min_cuts_found/i))
    
    # Output results to a csv file
    Write('ps3_q5_output.txt', n, prob_min_cut[n])
    

  # Read in results file and create a plot of results
  ReadCSV('ps3_q5_output.txt')  

if __name__ == '__main__':
  #main()
  ReadCSV('ps3_q5_output.txt')