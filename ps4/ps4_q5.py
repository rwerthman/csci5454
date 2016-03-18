'''
Robert Werthman
CSCI 5454
PS4 Question 5
'''

import numpy as np
import math


def UpdateWeights(learning_rate, weights, loss_vector):
  weights_size = weights.shape[0]
  for i in range(weights_size):
    x = -learning_rate*loss_vector[i]
    weights[i] = weights[i]*math.exp(x)
  return weights

def GetProbilityDistribution(weights):
  weights_size = weights.shape[0]
  probability_distribution = np.ones((weights_size,1), dtype=np.float64)
  for i in range(weights_size):
    probability_distribution[i] = weights[i]/np.sum(weights)
  return probability_distribution

def ChooseAction(weights):
  probability_distribution = GetProbilityDistribution(weights)
  reshaped_distribution = np.reshape(probability_distribution, weights.shape[0])
  actions = np.arange(weights.shape[0])
  action = np.random.choice(actions, p=reshaped_distribution)
  return action, probability_distribution

def Hedge():
  # Initialize pay off matrix
#   M = np.array([[ 0, 1,-1],
#                 [-1, 0, 1],
#                 [ 1,-1, 0]])
  
  M = np.array([[1,0,1,8,0],
                [5,8,9,2,1],
                [0,1,8,0,5],
                [8,9,2,1,0],
                [1,8,0,5,8]])
#   M = np.array([[1,2],
#                 [1,2]])
    
  # The number of times hedge will run to find the nash equilibrium
  T = 25
  
  weights_size = M.shape[0]
  row_weights = np.ones((weights_size,1))
  column_weights = np.ones((weights_size,1))
  learning_rate = 1.0/math.sqrt(T)
  
  row_payoff = np.zeros((weights_size,1))
  column_payoff = np.zeros(weights_size)
  
  print 'initial row weights', row_weights
  print 'initial column weights', column_weights
  print 'initial learning rate', learning_rate
  print 'initial row payoff', row_payoff
  print 'initial column payoff', column_payoff
  
  for t in range(T):
    print '##########'
    print 'Round', t
    print '##########'
    
    row_action, row_distribution =  ChooseAction(row_weights)
    column_action, column_distribution =  ChooseAction(column_weights)
    
    print 'row distribution', row_distribution.T
    print 'column distribution', column_distribution
    
    row_loss = M.dot(column_distribution)
    column_loss = (row_distribution.T).dot(M)
    
    # Iteratively calculate the vector of expected payoffs
    # for each player.  Every entry should sum to 0.
    row_payoff = np.add(row_payoff, (row_distribution.T).dot(row_loss))
    column_payoff = np.subtract(column_payoff, column_loss.dot(column_distribution))
    
    print 'row payoff', row_payoff
    print 'column payoff', column_payoff
    
    print 'row loss', row_loss
    print 'column loss', column_loss
    
    row_nash_equalibrium = (row_distribution.T).dot(row_loss)
    column_nash_equalibrium = column_loss.dot(column_distribution)
    
#     print 'nash equalibrium found by row', row_nash_equalibrium
#     print 'nash equalibrium found by column', column_nash_equalibrium
    
    
    
    
    row_weights = UpdateWeights(learning_rate, row_weights, row_loss)
    column_weights = UpdateWeights(learning_rate, column_weights, column_loss.T)
        
#     print 'updated row weights', row_weights
#     print 'updated column weights', column_weights
    
  print 'time-averaged expected payoff row', row_nash_equalibrium/T
  print 'time-averaged expected payoff column', column_nash_equalibrium/T
    

def main():
  Hedge()

if __name__ == '__main__':
  main()
  