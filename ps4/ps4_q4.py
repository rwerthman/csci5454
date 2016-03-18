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
  M = np.array([[ 0, 1,-1],
                [-1, 0, 1],
                [ 1,-1, 0]])
    
  # The number of times hedge will run to find the nash equilibrium
  rounds = 3
  
  weights_size = M.shape[0]
  row_weights = np.ones((weights_size,1))
  column_weights = np.ones((weights_size,1))
  
  learning_rate = 1.0/math.sqrt(rounds)
  
  print 'initial row weights', row_weights
  print 'initial column weights', column_weights
  print 'initial learning rate', learning_rate
  
  for t in range(rounds):
    print '##########'
    print 'Round', t
    print '##########'
    
    row_action, row_distribution =  ChooseAction(row_weights)
    column_action, column_distribution =  ChooseAction(column_weights)
    
    print 'row distribution', row_distribution.T
    print 'column distribution', column_distribution
    
    row_loss = M.dot(column_distribution)
    column_loss = (row_distribution.T).dot(M)
    
    row_nash_equalibrium = (row_distribution.T).dot(row_loss)
    column_nash_equalibrium = column_loss.dot(column_distribution)
    
    print 'nash equalibrium found by row', row_nash_equalibrium
    print 'nash equalibrium found by column', column_nash_equalibrium
    
    
    print 'row loss', row_loss
    print 'column loss', column_loss
    
    row_weights = UpdateWeights(learning_rate, row_weights, row_loss)
    column_weights = UpdateWeights(learning_rate, column_weights, column_loss.T)
        
    print 'update row weights', row_weights
    print 'update column weights', column_weights
    

def main():
  Hedge()

if __name__ == '__main__':
  main()
  