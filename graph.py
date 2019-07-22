
#   An implementation of Breath First Search
#   https://en.wikipedia.org/wiki/Breadth-first_search
#
#   Methods implemented:
#       1- add edges to the graph
#       2- breath first search

from queue import Queue
from collections import defaultdict


# A directed representation of a graph
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edges(self, from_node, to_node):
        self.graph[from_node].append(to_node)

    # This function performs a breath first traversal of the tree on a directed graph
    # Each node is added to a queue.
    # Once popped from the queue, the popped node is added to the path and its neighbors get added to the queue.
    # Complexity: O(n)
    def breath_first_search(self, start):
        q = Queue()
        path = []
        q.enqueue(start)

        while not q.is_empty():
            node = q.dequeue()

            if node not in path:
                path.append(node)
                print(f"path : {path}")
                if len(path) == len(self.graph):
                    return path
                else:
                    for neighbor in self.graph[node]:
                        if neighbor not in path:
                            q.enqueue(neighbor)
        if len(path) < len(self.graph):
            print("Error, not every node could be reached from the starting node")
        return path


if __name__ == "__main__":

    my_graph = Graph()
    my_graph.add_edges('A', 'B')
    my_graph.add_edges('A', 'C')
    my_graph.add_edges('B', 'C')
    my_graph.add_edges('B', 'D')
    my_graph.add_edges('C', 'D')
    my_graph.add_edges('D', 'C')
    my_graph.add_edges('D', 'E')
    my_graph.add_edges('D', 'F')
    my_graph.add_edges('E', 'D')
    my_graph.add_edges('F', 'D')

    print(my_graph.breath_first_search('A'))




