from AVLTree import AVLTree

def main():
	tree = AVLTree()

	tree.insert(5) # Root node

	tree.insert(3)
	tree.insert(4)
	tree.insert(6)
	tree.insert(5)
	tree.insert(7)
	tree.insert(8)
	tree.insert(2)
	tree.insert(1)


	tree.print_tree(tree.root)


if __name__ == '__main__':
	main()