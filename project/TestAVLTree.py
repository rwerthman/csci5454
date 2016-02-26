from AVLTree import AVLTree

def CreateTree():
	tree = AVLTree()

	tree.Insert(5) # Root node

	tree.Insert(3)
	tree.Insert(4)
	tree.Insert(6)
	tree.Insert(5)
	tree.Insert(7)
	tree.Insert(8)
	tree.Insert(2)
	tree.Insert(1)

	return tree


def TestFind():
	'''
	'''
	tree = CreateTree()

	node = tree.Find(10)
	Test('Test Find method with key not in tree.', node is None)

	node = tree.Find(2)
	Test('Test Find method with key in tree.', node.key == 2)

def TestDelete():
	'''

	'''

	#
	# Tests for deleting a leaf node
	#
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



def Test(testName, bool):
	if bool:
		print testName + " Passed."
	else:
		print testName + " Failed."


def main():
	TestFind()
	TestDelete()


if __name__ == '__main__':
	main()