
#   BinarySearchTree.py
#   PythonAlgorithms
#
#   Created by Maryam Ashoori on June 2019.

class Node:
    def __init__(self, x):
        self.value = x
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, value):
        if (self.root == None):
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, curr_node, value):
        if (value <curr_node.value):
            if curr_node.left == None:
                curr_node.left = Node(value)
                return
            else:
                self._insert(curr_node.left , value)
        elif (value > curr_node.value ):
            if curr_node.right == None:
                curr_node.right = Node(value)
            else:
                self._insert(curr_node.right, value)
        else:
            print ("item already in the tree")

    # Traversal
    def traverse(self):
        if self.root != None:
            self._traverse (self.root)

    def _traverse(self, curr_node):
        if curr_node == None:
            return
        self._traverse (curr_node.left)
        print (curr_node.value)
        self._traverse(curr_node.right)

    # Height
    def height (self):
        if self.root != None:
            return self._height (self.root, 0)
        else:
            return 0

    def _height (self, curr_node, height):
        if curr_node != None:
            return max (self._height (curr_node.left, height), self._height(curr_node.right, height))+1
        else:
            return height

    # Check membership
    def findTarget(self, value):
        if self.root != None:
            return self._findTarget (self.root, value)
        else:
            return False

    def _findTarget (self, curr_node, target):
        if curr_node != None:
            if target == curr_node.value:
                return True
            elif (target > curr_node.value):
                return self._findTarget(curr_node.right, target)
            else:
                return self._findTarget(curr_node.left, target)
        else:
            return False

# Testing the class
tree = BinarySearchTree ()
tree.insert(10)
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(11)
tree.traverse()
print ("Height =" , tree.height())
print ("Target found = ", tree.findTarget(15))


