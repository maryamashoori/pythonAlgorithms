

#   A Python implementation of Max Heap
#   https://en.wikipedia.org/wiki/Heapsort
#
#   Created by Maryam Ashoori on July 2019
#   Tested in Python 3.7
#
#
#   Methods implemented:
#       1- max heapify
#       2- heapsort


class Max_heap:
    # Building a max heap
    # Complexity: O(n)
    def __init__(self, input):
        self.heap_size = len(input)
        self.elements = input
        for i in range(int(self.heap_size/2-1), -1, -1):
            self.max_heapify(i)

    # Performance complexity: O(log n)
    def max_heapify(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        if left < self.heap_size and self.elements[left] > self.elements[index]:
            largest = left
        else:
            largest = index

        if right < self.heap_size and self.elements[right] > self.elements[largest]:
            largest = right

        # swaps the index element with the largest element
        if largest != index:
            temp = self.elements[index]
            self.elements[index] = self.elements[largest]
            self.elements[largest] = temp
            self.max_heapify(largest)

    # prints the root, swaps the root with the last element of the heap and heapifies the heap.
    # Then it decreases the heap size
    # Performance complexity: O(n log n) -- n times calling max_heapify function
    def heap_sort(self):
        while self.heap_size > 0:
            print(self.elements[0])
            self.elements[0] = self.elements[self.heap_size-1]
            self.heap_size -= 1
            self.max_heapify(0)

    def __repr__(self):
        # return ",".join(map(lambda x: str(x), self.queue))
        return str(self.elements)

if __name__ == "__main__":
    myheap = Max_heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
    print (myheap)
    myheap.heap_sort()

