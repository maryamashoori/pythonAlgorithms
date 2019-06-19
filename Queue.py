class Queue:
    def __init__(self):
        self.queue = []

    # Push onto the queue. enqueue. add to the rear of the queue
    def push(self, value):
        self.queue.append(value)

    def print(self):
        for item in self.queue:
            print(item)

    # Returns the front of the queue
    def front(self):
        return self.queue[0]

    # Pop put of queue. dequeue. remove from the front
    def pop(self):
        front= self.front()
        self.queue.pop(0)
        return front

if __name__ == "__main__":
    q = Queue()
    q.push (5)
    q.push (10)
    q.print()
    print ("The item at the front of the queue is", q.front())
    print (q.pop(), "is popped")
