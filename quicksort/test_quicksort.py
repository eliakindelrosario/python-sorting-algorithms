from quicksort import *
import unittest

class TestQuickSort(unittest.TestCase):
    def test_swap(self):
        l = [1,2,3]
        swap(l,0,2)
        self.assertEqual(l, [3,2,1])

    def test_partition(self):
        self.assertEqual(partition([1,5,2,3],0,3),3)
        self.assertEqual(partition([1,5,2,3,5],0,3),3)
        self.assertEqual(partition([2,1,3,6,4],0,4),4)
        self.assertEqual(partition([2,1,6,11,2,3,2],0,6),4)
        self.assertEqual(partition([2,1,6,2,2,3],0,5),5)

    def test_quicksort(self):
        l = [2,1,6,11,2,3,2]
        quicksort(l,0,6)
        self.assertEqual(l, [1,2,2,2,3,6,11])


if __name__=='__main__':
    unittest.main()
