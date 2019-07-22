
#   An implementation of Merge Sort
#   https://en.wikipedia.org/wiki/Merge_sort
#
#   Created by Maryam Ashoori on July 2019.
#   Tested in Python 3.7

# Merge Sort is a recursive, divide and conquer, and stable algorithm.
# Time complexity can be expressed as T(n) = 2T(n/2) + Theta(n)
# Auxiliary Space: O(n)
# Merge sort is often the preferred sorting algorithm for a linked list.


class Merge_sort:

    # Time Complexity: O(n log n)
    # Extra space needed: O(n) in merge function
    def merge_sort(self, mylist):
        middle = int(len(mylist)/2)
        if middle != 0:
            left = self.merge_sort(mylist[:middle])
            right = self.merge_sort(mylist[middle:])
            print("merging", left, right)
            return self.merge(left, right)
        return mylist


    # merge function merges two sorted list of list1 and list2
    def merge(self, list1,list2):
        temp = []
        i1 = 0 #pointer to the beginning of list 1
        i2 = 0 # pointer to the beginning of list 2
        while i1 < len(list1) or i2 < len(list2):
            if i1 < len(list1) and i2 < len(list2):
                if list1[i1] < list2[i2]:
                    temp.append (list1[i1])
                    i1 += 1
                else:
                    temp.append(list2[i2])
                    i2 += 1
            elif i1 < len(list1):
                temp.append(list1[i1])
                i1 += 1
            elif i2 < len(list2):
                temp.append(list2[i2])
                i2 += 1
        return temp

if __name__ == "__main__":
    input = [1,9,3,6,2,4]
    msort =Merge_sort()
    print(msort.merge_sort(input))






