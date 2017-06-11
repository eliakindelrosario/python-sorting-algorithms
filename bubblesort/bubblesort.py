

class BubbleSort():

	def __init__(self):
		pass

	def bubbleSort(self, x):
		self.x = x
		for elem in range(len(self.x)-1,0,-1):
			for i in range(elem):
				if self.x[i]> self.x[i+1]:
					self.swap(i)
	def swap(self, i):
		temp = self.x[i]
		self.x[i] = self.x[i+1]
		self.x[i+1] = temp


alist = [54,26,93,17,77,31,44,55,20]
sort = BubbleSort()
sort.bubbleSort(alist)
print(alist)