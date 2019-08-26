

#   A Python implementation of Priority Queue using MaxHeap
#   https://en.wikipedia.org/wiki/Priority_queue
#
#   Created by Maryam Ashoori on July 2019
#   Tested in Python 3.7
#
#
#   Methods implemented:
#       1- return the max element
#       2- remove the max element from the queue
#       3- increase key
#       4- insert an element to the queue

from maxheap import MaxHeap


class PriorityQueue(MaxHeap):

    # returns the front element of the queue
    # Performance complexity: O(1)
    def heap_maximum(self):
        if self.heap_size >0:
            return self.elements[0]
        else:
            print("Error: Heap underflow)")
            return -1

    # extracts the front element of the queue
    # Performance complexity: O(log n)
    def heap_extract_max (self):
        if self.heap_size >0:
            max = self.elements[0]
            self.elements[0] = self.elements[self.heap_size-1]
            self.heap_size -=1
            self.elements.pop(self.heap_size)
            self.max_heapify(0)
            return max
        else:
            print("Error: Heap underflow")
            return -1

    # implements an increase-key operation in a p queue
    # Performance complexity: O(log n) since the path traced from index to the root has length of O(lg n)
    def heap_increase_key(self, index, key):
        if self.heap_size < index:
            print("Error: Index out of range")
        elif key < self.elements[index]:
            print("Error: new key should be larger than the current key")
        else:
            self.elements[index] = key
            # while the element in the heap is larger than it's parent, swap the two elements
            while self.elements[index] > self.elements [int(index/2)]:
                temp = self.elements [int(index/2)]
                self.elements[int(index/2)] = self.elements[index]
                self.elements[index] = temp
                index = int(index/2)

    # implements insert operation in a p queue . It takes a key and inserts at the right place in the p queue
    # Performance complexity: similar to heap_increase_key : O(log n)
    def max_heap_insert(self, key):
        self.heap_size += 1
        self.elements.append(-1000000)
        self.heap_increase_key(self.heap_size-1, key)


if __name__ == "__main__":
    p_queue = PriorityQueue([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
    print(f"Priority queue: {p_queue}")
    print(f"Front of the queue: {p_queue.heap_maximum()}")
    p_queue.heap_increase_key(9, 15)
    print(f"Priority queue after the value increase: {p_queue}")
    p_queue.max_heap_insert(20)
    print(f"New element inserted: {p_queue}")
    p_queue.heap_extract_max()
    print(f"Front element of the queue is removed: {p_queue}")



