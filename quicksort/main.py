from quicksort import *
from util import *
from time import time
from random import randint
from sys import exit



# num = getInput()

def setup():
	x = [] # empty list
	# add 100 random elements to the 
	# empty list
	for i in range(0, 100):
	    x.append(randint(0, 100))
	# return full list
	return x

def main():
	x = setup() # list with 100 elements
	start = time() # program start time
	print("Before: {}".format(x))
	quicksort_(x)
	print("After: {}".format(x))
	print("{0:.5f} seconds".format(time() - start)) # program end time

if __name__ == "__main__":
	exit(main())

