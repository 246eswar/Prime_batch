class Node:
	def __init__(self,data):
		self.value=data
		self.left=None
		self.right=None
def insert(root,data):
	if root is None:
		return Node(data)
	else:
		if root.value==data:
			return root
		elif root.value<data:
			root.right=insert(root.right,data)
		else:
			root.left=insert(root.left,data)
	return root
def family(root):
	if root is None:
		return True
	if root.left or root.right:
		if root.left and root.right:
			return False
		if not root.left and not root.right:
			return False
	return family(root.left) and family(root.right)
m=int(input())
l1=list(map(int,input().split()))
root=None
for i in l1:
	root=insert(root,i)
if family(root):
	print(1)
else:
	print(0)
