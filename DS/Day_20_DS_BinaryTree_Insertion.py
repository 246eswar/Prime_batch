#Binary tree has 0,1,2 maximum childs
#operand should be always in child
#Binary search tree it is introduced for searching in tree
#but in tree values are added without using any condition so
#for this check two conditions
#left part < root
#right part > root

#AVS has balance factor of 0,1,2 only'
#If not then left rotate or right rotate will be done

#create a class for node
class Node:
    def __init__ (self,key):
        #only data pass is nothing but key
        self.left=None
        self.right=None
        self.value=key
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,key):
        #data is information
        #so taken key
        if self.root is None:
            self.root=Node(key)#nodes are None then assign
        else:
            self._insert_recursively(self.root,key)
            #current node is base on root    
    def _insert_recursively(self,current_node,key):
        #first check left then after check right
        #binary search is done upto root node is None
        if current_node.left is None:
            current_node.left = Node(key)
        elif current_node.right is None:
            current_node.right = Node(key)
        else:#both are fillef means not none then starts with left call recursively
            self._insert_recursively(current_node.left,key)
    def inorder(self):
        return self.inorder_traversal(self.root)#root node call
    def inorder_traversal(self,current_node):#travel inorder
        #nodes are available or not
        if current_node is None:
            return []
        #some elements
        #then left root right(inorder)
        return self.inorder_traversal(current_node.left)+[current_node.value]+self.inorder_traversal(current_node.right)
    def preorder(self):
        return self.preorder_traversal(self.root)#root node call
    def preorder_traversal(self,current_node):#travel inorder
        #nodes are available or not
        if current_node is None:
            return []
        #some elements
        #then  root left right(preorder)
        return [current_node.value]+self.inorder_traversal(current_node.left)+self.inorder_traversal(current_node.right)   
    def postorder(self):
        return self.postorder_traversal(self.root)#root node call
    def postorder_traversal(self,current_node):#travel inorder
        #nodes are available or not
        if current_node is None:
            return []
        #some elements
        #then left right  root (postorder)
        return self.inorder_traversal(current_node.left)+self.inorder_traversal(current_node.right)+[current_node.value]
tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
print("INORDER:",tree.inorder())
print("PREORDER:",tree.preorder())
print("POSTORDER:",tree.postorder())
