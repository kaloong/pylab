#! /usr/bin/python

class Node:
	def __init__(self, data, left=None, right=None):
		self.left = left
		self.right = right
		self.data = data

class BST:
	def __init__(self):
		self.root = None

	def insert( self, x):
		if not self.root :
			self.root = Node(x)
			print("root : %d"%x)
		else:
			self._insert(x, self.root)

	def _insert( self, x, root):
		if x < root.data:
			"""If root.left doesnt have anything is true """
			if not root.left:
				root.left=Node(x)
				print("left : %d"%x)
			else:
				self._insert(x, root.left)
		else:
			if not root.right:
				root.right = Node(x)
				print("right: %d"%x)
			else:
				self._insert(x, root.right)

def inorder(root):
	if root.left :
		inorder(root.left)
	print("%d"%root.data, end=", ")
	if root.right:
		inorder(root.right)


def preorder(root):
	print("%d"%root.data, end=", ")
	if root.left:
		preorder(root.left)	
	if root.right:
		preorder(root.right)


def postorder(root):
	if root.left:
		postorder(root.left)
	if root.right:
		postorder(root.right)
	print("%d"%root.data, end=", ")


bst = BST()
for i in 25,15,50,10,22,35,70,4,12,18,24,31,44,66,90,91,92:
	bst.insert(i)

inorder(bst.root)

print("\n")
preorder(bst.root)
print("\n")
postorder(bst.root)
print("\n")
