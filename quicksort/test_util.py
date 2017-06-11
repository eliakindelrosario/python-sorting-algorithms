from util import *
import unittest

class TestUtil(unittest.TestCase):
    def test_get_list_of_numbers(self):
        self.assertEqual(get_list_of_numbers('1 2 3'), [1,2,3])


if __name__=='__main__':
    unittest.main()
