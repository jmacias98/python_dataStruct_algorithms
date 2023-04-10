'''
This program utilizes the concept of binary tree
'''
 
# initialize Node class, create the Root
class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

    # compare the new value with parent node 
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # print the tree             
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

# root node with insert() to add nodes
root = Node(15) 
root.insert(77)
root.insert(88)
root.insert(3)
root.insert(101)
root.insert(69)
root.insert(1)
print("Binary Tree")
root.printTree() 

# OUTPUT:
# Binary Tree
# 1
# 3
# 15
# 69
# 77
# 88
# 101






