#  An implementation of Binary Search Tree
#  https://en.wikipedia.org/wiki/Linked_list
#
#   Created by Maryam Ashoori on August 2019
#   Tested in Python 3.7
#
#
#   Methods implemented:
#       1- insert elements
#       2- print elements
#       3- remove duplicates


class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None
    #
    # def __str__(self):
    #     return str(self.value)


# class LinkedList:
#
#     def __init__(self, values=None):
#         self.head = None
#         self.tail = None
#         if values is not None:
#             self.add_multiple(values)

class LinkedList:

    def __init__(self):
        self.head = None

    # Function to add a new node to the end of the list
    # Since we are not keeping a pointer to the tail here, each time, it has to iterate through the list to get to the
    # end - > O(n). If the insertion option is frequently used, it's recommended to implement a tail pointer and do
    # the insert in O(1)
    def insert(self, value):
        if self.head is None:
            self.head = LinkedListNode(value)
        else:
            self._insert(self.head, value)

    def _insert(self, curr_node, value):

        if curr_node.next is None:
            curr_node.next = LinkedListNode(value)
        else:
            self._insert(curr_node.next, value)

    # Function to print the list
    # It iterates through the list -> O(n) time complexity
    def print(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            self._print(self.head)

    def _print(self, curr_node):
        if curr_node is None:
            return
        else:
            print(curr_node.value)
            self._print(curr_node.next)

    # Function to remove duplicates
    # It's using hashtable and adds the seen values to a set
    # As it iterates through the list, if the node value is found in the seen set, it removes the node from the list
    # -> O(n) time complexity
    def remove_duplicates(self):
        if self.head is None:
            print("List is empty")
        else:
            seen = set()
            seen.add(self.head.value)
            self._remove_duplicates(self.head, seen)

    def _remove_duplicates(self, curr_node, seen):
        if curr_node.next is not None:
            if curr_node.next.value in seen:
                curr_node.next = curr_node.next.next
            else:
                seen.add(curr_node.next.value)
                self._remove_duplicates(curr_node.next, seen)


if __name__ == "__main__":
    my_linked_list = LinkedList()
    my_linked_list.insert(5)
    my_linked_list.insert(10)
    my_linked_list.insert(5)
    my_linked_list.insert(15)
    my_linked_list.print()
    print ("Removing Duplicates")
    my_linked_list.remove_duplicates()
    my_linked_list.print()






