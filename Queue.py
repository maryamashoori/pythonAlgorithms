#   Implementation of a queue
#   https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
#   PythonAlgorithms
#
#   Created by Maryam Ashoori on June 2019.

class Queue:
    def __init__(self):
        self.queue = []

    # Add an element to the rear of the queue
    # complexity: O(1)
    def insert(self, value):
        self.queue.append(value)

    # Print the elements in the queue
    # complexity: O(n)
    def print(self):
        for item in self.queue:
            print(item)

    # A different implementation of the print function
    def __repr__(self):
        return ",".join(map(lambda x: str(x), self.queue))

    # Returns the front of the queue
    def front(self):
        return self.queue[0]

    # Delete an element from the front of the queue
    # complexity: O(1)
    def delete(self):
        front = self.front()
        self.queue.pop(0)
        return front

if __name__ == "__main__":
    q = Queue()
    q.insert(5)
    q.insert(10)
    q.print()
    print("queue:", q) # calling __repr__
    print("The item at the front of the queue is", q.front())
    print(q.delete(), "is popped")