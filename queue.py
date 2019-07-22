#   Implementation of a dynamic queue
#   The capacity of the queue is not fixed and is dynamically changed
#   https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
#   PythonAlgorithms
#
#   Created by Maryam Ashoori on July 2019
#   Tested in Python 3.7 
#
#
#   Methods implemented:
#       1- enqueue
#       2- print
#       3- return the front of the queue
#       4- dequeue
#       5- check if the queue is empty

class Queue:
    def __init__(self):
        self.queue = []

    # Add an element to the rear of the queue
    # Time complexity: O(1)
    def enqueue(self, value):
        self.queue.append(value)

    # Print the elements in the queue
    # Time complexity: O(n)
    def print(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            for item in self.queue:
                print(item)

    # A different implementation of the print function
    def __repr__(self):
        return ",".join(map(lambda x: str(x), self.queue))

    # Returns the front of the queue
    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.queue[0]

    # Delete an element from the front of the queue
    # Time complexity: O(1)
    def dequeue(self):
        if self.is_empty():
            print("Nothing in the queue")
            return None
        else:
            return self.queue.pop(0)


    # checks if the queue is empty
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(10)
    q.enqueue(7)
    # q.print()
    print("queue:", q) # calling __repr__
    print("The item at the front of the queue is", q.front())
    q.dequeue()
    print("queue:", q)  # calling __repr__
    # print(q.is_empty())
