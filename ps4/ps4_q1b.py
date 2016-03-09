'''

Sources
---------
https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
  - Create and choose an element with a probability
https://web.eecs.umich.edu/~jabernet/eecs598course/fall2013/web/notes/lec4_091613.pdf
  -
https://stackoverflow.com/questions/10271484/python-element-wise-multiplication-of-two-lists
  - dot product of two lists
'''
#from numpy.random import choice
from random import random
import math
import matplotlib.pyplot as plt

def UpdateWeights(learning_rate, weights, loss_vector):
  for i in range(len(weights)):
    x = -learning_rate*loss_vector[i]
    weights[i] = weights[i]*math.exp(x)
  return weights

def GetProbilityDistribution(weights):
  # Create probabilities for each weight/column of the matrix
  probability_distribution = [(weight/sum(weights)) for weight in weights]  
  return probability_distribution

def NatureChoosesLossVector(num_actions):
  loss_vector = []
  for i in range(num_actions):
    loss_vector.append(random())
  return loss_vector 

def AlgorithmLoss(weights, loss_vector, probability_distribution):
  #algorithm_loss = 0.0
  #for i in range(len(weights)):
    #algorithm_loss += weights[i]*loss_vector[i]
  #algorithm_loss = algorithm_loss/sum(weights)
  # dot product of the probability distribution and the loss vector
  algorithm_loss = sum([i*j for (i, j) in zip(loss_vector, probability_distribution)])
  return algorithm_loss
    

def Hedge(learning_rate, rounds, num_actions):
  weights = [1.0]*num_actions
  loss_per_action = [0.0]*num_actions
  algorithm_loss = 0.0
  for t in range(rounds):
    probability_distribution = GetProbilityDistribution(weights)
    loss_vector = NatureChoosesLossVector(num_actions)
    # Keep track of the losses for each of the actions
    for i in range(len(loss_per_action)):
      loss_per_action[i] += loss_vector[i]
    # Caclulate the algorithm loss for the round
    algorithm_loss += AlgorithmLoss(weights, loss_vector, probability_distribution)
    weights = UpdateWeights(learning_rate, weights, loss_vector)
  
  regret = algorithm_loss - min(loss_per_action)
  return regret

def main():
  regrets = []
  T = []
  num_actions = 2
  for i in range(2,300,1):
    print i
    rounds = i**2
    T.append(rounds)
    #learning_rate = 1.0/math.sqrt(rounds)
    learning_rate = math.sqrt((8*math.log10(num_actions))/rounds)
  
  
    regrets.append(Hedge(learning_rate, rounds, num_actions))
 
  c1 = .5
  c2 = 0.01
  c1_T = [c1*math.sqrt(x) for x in T]
  c2_T = [c2*math.sqrt(x) for x in T]
  
  plt.figure()
  a = plt.scatter(T,regrets,color='b')
  b = plt.scatter(T,c1_T,color='g')
  c = plt.scatter(T,c2_T,color='r')
  #plt.ylim(0, 150)
  #plt.xlim(0, 70000)
  plt.title("Plot of Regret, c1*sqrt(T), c2*sqrt(T)")
  plt.legend((a,b,c),('Regret', 'c1*sqrt(T)', 'c2*sqrt(T)'), loc=2)
  plt.xlabel('Iteration')
  plt.ylabel('Regret')
  plt.savefig('q1b.png')
  

  
  

if __name__ == '__main__':
  main()