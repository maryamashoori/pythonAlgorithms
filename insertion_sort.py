
#   An implementation of Insertion Sort
#   https://en.wikipedia.org/wiki/Insertion_sort
#
#   Created by Maryam Ashoori on July 2019.
#   Tested in Python 3.7

# Performance Complexity: O(n^2)
# In-place sorting algorithm


def insertion_sort(my_list):
    for key in range(len(my_list)):
        for i in range(key):
            if my_list[i] > my_list[key]:
                temp = my_list[key]
                my_list[key] = my_list[i]
                my_list[i] = temp
    return my_list


if __name__ == '__main__':
    print(insertion_sort([2, 3, 1, 8, 3, 4]))
