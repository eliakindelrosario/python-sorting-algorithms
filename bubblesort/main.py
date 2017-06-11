from random import randint
from sys import exit
from time import time
from bubblesort import BubbleSort

def setup():
	x = []
	for i in range(0, 100):
	    x.append(randint(0, 100))
	return x

def main():
	x = setup() 
	start = time() # program start time
	print("Before: {}".format(x))
	sort = BubbleSort()
	sort.bubbleSort(x)
	print("After: {}".format(x))
	print("{0:.5f} seconds".format(time() - start)) # program end time

if __name__ == "__main__":
	exit(main())