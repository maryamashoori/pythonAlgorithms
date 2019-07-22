
#   An implementation of Insertion Sort
#   https://en.wikipedia.org/wiki/Insertion_sort
#
#   Created by Maryam Ashoori on July 2019.
#   Tested in Python 3.7

# Performance Complexity: O(n^2)
# In-place sorting algorithm


def insertion_sort(mylist):
    for key in range(len(mylist)):
        for i in range(key):
            if mylist[i] > mylist[key]:
                temp = mylist[key]
                mylist[key] = mylist[i]
                mylist[i] = temp
    return mylist

if __name__ == '__main__':
    print (insertion_sort([2, 3, 1, 8, 3, 4]))
