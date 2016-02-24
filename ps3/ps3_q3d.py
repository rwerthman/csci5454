'''
Robert Werthman
CSCI5454
Problem Set 3, Question 3, Part d

Dispense minions into k pods until all of the pods 
have at least one minion. 
'''

import random
import collections



def main():
	num_pods_per_interation = collections.OrderedDict()
	for i in xrange(1,20):
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

	print 'Number of minions dispensed: ', num_pods_per_interation

if __name__ == '__main__':
	main()