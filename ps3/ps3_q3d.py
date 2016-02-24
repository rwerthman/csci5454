'''
Robert Werthman
CSCI5454
Problem Set 3, Question 3, Part d

Dispense minions into k pods until all of the pods 
have at least one minion. 
'''

import random
import collections
import matplotlib.pyplot as plt
import math


def DispenseMinions():
	num_pods_per_interation = collections.OrderedDict()
	for i in xrange(1,30):
		num_pods_per_interation[i*100] = 0
	for num_pods in num_pods_per_interation:
		# Create a pod object that holds the pods
		pod_container = {}
		# Initialize all of the pods to empty (0)
		for i in xrange(0,num_pods):
			pod_container[i] = 0
		# Count the number of minions we have to insert before
		# the pods have at least one minion
		num_minions_dispensed = 0
		# Add minions (integers) to the pods until each pod
		# has at least one minion
		while True:
			num_minions_dispensed = num_minions_dispensed + 1
			# Choose a random pod to insert a minion
			pod_number = random.randint(0,num_pods)
			# Insert the minion in the random pod
			pod_container[pod_number] = 1
			# If all of the pods have at least 1 minion leave the loop
			if len(set(pod_container.values())) == 1:
				break
		num_pods_per_interation[num_pods] = num_minions_dispensed
	return num_pods_per_interation

def GraphOutput(pods_with_num_minions):

	# Create two lists of the number of pods 
	# and the number of minions dispensed for
	# each number of pods
	num_pods = []
	num_minions = []
	for k,v in pods_with_num_minions.items():
		num_pods.append(k)
		num_minions.append(v)

	# Plot c1*f(x) and c2*f(x) where f(x) = xlog(x)
	# c1 and c2 are constants and x is the number of pods per iteration
	c1 = 1.5
	c2 = .5
	num_pods_log_c1 = [c1*(x*math.log(x)) for x in num_pods]
	num_pods_log_c2 = [c2*(x*math.log(x)) for x in num_pods]

	plt.figure()
	a = plt.scatter(num_pods, num_minions, color='b')
	b = plt.scatter(num_pods, num_pods_log_c1, color='r')
	c = plt.scatter(num_pods, num_pods_log_c2, color='g')
	plt.ylim(0, 40000)
	plt.xlim(0, 3000)
	plt.title("Numerical Plot of 3c, c1f(k), c2f(k)")
	plt.legend((a,b,c),('3c', 'c1f(k)', 'c2f(k)'), loc=2)
	plt.savefig('q3_3d.png')

def main():

	pods_with_num_minions = DispenseMinions()
	GraphOutput(pods_with_num_minions)

if __name__ == '__main__':
	main()