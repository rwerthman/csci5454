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
	
    # Check if the tree is empty
    if self.root is None:
      print 'Find: Tree is empty.'
      return

    current_node = self.root # Start looking for the key at the root node

    while current_node is not None:
      if key == current_node.key:
        return current_node
      elif key < current_node.key:
        current_node = current_node.left_child
      else:
        current_node = current_node.right_child
    return None





  def Delete(self, key):

    # Check if the tree is empty
    if self.root is None:
      print 'Delete: Tree is empty.'
      return

    # Node to be removed
    r_node = self.Find(key)

    if r_node is None:
    	print 'Delete: Key not found in tree.'
    	return

    # If the key is found in a leaf node
    if r_node.right_child is None and r_node.left_child is None:
    	# Check the which child the leaf node belongs to and delete it
    	self.Transplant(r_node, None)
      
    # If the key is found in a node with only a left child
    elif r_node.right_child is None and r_node.left_child is not None:
      self.Transplant(r_node, r_node.left_child)

    # If the key is found in a node with only a right child
    elif r_node.right_child is not None and r_node.left_child is None:
      self.Transplant(r_node, r_node.right_child)

    # If the key is found in a node with both a left and a right child
    else:
      successor = self.FindSuccessor(r_node)

      # Check if the successor is not the right child of the node we are deleting
      if successor.parent is not r_node:
      	self.Transplant(successor, successor.right_child)
      	successor.right_child = r_node.right_child
      	successor.right_child.parent = successor

      self.Transplant(r_node,successor)
      successor.left_child = r_node.left_child
      successor.left_child.parent = successor



  def FindSuccessor(self, node):
  	if node.right_child is not None:
  		# Set node to its right child
  		node = node.right_child
  		while node.left_child is not None:
  			node = node.left_child
  		return node


  def Transplant(self, node, node_child):
    # Check which child of the parent the current node belongs to

    # If the node we are looking at is a leaf node no transplant necessary
    if node_child is None:
      if node.parent.right_child is node:
        node.parent.right_child = None
      else:
        node.parent.left_child = None
    # If the node is the parent's right child
    elif node.parent.right_child is node:
    	# Set the parent's right child to the child of the node
      node.parent.right_child = node_child
      # Set the child's of the node to it the node's parent
      node_child.parent = node.parent
    # If the node is the parent's left child
    else:
    	# Set the parent's right child to the child of the node
      node.parent.left_child = node_child
      # Set the child's of the node to it the node's parent
      node_child.parent = node.parent

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

  def UpdateHeights(self):
  	pass

  def Balance(self):
  	pass


class AVLNode(object):

  def __init__(self, key):
	self.left_child = None
	self.right_child = None
	self.parent = None
	self.key = key
	self.height = 0
