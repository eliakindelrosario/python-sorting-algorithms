'''
The quicksort algorithm work based on the idea that given a set of ordinal
elements. The set is partitioned into two partitions, where one partition
only contains elements which are less than or eaual to the pivot. The other
partition only contains elements which are greater than the pivot , where
the pivot is the value of the last element in the set.

The algorithm is then performed on each of the partitions until only one element
is left.

'''

"""
Parttion, when given a list of numbers, L, a low index and a high index:
    1. Declare a variable pivot and set it equal to the element
       in L at the high index posisiton.
    2. Declare a variable 'a' and set it equal to the low index.
    3. Declare a variable 'b' and set it equal to the high index.
    4. Loop forever
       1. While the element in L at position a is less than or equal to
          the pivot and a < b set a equal to a+1. 
       2. While the element in L at position b is greater than the pivot
          and a < b set b equal to a-1.
       3. If a >= b return a
       4. Swap elements
    
"""

def partition(L, low_index, high_index):
    pivot = L[high_index]
    b = high_index
    a = low_index
    while True:
        while (a < b) & (L[a] <= pivot):
            a = a+1
        while (a < b) & (L[b] > pivot):
            b = b-1
        if a >= b:
            return a
        swap(L, a, b)


'''
Swap, when given a list of numbers, L, and two indeces of elements within the list
swaps the two elements.
'''
def swap(L, low_index, high_index):
    temp = L[low_index]
    L[low_index] = L[high_index]
    L[high_index] = temp
            

'''
Given a list of numbers, L, a low index, and a high index:
    1. If high index - low index < 1: do nothing
    2. partiton L
    3. recursively call on left partition
    4. recursively call on right partition
'''
def quicksort(L, low_index, high_index):
    if (high_index - low_index) < 1:
        return
    p = partition(L, low_index, high_index)
    quicksort(L, low_index, p-1)
    quicksort(L, p, high_index)
