from quicksort import *
from util import *

num = getInput()
print("Your orignal list was:\n",num)
quicksort(num, 0, len(num)-1)
print("Your sorted list is:\n",num)


