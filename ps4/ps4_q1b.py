'''

Sources
---------
https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
  - 
https://web.eecs.umich.edu/~jabernet/eecs598course/fall2013/web/notes/lec4_091613.pdf
  -
'''
from numpy.random import choice
from random import random
import math

def UpdateWeights(learning_rate, weights, loss_vector):
  for i in range(len(weights)):
    x = -learning_rate*loss_vector[i]
    weights[i] = weights[i]*math.exp(x)
  return weights

def ChooseAction(weights):
  # The AI can choose a column in the matrix
  actions = [i for i in range(len(weights))]
  # Create probabilities for each weight/column of the matrix
  probability_distribution = [(weight/sum(weights)) for weight in weights]
  # Choose action/column according to the distribution
  action = choice(actions, p=probability_distribution)
  return action, probability_distribution

def NatureChoosesLossVector(num_actions):
  loss_vector = []
  for i in range(num_actions):
    loss_vector.append(random())
  return loss_vector 

def AlgorithmLoss(weights, loss_vector):
  algorithm_loss = 0.0
  for i in range(len(weights)):
    algorithm_loss += weights[i]*loss_vector[i]
  algorithm_loss = algorithm_loss/sum(weights)
  return algorithm_loss
    

def Hedge(learning_rate, rounds, num_actions):
  weights = [1.0]*num_actions
  total_min_loss = 0.0
  algorithm_loss = 0.0
  for t in range(rounds):
    print '##########'
    print 'Round', t
    print '##########'
    # Have nature create a random loss vector
    loss_vector = NatureChoosesLossVector(num_actions)
    # Choose the smallest loss out of all of the actions
    total_min_loss += min(loss_vector)
    # Caclulate the algorithm loss for the round
    algorithm_loss += AlgorithmLoss(weights, loss_vector)
    weights = UpdateWeights(learning_rate, weights, loss_vector)
    print 'Weight vector', weights   
    print 'Loss vector', loss_vector
    print 'Total minimum loss', total_min_loss
    print 'Total algorithm loss', algorithm_loss
   
  
  regret = algorithm_loss - total_min_loss
  print 'Total regret', regret

def main():
  
  rounds = 400
  learning_rate = 1.0/math.sqrt(rounds)
  num_actions = 2
  
  
  Hedge(learning_rate, rounds, num_actions)

  
  

if __name__ == '__main__':
  main()