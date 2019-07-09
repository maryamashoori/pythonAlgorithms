#   A Python implementation of Quick Sort
#   https://en.wikipedia.org/wiki/Quicksort
#
#   Created by Maryam Ashoori on July 2019.
#   Tested in Python 3.7

class Quick_sort:
    def __init__(self, input):
        self.elements = input

    # sorts through divide and concur
    # Performance complexity: Average O(n log n) -- It calls partition log n times and parttion is O(n)
    # Worst case: when the input is reverse sorted, the partition functions partitions to 1, and n-1 partitions
    # instead of n/2 and n/2. This brings up the complexity to O(n^2)
    def quick_sort(self, start, end):
        if start < end:
            pivot = self.partition(start, end)
            self.quick_sort(0, pivot-1)
            self.quick_sort(pivot+1, end)

    # Performance complexity: O(n)
    def partition(self, start, end):
        i = start -1
        pivot = self.elements[end -1]
        for j in range (start, end):
            if self.elements[j] < pivot:
                i +=1
                # elements before i are smaller than pivot and elements
                # swap the element of index j with i+1
                temp = self.elements[i]
                self.elements[i] = self.elements[j]
                self.elements[j] = temp
        # swap the pivot element with the element in i+1 (larger than pivot)
        i +=1
        temp = self.elements[i]
        self.elements[i] = pivot
        self.elements[end-1] = temp
        return i

if __name__ == "__main__":
    input = [2, 8, 7, 1, 3, 5, 6, 4]
    qsort = Quick_sort(input)
    print(f"input before sorting: {qsort.elements}")
    qsort.quick_sort(0, len(input))
    print(f"input after sorting: {qsort.elements}")