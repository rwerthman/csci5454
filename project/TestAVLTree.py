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
  
  tree = CreateTree()

  node = tree.Find(10)
  Test('Test Find method with key not in tree.', node is None)

  node = tree.Find(2)
  Test('Test Find method with key in tree.', node.key == 2)

def TestFindSuccessor():
	print bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Tests for FindSuccessor' + bcolors.ENDC
	tree = CreateTree()
	tree.PrintTree(tree.root)

	node = tree.Find(6)
	successor = tree.FindSuccessor(node)
	node = tree.Find(6.5)
	Test('Test FindSuccessor: Node is correct successor.', successor is node)

	node = tree.Find(5)
	successor = tree.FindSuccessor(node)
	node = tree.Find(5.5)
	Test('Test FindSuccessor: Node is correct successor.', successor is node)


def TestDelete():

  #
  # Tests for deleting a leaf node
  #
  print bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Tests for deleting a leaf node' + bcolors.ENDC

  tree = CreateTree()
  tree.PrintTree(tree.root)

  tree.Delete(8)
  tree.PrintTree(tree.root)
  node = tree.Find(8)
  Test('Test Delete method with leaf node.', node is None)

  tree.Delete(4)
  tree.PrintTree(tree.root)
  node = tree.Find(4)
  Test('Test Delete method with leaf node.', node is None)

  tree.Delete(1)
  tree.PrintTree(tree.root)
  node = tree.Find(1)
  Test('Test Delete method with leaf node.', node is None)

  #
  # Tests for deleting node with single child
  #
  print bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Tests for deleting node with single child' + bcolors.ENDC

  tree = CreateTree()
  tree.Delete(2)
  tree.PrintTree(tree.root)
  node = tree.Find(2)
  Test('Test Delete method with left child: Node is removed.', node is None)
  parent = tree.Find(3)
  child = tree.Find(1)
  Test('Test Delete method with left child: Child is correct.', parent.left_child is child)
  Test('Test Delete method with left child: Parent is correct.', child.parent is parent)

  tree.Delete(7)
  tree.PrintTree(tree.root)
  node = tree.Find(7)
  Test('Test Delete method with right child: Node is removed.', node is None)
  parent = tree.Find(6)
  child = tree.Find(8)
  Test('Test Delete method with right child: Child is correct.', parent.right_child is child)
  Test('Test Delete method with right child: Parent is correct.', child.parent is parent)


  #
  # Tests for deleting node with both children
  #
  print bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKBLUE + 'Tests for deleting node with two children' + bcolors.ENDC

  tree = CreateTree()
  tree.Delete(6)
  tree.PrintTree(tree.root)

  node = tree.Find(6)
  Test('Test Delete method with both children: Node is removed.', node is None)
  parent = tree.Find(5)
  child = tree.Find(6.5)
  Test('Test Delete method with both children: Child is correct.', parent.right_child is child)
  Test('Test Delete method with both children: Parent is correct.', child.parent is parent)

  parent = tree.Find(6.5)
  child = tree.Find(5.5)
  Test('Test Delete method with both children: Child is correct.', parent.left_child is child)
  Test('Test Delete method with both children: Parent is correct.', child.parent is parent)

  parent = tree.Find(6.5)
  child = tree.Find(7)
  Test('Test Delete method with both children: Child is correct.', parent.right_child is child)
  Test('Test Delete method with both children: Parent is correct.', child.parent is parent)


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
  TestFind()
  TestDelete()
  TestFindSuccessor()


if __name__ == '__main__':
  main()