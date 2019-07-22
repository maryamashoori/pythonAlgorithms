
#   A Python implementation of Counting Sort
#   https://en.wikipedia.org/wiki/Counting_sort
#
#   Created by Maryam Ashoori on July 2019.
#   Tested in Python 3.7

import numpy as np

# Counting sort is a linear sort algorithm on an an array of digits that are bounded to an upper bound of max
# Performance complexity is O(n+max)
def counting_sort(input):
    max = np.amax(input)
    temp = []
    sorted_input = input.copy()
    temp = [0] * (max+1) # initializes the value of temp with 0 for each digit
    for element in range(len(input)):
        temp[input[element]-1] +=1
    for j in range(1, max+1):
        temp[j] = temp[j] + temp[j-1]
    for element in range(len(input)-1, 0, -1):
        sorted_input[temp[input[element]-1]-1] = input[element]
        temp[input[element]-1] -=1
    return sorted_input

if __name__=="__main__":
    input = [2, 8, 3, 5, 7, 5, 6, 4]
    print(f"Input is {input}, \nSorted input is {counting_sort(input)}")