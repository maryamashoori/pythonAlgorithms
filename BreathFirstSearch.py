from Queue import Queue
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C', 'E', 'F'],
         'E': ['D'],
         'F': ['D']}

def BreathFirstSearch(start, end):
    q = Queue()
    path = []
    q.push(start)
    while q != None:
        node = q.pop()
        if not node in path:
            path.append(node)
            print(path)
            if node == end:
                return path
            else:
                for neighbour in graph[node]:
                    if not neighbour in path:
                        q.push(neighbour)
                        print(neighbour, "added")
    return path

if __name__ == "__main__":
    BreathFirstSearch ('A', 'F')





