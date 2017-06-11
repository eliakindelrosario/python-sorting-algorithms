

class BubbleSort():
	
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
