
#   An implementation of Breath First Search
#   https://en.wikipedia.org/wiki/Breadth-first_search
#
#   Created by Maryam Ashoori on July 2019.
#   Tested in Python 3.7

from Queue import Queue

# This function performs a breath first traversal of the tree
# Each node is added to a queue.
# Once popped from the queue, the popped node is added to the path and its neighbors get added to the queue.
# Complexity: O(n)

def BreathFirstSearch(graph):
    q = Queue()
    path = []
    q.push (list(graph)[0])
    while q != None:
        node = q.pop()
        if not node in path:
            path.append(node)
            if len(path) == len(graph):
                return path
            else:
                for neighbor in graph[node]:
                    if not neighbor in path:
                        q.push(neighbor)
    return path

if __name__ == "__main__":
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C', 'E', 'F'],
             'E': ['D'],
             'F': ['D']}
    print (BreathFirstSearch (graph))





