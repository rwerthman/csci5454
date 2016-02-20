class AVLTree(object):

	def __init__(self):
		self.root = None

	def insert(self, key):
		'''
		Insert a key into an AVL tree

		'''

		new_node = AVLNode(key) # Create a new node with the key argument of insert

		parent_node = None # This will be used to store the parent node
		current_node = self.root # Start the insert at root of the tree

		# If there are nodes in the tree
		while current_node is not None:

			parent_node = current_node # Set y to the parent node

			# Insert into the left part of the tree if the key of the new node 
			# is less than the key of the current node we are looking at
			if new_node.key < current_node.key: 
				current_node = current_node.left_child
			else:
				# Insert into the right part of the tree
				# if the key of the new node is less than
				# the key of the current node we are looking at
				current_node = current_node.right_child

		new_node.parent = parent_node # Set the parent node of the new node

		# Set the root node of the tree to the new node
		# since the tree is empty
		if parent_node is None:
			self.root = new_node
		# Set the left child of the parent node to the new node
		elif new_node.key < parent_node.key:
			new_node.height = parent_node.height + 1 # Set the height of the new node
			parent_node.left_child = new_node
		# Set the right child of the parent to the new node
		else:
			new_node.height = parent_node.height + 1 # Set the height of the new node
			parent_node.right_child = new_node

		# TODO: Need to balance the tree after an insert



	def search(self):
		pass

	def delete(self):
		pass

	def print_tree(self, current_node):

		if self.root is None:
			print 'Tree is empty.'
			return

		if current_node is not None:

			# Print the right side of the parent
			if current_node.right_child is not None:
				self.print_tree(current_node.right_child)
				print '\t' * current_node.height + '    /'

			# Print the parent node
			print '\t' * current_node.height + str(current_node.key)

			# Print the left side of the parent
			if current_node.left_child is not None:
				print '\t' * current_node.height + '    \\'
				self.print_tree(current_node.left_child)





class AVLNode(object):

	def __init__(self, key):
		self.left_child = None
		self.right_child = None
		self.parent = None
		self.key = key
		self.height = 0
