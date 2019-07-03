
#   An implementation of Binary Search Tree
#   https://en.wikipedia.org/wiki/Binary_search_tree
#
#   Created by Maryam Ashoori on July 2019.
#   Tested in Python 3.7


class Node:
    def __init__(self, x):
        self.value = x
        self.right = None
        self.left = None


class Binary_search_tree:
    def __init__(self):
        self.root = None


    # Insertion : inserts an element to the BST
    # Complexity: O(log n)
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


    # Traversal : Traverses all the elements in the tree
    # Complexity: O(n)
    def print(self):
        if self.root != None:
            self._print(self.root)


    def _print(self, curr_node):
        if curr_node == None:
            return
        self._print(curr_node.left)
        print(curr_node.value)
        self._print(curr_node.right)


    # Height : Returns the hight of the tree
    # Complexity: O(log n)
    def height(self):
        if self.root != None:
            return self._height (self.root, 0)
        else:
            return 0


    def _height(self, curr_node, height):
        if curr_node != None:
            return max(self._height(curr_node.left, height), self._height(curr_node.right, height))+1
        else:
            return height


    # Search: searches if an element is in the tree
    # Complexity: O(log n)
    def find_target(self, value):
        if self.root != None:
            return self._find_target(self.root, value)
        else:
            return False


    def _find_target(self, curr_node, target):
        if curr_node != None:
            if target == curr_node.value:
                return True
            elif (target > curr_node.value):
                return self._find_target(curr_node.right, target)
            else:
                return self._find_target(curr_node.left, target)
        else:
            return False

# Testing the class
tree = Binary_search_tree ()
tree.insert(10)
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(11)
tree.print()
print("Height =", tree.height())
print("Target found = ", tree.find_target(15))


