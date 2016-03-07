
class Expert(object):
  def __init__(self):
    self.weight = 0

def Hedge(experts, learning_rate):
  # Initialize weights for each expert to 1
  for expert in experts:
    expert.weight = 1

def main():
  # Number of experts
  num_experts = 10
  # Create a list of experts
  experts = [None]*num_experts
  for i in range(num_experts):
    experts[i] = Expert()
  
  print len(experts)
  

if __name__ == '__main__':
  main()