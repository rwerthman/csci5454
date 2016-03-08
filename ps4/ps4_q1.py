'''

Sources
---------
https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
  - 
https://web.eecs.umich.edu/~jabernet/eecs598course/fall2013/web/notes/lec4_091613.pdf
  -
'''
from numpy.random import choice
from random import randint
import math

def ChooseAction(weights):
  # The AI can choose a column in the matrix
  actions = [i for i in range(len(weights))]
  # Create probabilities for each weight/column of the matrix
  probability_distribution = [(weight/sum(weights)) for weight in weights]
  # Choose action/column according to the distribution
  action = choice(actions, p=probability_distribution)
  return action, probability_distribution

def UpdateWeights(learning_rate, weights, loss_vector):
  for i in range(len(weights)):
    x = -learning_rate*loss_vector[i]
    weights[i] = weights[i]*math.exp(x)
  return weights

def UpdateScores(ai_score, ai_action, user_score, user_action, payoff_matrix):
  old_ai_score = ai_score
  ai_score = old_ai_score - payoff_matrix[user_action][ai_action]
  print 'old AI score', old_ai_score, ', new AI score', ai_score, ', difference', \
        ai_score - old_ai_score
  
  old_user_score = user_score
  user_score = old_user_score + payoff_matrix[user_action][ai_action]
  print 'old user score', old_user_score, ', new user score', user_score, ', difference', \
        user_score - old_user_score
        
  return ai_score, user_score

def Hedge(learning_rate, payoff_matrix, rounds):
  user_score = 0.0
  ai_score = 0.0
  weights = [1.0]*len(payoff_matrix[0])
  for t in range(rounds):
    print '##########'
    print 'Round', t
    print '##########'
    # Take in row of the payoff matrix from user
    user_action = int(input('Enter the row you wish to choose: '))
    print 'Action chosen by user', user_action
    # Get the column the AI will choose
    ai_action, probability_distribution = ChooseAction(weights)
    print 'Probability distribution of AI actions', probability_distribution
    print 'Action chosen by AI', ai_action
    # The loss vector is the row that is chosen by the user
    loss_vector = payoff_matrix[user_action]
    print 'AI loss vector', loss_vector
    # Update the weights for each column based on 
    # how much was lost for each column
    weights = UpdateWeights(learning_rate, weights, loss_vector)
    print 'AI weight vector', weights
    # Calculate the scores for the user and ai after this round
    ai_score, user_score = UpdateScores(ai_score, ai_action, user_score, user_action, payoff_matrix)
    
  

def main():
  
  payoff_matrix = [[randint(-10,10),randint(-10,10),randint(-10,10)],
                   [randint(-10,10),randint(-10,10),randint(-10,10)],
                   [randint(-10,10),randint(-10,10),randint(-10,10)]
                  ]
  rounds = 3
  learning_rate = 1.0
  
  print 'Payoff Matrix'
  for row in payoff_matrix:
    print row
  
  Hedge(learning_rate, payoff_matrix, rounds)

  
  

if __name__ == '__main__':
  main()