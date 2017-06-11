# Quicksort 
'''
Quicksort is a very efficient sorting algorithm invented by C.A.R. Hoare. 
Its purpose is to sort a list of values recursively using the divide and concur strategy.
Quicksort can be implemented in several ways. However, at the core it all boils down to:
	1.	The partitioning of the list of values, and 
	2.	The sorting of the sub-lists. 

Quicksort is an excellent example to further understand the concept of recursion and master 
the technique of divide and concur.  
'''

# Synopsis 
'''
The quicksort works by dividing a list of values into two partitions and then sorting each 
partition respectively. For example, we divide the problem into two smaller ones and conquer 
by solving the simple scenario. 
'''

# Pseudo Implementation 
'''
1.	Pick a "pivot point" from the list. Picking a good pivot point can greatly affect the running time.
	-	Pivot point can be the first, middle or last value of the list. 
	-	Note: Randomly selecting one is also very useful, but does not get rid of the worst-case scenario. 
2.	Break the list into two lists: those elements less than the pivot element, and those elements
	greater than the pivot element.
3.	Recursively sort each of the sublists.
4.	Make one big list: the 'smaller' list, the pivot points, and the 'bigger' list.
5.	The list should be sorted by now. 
'''

# Purpose
'''
The purpose of this project is to conduct a step-by-step breakdown implementation of the quicksort
algorithm using a class.  
'''

#### Implementation ####
from sys import exit
from random import choice, randint
from math import ceil
from time import time

# The pivot in this quicksort algorithm is randomly selected 
class Quicksort():

	def quicksort(self, x):
		self.sort(x, 0, len(x)-1)

	def sort(self, x, left, right):
		# check if elements are in list
		if left >= right:
			return
		# select a randome pivot value
		pivot = x[randint(left,right)]
		# select the middle value of a list
		# pivot = x[ceil((left+right)/2)]
		
		# get the index where the list is split
		index = self.partition(x, left, right, pivot)
		# sort the left side of the list
		self.sort(x, left, index-1)
		# sort the right side of the list
		self.sort(x, index, right)

	def partition(self, x, left, right, pivot):
		# as long as left and right pointer do not overlap, continue spliting the list 
		while left <= right:
			# Left side
			# as long as the value in the left side of the list is less than the pivot value, 
			# move up the list 
			while x[left]<pivot:
				# print("Left Side")
				# print(x)
				# print("left: {} < pivot: {}".format(x[left], pivot))
				# print("\n")
				left += 1

			# Right side
			# as long as the value in the right side of the list greater than the pivot value, 
			# move down the list 
			while x[right]>pivot:
				#print("Right Side")
				# print(x)
				# print("right: {} > pivot: {}".format(x[right], pivot))
				# print("\n")
				right -= 1

			# make sure that left and right pointers do not overlap
			if left<=right:
				# swap values that are out of place
				self.swap(x, left, right)
				# continue traversing the list
				left += 1
				right -= 1

		# return the last index where both pointers meet 
		return left

	def swap(self, x, left, right):
		#print("swapping left:{} with right:{}".format(x[left], x[right]))
		temp = x[left] # store left value
		x[left] = x[right] # swicth left value with right value
		x[right] = temp # switchc right value with left value 

# def quicksort_alternative(x):
# 	# if the list has less then two elements,
# 	# then it is sorted
# 	if len(x) < 2:
# 		return x

# 	# select a random list element 
# 	pivot = choice(x)
# 	#print("pivot: {}".format(pivot))

# 	# splite the list into smaller list 
# 	# left_list contains all values smaller than the pivot
# 	left_list = [element for element in x if element < pivot]

# 	# middle list contain all values equal to the pivot 
# 	middle_list = [element for element in x if element == pivot]

# 	# right_list contains all values that are bigger than the pivot
# 	right_list = [element for element in x if element > pivot]

# 	# concatinate the list
# 	# return the list sorted after recursively sorting the left_list and the right_list
# 	return quicksort(left_list) + middle_list + quicksort(right_list)

