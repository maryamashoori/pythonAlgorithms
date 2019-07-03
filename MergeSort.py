
#   An implementation of Merge Sort
#   https://en.wikipedia.org/wiki/Merge_sort
#
#   Created by Maryam Ashoori on July 2019.
#   Tested in Python 3.7


# Performance Complexity: O(n log n)
# Extra space needed O(n) in merge function
def merge_sort(mylist):
    middle = int(len(mylist)/2)
    if middle != 0:
        left = merge_sort(mylist[:middle])
        right = merge_sort(mylist[middle:])
        print("merging", left, right)
        return merge(left,right)
    return mylist


# merge function merges two sorted list of list1 and list2
def merge(list1,list2):
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
    print (merge_sort([1,9,3,6,2,4]))






