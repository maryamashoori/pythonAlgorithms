
#   An implementation of Breath First Search
#   https://en.wikipedia.org/wiki/Breadth-first_search
#
#   Methods implemented:
#       1- add edges to the graph
#       2- Dijkstra's shortest path algorithm
#       3- breath first search

from queue import Queue
from collections import defaultdict


# A directed representation of a weighted graph
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = []  # storing the set of vertices

    def add_edges(self, from_node, to_node, weight):
        edge = [to_node, weight]
        self.graph[from_node].append(edge)
        if from_node not in self.vertices:
            self.vertices.append(from_node)

    def find_min_distance (self, start, visited, distance):
        min_distance = float("inf")
        min_node = ''
        for node in distance:
            if node not in visited:
                if distance[node] < min_distance:
                    min_node = node
                    min_distance = distance[node]
        return min_node

    # Dijkstra's shortest path algorithm
    # https: // en.wikipedia.org / wiki / Dijkstra % 27s_algorithm
    # Time complexity is of dijkstra algorithm is
    # for n vertices, we check one by one each time starting from the node with the minimum distance and
    # check their edges and see if they decrease the distance of their neighbors
    # the sum of the degrees of nodes are 2*number of edges (m)
    # so the time complexity is O(n + m * time_complexity of find_min_distance)
    # find_min_distance) can be implemented with a priority queue (maxheap) ->time complexity: O(n+mlog n)
    # but here I didn't use max heap. the complexity of my find_min_distance is O(n) which makes the total
    # time complexity: O(n + mn)
    def dijkstra(self, start):
        distance = {}
        for node in self.vertices:
            distance[node] = float("inf")  # set the initial distance to INF
        distance[start] = 0
        visited = []
        while len(visited) is not len(self.vertices):
            min_node = self.find_min_distance(start, visited, distance)
            curr_node = min_node
            visited.append(curr_node)
            for i in range(len(self.graph[curr_node])):
                if self.graph[curr_node][i] not in visited:
                    if distance[curr_node] + self.graph[curr_node][i][1] < distance[self.graph[curr_node][i][0]]:
                        distance[self.graph[curr_node][i][0]] = distance[curr_node] + self.graph[curr_node][i][1]
        return distance

    # BFS uses a queue for traversal
    # Time complexity of traversal is O(n) when n is the number of vertices
    # each node in the graph is traversed once
    def breath_first_search(self, start):
        q = Queue()
        path = []
        q.enqueue(start)

        while not q.is_empty():
            node = q.dequeue()

            if node not in path:
                path.append(node)
                if len(path) == len(self.graph):
                    return path
                else:
                    for neighbor in self.graph[node]:
                        if neighbor[0] not in path:
                            q.enqueue(neighbor[0])
        if len(path) < len(self.graph):
            print("Error, not every node could be reached from the starting node")
        return path


if __name__ == "__main__":

    my_graph = Graph()
    my_graph.add_edges('A', 'B', 1)
    my_graph.add_edges('A', 'C', 2)
    my_graph.add_edges('B', 'C', 3)
    my_graph.add_edges('B', 'D', 4)
    my_graph.add_edges('C', 'D', 1)
    my_graph.add_edges('D', 'C', 2)
    my_graph.add_edges('D', 'E', 1)
    my_graph.add_edges('D', 'F', 3)
    my_graph.add_edges('E', 'D', 2)
    my_graph.add_edges('F', 'D', 4)

    print(f"The BFS traversal of the graph is {my_graph.breath_first_search('A')}")
    start_node = 'A'
    distance = my_graph.dijkstra(start_node)
    print(f"The shortest distance from {start_node} is {distance}")


