class AVLTree(object):

	def __init__(self):
		self.root = None

	def Insert(self, key):
		'''
		Insert a key into an AVL tree

		Args:
		  self
		  key 

		Returns:

		Sources:
		  Introduction to Algorithms, Third Edition (page 294)
		    - Non-recursive insert of a node into a binary tree

		'''

		# Create a new node with the key argument of insert
		new_node = AVLNode(key) 

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
		# if the tree is empty
		if parent_node is None:
			self.root = new_node
		# Set the left child of the parent node to the new node
		elif new_node.key < parent_node.key:
			# Set the height of the new node
			new_node.height = parent_node.height + 1 
			parent_node.left_child = new_node
		# Set the right child of the parent to the new node
		else:
			# Set the height of the new node
			new_node.height = parent_node.height + 1 
			parent_node.right_child = new_node

		# TODO: Need to balance the tree after an insert



	def Find(self, key):
		'''

		'''		
		# Check if the tree is empty
		if self.root is None:
			print 'Find: Tree is empty.'
			return

		current_node = self.root # Start looking for the key at the root node

		while current_node is not None:
			if key == current_node.key:
				return current_node
			if key < current_node.key:
				current_node = current_node.left_child
			else:
				current_node = current_node.right_child

		return None





	def Delete(self, key):
		'''


		'''

		# Check if the tree is empty
		if self.root is None:
			print 'Delete: Tree is empty.'
			return

		current_node = self.Find(key)

		# If the key is found in a leaf node
		if current_node.right_child is None and current_node.left_child is None:
			# Check the which child the leaf node belongs to and delete it
			if current_node.parent.right_child is current_node:
				current_node.parent.right_child = None
			else:
				current_node.parent.left_child = None


		

	def PrintTree(self, current_node):
		'''

		Description:

		Args:

		Returns:

		Sources: 
		  https://stackoverflow.com/questions/20242479/printing-a-tree-data-
		  												structure-in-python
		    - How to print a tree data structure that is understandable
		'''

		# Check if the tree is empty
		if self.root is None:
			print 'PrintTree: Tree is empty.'
			return

		if current_node is not None:

			# Print the right side of the parent
			if current_node.right_child is not None:
				self.PrintTree(current_node.right_child)
				print '\t' * current_node.height + '    /'

			# Print the parent node
			print '\t' * current_node.height + str(current_node.key)

			# Print the left side of the parent
			if current_node.left_child is not None:
				print '\t' * current_node.height + '    \\'
				self.PrintTree(current_node.left_child)





class AVLNode(object):

	def __init__(self, key):
		self.left_child = None
		self.right_child = None
		self.parent = None
		self.key = key
		self.height = 0
