from AVLTree import AVLTree
from AVLTree import NullAVLNode

def CreateBasicTree():
  tree = AVLTree()
  tree.Insert(5) # Root node
  tree.Insert(3)
  tree.Insert(4)
  tree.Insert(6)
  tree.Insert(5.5)
  tree.Insert(7)
  tree.Insert(6.6)
  tree.Insert(6.5)
  tree.Insert(8)
  tree.Insert(2)
  tree.Insert(1)
  
  return tree

def CreateRightUnBalancedTree():
  tree = AVLTree()
  tree.Insert(3)
  tree.Insert(5)
  tree.Insert(7)

  return tree

def CreateLeftUnBalancedTree():
  tree = AVLTree()
  tree.Insert(7)
  tree.Insert(5)
  tree.Insert(3)

  return tree

def AssertInsert():
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Assert: Insert Nodes into tree' + bcolors.ENDC
  tree = CreateBasicTree()
  #tree.PrintTree(tree.root, tree.root.height)
  
  root = tree.Search(5)
  Assert('Insert method root is 5', tree.root.key == root.key)

  Assert('Insert method right child of root is 6', root.right_child.key == tree.root.right_child.key)
  Assert('Insert method left child of root is 3', root.left_child.key == tree.root.left_child.key)
  

def AssertLeftRotate():
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Assert: Left Rotate Tree' + bcolors.ENDC
  tree = CreateRightUnBalancedTree()
  #tree.PrintTree(tree.root, tree.root.height)

  tree.LeftRotate(tree.root)

  #tree.PrintTree(tree.root, tree.root.height)

  root = tree.Search(5)
  Assert('Rotate method new root node is 5', tree.root.key == root.key)
  Assert('Rotate method height of root node is 1', root.height == 1)
  
  Assert('Rotate method left child of root is 3', tree.root.left_child.key == 3)
  Assert('Rotate method right child of root is 7', tree.root.right_child.key == 7)

  Assert('Rotate method height of left child of new root is 0', tree.root.left_child.height == 0)

def AssertRightRotate():
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Assert: Right Rotate Tree' + bcolors.ENDC
  tree = CreateLeftUnBalancedTree()
  #tree.PrintTree(tree.root, tree.root.height)

  tree.RightRotate(tree.root)

  #tree.PrintTree(tree.root, tree.root.height)

  root = tree.Search(5)
  Assert('Rotate method new root node is 5', tree.root.key == root.key)
  Assert('Rotate method height of root node is 1', root.height == 1)
  
  Assert('Rotate method left child of root is 3', tree.root.left_child.key == 3)
  Assert('Rotate method right child of root is 7', tree.root.right_child.key == 7)
  
  Assert('Rotate method height of right child of new root is 0', tree.root.right_child.height == 0)


def AssertSearch():

  # Asserts for Searching a node

  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Assert: Search a node' + bcolors.ENDC
  
  tree = CreateBasicTree()

  node = tree.Search(10)
  Assert('Search method with key 10 not in tree.', isinstance(node, NullAVLNode))

  node = tree.Search(2)
  Assert('Search method with key 2 in tree.', node.key == 2)

def AssertSearchSuccessor():
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Assert: SearchSuccessor of a node' + bcolors.ENDC
  tree = CreateBasicTree()
  # tree.PrintTree(tree.root, tree.root.height)

  node = tree.Search(6)
  successor = tree.SearchSuccessor(node)
  node = tree.Search(6.5)
  Assert('Successor of 6 is 6.5.', successor is node)

  node = tree.Search(5.5)
  successor = tree.SearchSuccessor(node)
  node = tree.Search(6)
  Assert('Successor of 5.5 is 6.', successor is node)


def AssertDelete():

  #
  # Asserts for deleting a leaf node
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Assert: Delete a leaf node' + bcolors.ENDC

  tree = CreateBasicTree()
  # tree.PrintTree(tree.root, tree.root.height)

  tree.Delete(8)
  #tree.PrintTree(tree.root, tree.root.height)
  node = tree.Search(8)
  Assert('Delete method with leaf node: 8 is removed.', isinstance(node, NullAVLNode))

  tree.Delete(4)
  #tree.PrintTree(tree.root)
  node = tree.Search(4)
  Assert('Delete method with leaf node: 4 is removed.', isinstance(node, NullAVLNode))

  tree.Delete(1)
  #tree.PrintTree(tree.root, tree.root.height)
  node = tree.Search(1)
  Assert('Delete method with leaf node: 1 is removed.', isinstance(node, NullAVLNode))

  #
  # Asserts for deleting node with single child
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Assert: Delete node with single child' + bcolors.ENDC

  tree = CreateBasicTree()
  # tree.PrintTree(tree.root, tree.root.height)
  tree.Delete(2)
  # tree.PrintTree(tree.root, tree.root.height)
  node = tree.Search(2)
  Assert('Delete method with left child: 2 is removed.', isinstance(node, NullAVLNode))
  parent = tree.Search(3)
  child = tree.Search(1)
  Assert('Delete method with left child: Left child of 3 is 1.', parent.left_child is child)
  Assert('Delete method with left child: Parent of 1 is 3.', child.parent is parent)
  tree.Delete(7)
  # tree.PrintTree(tree.root, tree.root.height)
  node = tree.Search(7)
  Assert('Delete method with right child: 7 is removed.', isinstance(node, NullAVLNode))
  parent = tree.Search(6)
  child = tree.Search(6.5)
  Assert('Delete method with right child: Right child of 6 is 6.5.', parent.right_child is child)
  Assert('Delete method with right child: Parent of 6.5 is 6.', child.parent is parent)

  node = tree.Search(6.6)
  child = tree.Search(5.5)

  Assert('Delete method with right child: right child of 5.5 is 6.6.', child.right_child is node)  
  Assert('Delete method with right child: Height of 5.5 is 3.', child.height == 3)


  #
  # Asserts for deleting node with both children
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Assert: Delete node with two children' + bcolors.ENDC

  tree = CreateBasicTree()
  #tree.PrintTree(tree.root, tree.root.height)

  tree.Delete(6)
  #tree.PrintTree(tree.root, tree.root.height)

  node = tree.Search(6)
  Assert('Delete method with both children: 6 no longer exists.', isinstance(node, NullAVLNode))
  parent = tree.Search(5)
  child = tree.Search(6.5)
  Assert('Delete method with both children: Right child of 5 is 6.5.', parent.right_child is child)
  Assert('Delete method with both children: Parent of 6.5 is 5', child.parent is parent)

  parent = tree.Search(6.5)
  child = tree.Search(5.5)
  Assert('Delete method with both children: Left child of 6.5 is 5.5.', parent.left_child is child)
  Assert('Delete method with both children: Parent of 5.5 is 6.5.', child.parent is parent)

  parent = tree.Search(6.5)
  child = tree.Search(7)
  Assert('Delete method with both children: Right child of 6.5 is 7.', parent.right_child is child)
  Assert('Delete method with both children: Parent of 7 is 6.5.', child.parent is parent)

  #
  # Asserts for deleting node with both children
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Assert: Delete root node' + bcolors.ENDC
  tree = CreateBasicTree()
  #tree.PrintTree(tree.root, tree.root.height)
  tree.Delete(5)
  #tree.PrintTree(tree.root, tree.root.height)
  n = tree.Search(5.5)

  Assert('Delete method with root: 5.5 is new root.', tree.root.key == n.key)
  Assert('Delete method with root: height of 5.5 is now 4.', n.height == 4)
  Assert('Delete method with root: parent of 5.5 is none.', isinstance(n.parent, NullAVLNode))
  Assert('Delete method with root: right child of 5.5 is 6.', n.right_child.key == 6)
  Assert('Delete method with root: left child of 5.5 is 3.', n.left_child.key == 3)
  

def AssertUpdateHeightAndBalance():
	#
  # Asserts for updating the heights in a tree after a deletion of a node
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Assert: UpdateHeightAndBalances after node is deleted' + bcolors.ENDC
  tree = CreateBasicTree()
  #tree.PrintTree(tree.root, tree.root.height)
  tree.Delete(6)
  #tree.PrintTree(tree.root, tree.root.height)

  n = tree.Search(6.5)
  Assert('Height of node with key 6.5 should be 2.', n.height == 2)

  n = tree.Search(7)
  Assert('Height of node with key 7 should be 1.', n.height == 1)

  n = tree.Search(5.5)
  Assert('Height of node with key 5.5 should be 0.', n.height == 0)

  n = tree.root
  Assert('Height of root node should be 3.', n.height == 3)

  n = tree.Search(4)
  Assert('Height of node with key 4 should be 0.', n.height == 0)

def AssertBalance():
  
  # Asserts for balancing a tree
  
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Assert: Balance left heavy child tree' + bcolors.ENDC
 
  tree = AVLTree()
  tree.Insert(7)
  tree.Insert(5)
  tree.Insert(6)

  #tree.PrintTree(tree.root, tree.root.height)

  parent = tree.Search(6)
  n = tree.Search(7)
  Assert('Right child of 6 should be 7', parent.right_child is n)
  Assert('7 should have 6 as the parent', n.parent is parent)
  Assert('Height of 7 should be 0', n.height == 0)

  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Assert: Balance left heavy child tree' + bcolors.ENDC

  tree = AVLTree()
  tree.Insert(3)
  tree.Insert(5)
  tree.Insert(4)
  #tree.PrintTree(tree.root, tree.root.height)

  root = tree.Search(4)
  n = tree.Search(5)
  Assert('Right child of 4 should be 5', root.right_child is n)
  Assert('5 should have 4 as the parent', n.parent is root)
  Assert('Height of 5 should be 0', n.height == 0)
  Assert('Root of tree should be 4', tree.root is root)

  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Assert: Balance large tree insert' + bcolors.ENDC
  # Insert: 9, 4, 1, 2, 8, 6, 5, 7, 10, 11, 12

  tree = AVLTree()
  tree.Insert(9)
  tree.Insert(4)
  tree.Insert(1)
  tree.Insert(2)
  tree.Insert(8)
  tree.Insert(6)
  tree.Insert(5)
  tree.Insert(7)
  tree.Insert(10)
  tree.Insert(11)
  tree.Insert(12)

  #tree.PrintTree(tree.root, tree.root.height)

  root = tree.Search(8)
  Assert('Root should be 8', root is tree.root)
  Assert('Root should have a height of 4', root.height == 3)

  n = tree.Search(7)
  Assert('7 should have null avl nodes as children', (isinstance(n.right_child, NullAVLNode) and isinstance(n.left_child, NullAVLNode)))
  a = tree.Search(6)
  b = tree.Search(4)
  Assert('The parent of 7 should be 6', n.parent is a)
  Assert('The parent of 6 should be 4', a.parent is b)

  c = tree.Search(10)
  d = tree.Search(11)
  e = tree.Search(9)
  Assert('10 should have children 11 and 9', c.left_child is e and c.right_child is d)
  Assert('The height of 10 should be 2', c.height == 2)
  

  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Assert: Balance large tree delete' + bcolors.ENDC
  # Delete: 9, 10, 12, 2
  tree.Delete(9)
  tree.Delete(10)
  tree.Delete(12)
  tree.Delete(2)

  # tree.PrintTree(tree.root, tree.root.height)

  root = tree.Search(6)
  a = tree.Search(4)
  b = tree.Search(8)
  c = tree.Search(7)
  Assert('Root should be 6', tree.root is root)
  Assert('Height of root should be 2', root.height == 2)
  Assert('Children of root should be 4 and 8', root.left_child is a and root.right_child is b)
  
  Assert('7 should have null avl nodes as children', (isinstance(n.right_child, NullAVLNode) and isinstance(n.left_child, NullAVLNode)))
  Assert('7 parent should be 8', c.parent is b)
  

  

class bcolors:
  HEADER = '\033[95m' # Purple
  OKBLUE = '\033[94m' # Blue
  OKGREEN = '\033[92m' # Green
  WARNING = '\033[93m' # Yellow
  FAIL = '\033[91m' # Red
  ENDC = '\033[0m' # Black
  BOLD = '\033[1m' # Bold
  UNDERLINE = '\033[4m' # Underline

def Assert(AssertName, test):
  if test:
    print bcolors.OKGREEN + AssertName + " Passed." + bcolors.ENDC
  else:
    print bcolors.FAIL + AssertName + " Failed." + bcolors.ENDC


def main():
  AssertSearch()
  AssertSearchSuccessor()
  AssertDelete()
  AssertUpdateHeightAndBalance()
  AssertInsert()
  AssertLeftRotate()
  AssertRightRotate()
  AssertBalance()


if __name__ == '__main__':
  main()