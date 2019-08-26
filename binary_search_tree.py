
#   An implementation of Binary Search Tree
#   https://en.wikipedia.org/wiki/Binary_search_tree
#
#   Created by Maryam Ashoori on July 2019
#   Tested in Python 3.7
#
#
#   Methods implemented:
#       1- insertion
#       2- traversal (inorder, preorder, postorder)
#       3- calculate height of the tree
#       4- search an element in the tree
#       5- delete a node from the tree
#       6- find the min element in the tree


class Node:
    def __init__(self, x):
        self.value = x
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insertion : inserts an element to the BST
    # Time complexity:
    # The average case: O(log n)
    # The worst case time complexity of insertion is O(h) where h is height of Binary Search Tree.
    # When a tree is not balanced, it can be O(n)
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, curr_node, value):
        if value < curr_node.value:
            if curr_node.left is None:
                curr_node.left = Node(value)
                return
            else:
                self._insert(curr_node.left, value)
        elif value > curr_node.value:
            if curr_node.right is None:
                curr_node.right = Node(value)
            else:
                self._insert(curr_node.right, value)
        else:
            print ("item already in the tree")

    # Traversal : Traverses all the elements in the tree
    # A BST can be traversed in inorder (left child, root, right child), preorder (root, left child, right child),
    # or postorder (left child, right child, root)

    # Inorder traversal
    # Time complexity: O(n)
    def inorder_traversal(self):
        if self.root is not None:
            self._inorder_traversal(self.root)
        else:
            print("Empty tree!")

    def _inorder_traversal(self, curr_node):
        if curr_node is None:
            return
        else:
            self._inorder_traversal(curr_node.left)
            print(curr_node.value)
            self._inorder_traversal(curr_node.right)

    # Preorder traversal
    # Time complexity: O(n)
    def preorder_traversal(self):
        if self.root is None:
            print("Empty tree!")
        else:
            self._preorder_traversal(self.root)

    def _preorder_traversal(self, curr_node):
        if curr_node is None:
            return
        else:
            print(curr_node.value)
            self._preorder_traversal(curr_node.left)
            self._preorder_traversal(curr_node.right)

    # Postorder traversal
    # Time complexity: O(n)
    def postorder_traversal(self):
        if self.root is not None:
            self._postorder_traversal(self.root)
        else:
            print("Empty tree!")

    def _postorder_traversal (self, curr_node):
        if curr_node is None:
            return
        else:
            self._postorder_traversal(curr_node.left)
            self._postorder_traversal(curr_node.right)
            print(curr_node.value)

    # Height : Returns the hight of the tree
    # Complexity: O(log n)
    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, curr_node, height):
        if curr_node is not None:
            return max(self._height(curr_node.left, height), self._height(curr_node.right, height))+1
        else:
            return height

    # Search: searches if an element is in the tree
    # The average case: O(log n)
    # The worst case time complexity of search is O(h) where h is height of Binary Search Tree.
    # When a tree is not balanced, it can be O(n)
    def search(self, value):
        if self.root is not None:
            return self._search(self.root, value)
        else:
            return False

    def _search(self, curr_node, target):
        if curr_node is not None:
            if target == curr_node.value:
                return True
            elif target > curr_node.value:
                return self._search(curr_node.right, target)
            else:
                return self._search(curr_node.left, target)
        else:
            return False

    # Time complexity: It has to search the element, then delete the node
    # Average: O (lg n)
    # Worst case: O(n) if the tree is not balanced

    def delete(self, key):
        if self.root is None:
            "Tree is empty"
        else:
            self.root = self._delete(self.root, key)

    def _delete(self, curr_node, key):
        if curr_node is None:
            return curr_node
        elif curr_node.value < key:
            curr_node.right = self._delete(curr_node.right, key)
        elif curr_node.value > key:
            curr_node.left = self._delete(curr_node.left, key)
        else:
            # Node has no child
            if curr_node.left is None and curr_node.right is None:
                curr_node = None

            # Node has one child
            elif curr_node.left is None:
                curr_node = curr_node.right
            elif curr_node.right is None:
                curr_node = curr_node.left

            # Node has two children
            # Replaces the node with a node with minimum key value in the right tree (implemented here)
            # or maximum key value in the left tree and continues to delete that node from the subtree
            else:
                temp = self.find_min(curr_node.right)
                print(f"Hit: curr_node= {curr_node.value}")
                curr_node.value = temp.value
                curr_node.right = self._delete(curr_node.right, temp.value)
        return curr_node

    # Given a non-empty binary search tree, return the node
    # with minimum key value found in that tree.
    def find_min(self, curr_node):
        while curr_node.left is not None:
            curr_node = curr_node
        return curr_node


# Testing the class
tree = BinarySearchTree ()
tree.insert(10)
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(5)
print("inorder traversal:")
tree.inorder_traversal()  # sorts the input
print("preorder traversal:")
tree.preorder_traversal()  # sorts the input
print("Height =", tree.height())
tree.delete(5)
print("postorder traversal:")
tree.postorder_traversal()  # sorts the input
print("Target found = ", tree.search(5))



