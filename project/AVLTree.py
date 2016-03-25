'''

Sources:
---------
  Introduction to Algorithms, Third Edition (page 294)
    - Insert, rotate, delete, Search successor methods of binary tree
  https://stackoverflow.com/questions/20242479/printing-a-tree-data-structure-in-python
    - How to print a tree data structure that is understandable
  https://www.youtube.com/watch?v=FNeL18KsWPc
    - MIT video lecture on AVL trees
  https://en.wikipedia.org/wiki/AVL_tree
    - AVL Tree cases
  https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
    - Visualization of an avl tree for creating my tests
'''


class AVLTree(object):


  def __init__(self):
    self.root = NullAVLNode()
  

  def Insert(self,key): 
    # Create a new node with the key argument of insert
    new_node = AVLNode(key) 

    parent_node = NullAVLNode() # This will be used to store the parent node
    current_node = self.root # Start the insert at root of the tree

    # If there are nodes in the tree
    while not isinstance(current_node, NullAVLNode):

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
    if isinstance(parent_node, NullAVLNode):
      self.root = new_node
    # Set the left child of the parent node to the new node
    elif new_node.key < parent_node.key:
    # Set the height of the new node
      parent_node.left_child = new_node
    # Set the right child of the parent to the new node
    else:
    # Set the height of the new node
      parent_node.right_child = new_node

    # Update heights of the new node and the nodes above it
    self.UpdateHeightAndBalance(new_node)

    # TODO: Need to balance the tree after an insert
    self.UpdateBalance(new_node)


  def Search(self, key):
  
    # Check if the tree is empty
    if isinstance(self.root, NullAVLNode):
      print 'Search: Tree is empty.'
      return

    node = self.root # Start looking for the key at the root node

    while not isinstance(node, NullAVLNode):
      # If we Search the a node that has the same key we are looking for
      # return it
      if key == node.key:
        return node
      elif key < node.key:
        node = node.left_child
      else:
        node = node.right_child
    # If we don't Search a node in the tree with the
    # key we are looking for return empty node
    return NullAVLNode()

  def Delete(self, key):

    # Check if the tree is empty
    if isinstance(self.root, NullAVLNode):
      print 'Delete: Tree is empty.'
      return

    # Node to be removed
    node = self.Search(key)

    if isinstance(node, NullAVLNode):
      print 'Delete: Key not found in tree.'
      return

    # If the key is found in a leaf node
    if isinstance(node.right_child, NullAVLNode) and isinstance(node.left_child, NullAVLNode):
      # Check the which child of the parent the leaf node belongs to and delete it
      if node.parent.right_child is node:
        node.parent.right_child = NullAVLNode()
      else:
        node.parent.left_child = NullAVLNode()
      
      self.UpdateHeightAndBalance(node.parent)
    # If the key is found in a node with only a left child
    # Left child takes the nodes place
    elif not isinstance(node.left_child, NullAVLNode) and isinstance(node.right_child, NullAVLNode):
      self.Transplant(node, node.left_child)
      self.UpdateHeightAndBalance(node.left_child)

    # If the key is found in a node with only a right child
    # Right child takes the nodes place
    elif not isinstance(node.right_child, NullAVLNode) and isinstance(node.left_child, NullAVLNode):
      self.Transplant(node, node.right_child)
      self.UpdateHeightAndBalance(node.right_child)

    # If the key is found in a node with both a left and a right child
    # Successor node takes the nodes place
    else:
      successor = self.SearchSuccessor(node)

      # Choose the correct node to start the height update 
      # from after removing a node
      x = None
      if successor.parent is not node:
        x = successor.parent
      else:
        x = successor

      # Check if the successor is not the right child of the node we are deleting
      # This means we have to traverse down the left tree of the right child
      # to Search the successor to the node we are deleting
      if successor.parent is not node:
        # Move the right child of the successor into the successor's place
        self.Transplant(successor, successor.right_child)
        # Move successor into place of the node we are deleting
        # Set the successor's right child to the right child 
        # of the node we are deleting
        successor.right_child = node.right_child
        # Set the node's right child parent to the successor
        successor.right_child.parent = successor

      # Move the successor into the node we are going to remove's place
      self.Transplant(node,successor)
      # Set the left child of the successor to the node's left child
      successor.left_child = node.left_child
      # Set the parent of the left child to the successor
      successor.left_child.parent = successor
      
      self.UpdateHeightAndBalance(x)


  def SearchSuccessor(self, node):
    # Set node to its right child
    node = node.right_child
    while not isinstance(node.left_child, NullAVLNode):
      # Traverse down left side of right child
      # to Search successor at the end
      node = node.left_child
    return node


  def Transplant(self, node, node_successor):
    # If the node we are deleting is the root
    # The root is now the child of that node (could be none)
    if isinstance(node.parent, NullAVLNode):
       self.root = node_successor

    # Check which child of the parent the current node we want to delete belongs to
    # If the node is the parent's right child
    elif node.parent.right_child is node:
      # Set the parent's right child to the child of the node to be deleted
      node.parent.right_child = node_successor

    # If the node is the parent's left child
    else:
      # Set the parent's right child to the child of the node to be deleted
      node.parent.left_child = node_successor

    # Set the parent of node that will take over
    # the deleted nodes position
    if not isinstance(node_successor, NullAVLNode):
      node_successor.parent = node.parent


  def PrintTree(self, current_node, depth):
    
    # Check if the tree is empty
    if isinstance(self.root, NullAVLNode):
      print 'PrintTree: Tree is empty.'
      return

    if not isinstance(current_node, NullAVLNode):

       # Print the left side of the parent
      if not isinstance(current_node.left_child, NullAVLNode):
        self.PrintTree(current_node.left_child, depth-1)
        print '\t' * (depth-1) + '    \\'
      
      # Print the parent node
      print '\t' * depth + str(current_node.key) + '(' + str(current_node.height) + ')'

      # Print the right side of the parent
      if not isinstance(current_node.right_child, NullAVLNode):
        print '\t' * (depth-1) + '    /'
        self.PrintTree(current_node.right_child, depth-1)


  def UpdateHeightAndBalance(self, node):

    # Check if the tree is empty
    if isinstance(self.root, NullAVLNode):
      print 'UpdateHeightAndBalance: Tree is empty.'
      return

    self.UpdateBalance(node)

    # Calculate the height by taking the maximum height of the children
    # and adding 1
    node.height = max(node.left_child.height, node.right_child.height) + 1

    if not isinstance(node.parent, NullAVLNode):
      self.UpdateHeightAndBalance(node.parent)

        	
  def LeftRotate(self,x):
    # Check if the tree is empty
    if isinstance(self.root, NullAVLNode):
      print 'LeftRotate: Tree is empty.'
      return
    
    y = x.right_child
    x.right_child = y.left_child
    
    if not isinstance(y.left_child, NullAVLNode):
      y.left_child.parent = x
    
    y.parent = x.parent

    if isinstance(x.parent, NullAVLNode):
      self.root = y
    elif x.parent.left_child is x:
      x.parent.left_child = y
    elif x.parent.right_child is x:
      x.parent.right_child = y

    y.left_child = x
    x.parent = y

    x.height = max(x.left_child.height, x.right_child.height) + 1


  def RightRotate(self,y):
    # Check if the tree is empty
    if isinstance(self.root, NullAVLNode):
      print 'RightRotate: Tree is empty.'
      return
    
    x = y.left_child
    y.left_child = x.right_child

    if not isinstance(x.right_child, NullAVLNode):
       x.right_child.parent = y

    x.parent = y.parent

    if isinstance(y.parent, NullAVLNode):
      self.root = x
    elif y is y.parent.left_child:
      y.parent.left_child = x
    elif y is y.parent.right_child:
      y.parent.right_child = x

    x.right_child = y
    y.parent = x
    
    y.height = max(y.left_child.height, y.right_child.height) + 1


  def UpdateBalance(self, x):
    if abs(x.left_child.height - x.right_child.height) <= 1:
      pass
    # Left heavy child sub tree
    elif x.left_child.height > x.right_child.height:
      y = x.left_child
      if y.left_child.height < y.right_child.height:
        self.LeftRotate(y)
      self.RightRotate(x)
    # Right heavy child sub tree
    elif x.left_child.height < x.right_child.height:
      y = x.right_child
      if y.left_child.height > y.right_child.height:
        self.RightRotate(y)
      self.LeftRotate(x)


class AVLNode(object):

  
  def __init__(self, key):
    self.left_child = NullAVLNode()
    self.right_child = NullAVLNode()
    self.parent = NullAVLNode()
    self.key = key
    self.height = 0


class NullAVLNode(object):


  def __init__(self):
    self.key = 'null'
    self.height = -1
