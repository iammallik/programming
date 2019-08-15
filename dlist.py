"""
	To test Double linkedlist and Tree
"""

class Dlist:
	def __init__(self):
		self.val = []
		self.left = None
		self.right = None


class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def build_tree():
	root = Node(0)
	root.left = Node(-1)
	root.right = Node(1)
	return root


if __name__ == '__main__':
	root = build_tree()
	print(root.left.val, " ", root.val, " ", root.right.val)
	dl = Dlist()
	dl.val.append(1)
	dl.val.append(2)
	dl.val.append(4)

	for x in dl.val:
		print(x, end=" - ")

