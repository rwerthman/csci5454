
from AVLTree import AVLTree

def CreateTree():
  tree = AVLTree()

  tree.Insert(5) # Root node

  tree.Insert(3)
  tree.Insert(4)
  tree.Insert(6)
  tree.Insert(5.5)
  tree.Insert(7)
  tree.Insert(6.5)
  tree.Insert(8)
  tree.Insert(2)
  tree.Insert(1)

  return tree


def TestFind():

	#
  # Tests for finding a node
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: Find a node' + bcolors.ENDC
  
  tree = CreateTree()

  node = tree.Find(10)
  Test('Find method with key 10 not in tree.', node is None)

  node = tree.Find(2)
  Test('Find method with key 2 in tree.', node.key == 2)

def TestFindSuccessor():
	print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: FindSuccessor of a node' + bcolors.ENDC
	tree = CreateTree()
	#tree.PrintTree(tree.root)

	node = tree.Find(6)
	successor = tree.FindSuccessor(node)
	node = tree.Find(6.5)
	Test('Successor of 6 is 6.5.', successor is node)

	node = tree.Find(5)
	successor = tree.FindSuccessor(node)
	node = tree.Find(5.5)
	Test('Successor of 5 is 5.5.', successor is node)


def TestDelete():

  #
  # Tests for deleting a leaf node
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: Delete a leaf node' + bcolors.ENDC

  tree = CreateTree()

  tree.Delete(8)
  #tree.PrintTree(tree.root)
  node = tree.Find(8)
  Test('Delete method with leaf node: 8 is removed.', node is None)

  tree.Delete(4)
  #tree.PrintTree(tree.root)
  node = tree.Find(4)
  Test('Delete method with leaf node: 4 is removed.', node is None)

  tree.Delete(1)
  #tree.PrintTree(tree.root)
  node = tree.Find(1)
  Test('Delete method with leaf node: 1 is removed.', node is None)

  #
  # Tests for deleting node with single child
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: Delete node with single child' + bcolors.ENDC

  tree = CreateTree()
  tree.Delete(2)
  #tree.PrintTree(tree.root)
  node = tree.Find(2)
  Test('Delete method with left child: 2 is removed.', node is None)
  parent = tree.Find(3)
  child = tree.Find(1)
  Test('Delete method with left child: Left child of 3 is 1.', parent.left_child is child)
  Test('Delete method with left child: Parent of 1 is 3.', child.parent is parent)

  tree.Delete(7)
  #tree.PrintTree(tree.root)
  node = tree.Find(7)
  Test('Delete method with right child: 7 is removed.', node is None)
  parent = tree.Find(6)
  child = tree.Find(8)
  Test('Delete method with right child: Right child of 6 is 8.', parent.right_child is child)
  Test('Delete method with right child: Parent of 8 is 6.', child.parent is parent)


  #
  # Tests for deleting node with both children
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: Delete node with two children' + bcolors.ENDC

  tree = CreateTree()
  tree.Delete(6)
  #tree.PrintTree(tree.root)

  node = tree.Find(6)
  Test('Delete method with both children: 6 no longer exists.', node is None)
  parent = tree.Find(5)
  child = tree.Find(6.5)
  Test('Delete method with both children: Right child of 5 is 6.5.', parent.right_child is child)
  Test('Delete method with both children: Parent of 6.5 is 5', child.parent is parent)

  parent = tree.Find(6.5)
  child = tree.Find(5.5)
  Test('Delete method with both children: Left child of 6.5 is 5.5.', parent.left_child is child)
  Test('Delete method with both children: Parent of 5.5 is 6.5.', child.parent is parent)

  parent = tree.Find(6.5)
  child = tree.Find(7)
  Test('Delete method with both children: Right child of 6.5 is 7.', parent.right_child is child)
  Test('Delete method with both children: Parent of 7 is 6.5.', child.parent is parent)

def TestUpdateHeights():
	#
  # Tests for updating the heights in a tree after a deletion of a node
  #
  print '\n' + bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Test: UpdateHeights after node is deleted' + bcolors.ENDC
  tree = CreateTree()
  tree.Delete(6)
  #tree.PrintTree(tree.root)

  n = tree.Find(6.5)
  Test('Height of node with key 6.5 should be 1.', n.height == 1)

  n = tree.Find(7)
  Test('Height of node with key 7 should be 2.', n.height == 2)

  n = tree.Find(5.5)
  Test('Height of node with key 5.5 should be 2.', n.height == 2)

  n = tree.root
  Test('Height of root node should be 0.', n.height == 0)

class bcolors:
  HEADER = '\033[95m' # Purple
  OKBLUE = '\033[94m' # Blue
  OKGREEN = '\033[92m' # Green
  WARNING = '\033[93m' # Yellow
  FAIL = '\033[91m' # Red
  ENDC = '\033[0m' # Black
  BOLD = '\033[1m' # Bold
  UNDERLINE = '\033[4m' # Underline

def Test(testName, bool):
  if bool:
    print bcolors.OKGREEN + testName + " Passed." + bcolors.ENDC
  else:
    print bcolors.FAIL + testName + " Failed." + bcolors.ENDC


def main():
  tree = CreateTree()
  tree.PrintTree(tree.root)

  TestFind()
  TestFindSuccessor()
  TestDelete()
  TestUpdateHeights()


if __name__ == '__main__':
  main()