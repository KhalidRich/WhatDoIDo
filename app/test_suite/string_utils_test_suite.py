import unittest
import random
from ..utils import string_utils

'''String Utils Unit Tests'''

class StringUtilsTestSuite(unittest.TestCase):

	def setUp(self):
		self.big_number = "123,456,789"
		self.awk_zero = "000,000,000"

	def test_big_number(self):
		big_number_int = 123456789
		self.assertEqual(big_number_int, string_utils.cint(self.big_number))

	def test_awk_zero(self):
		awk_zero_int = 0
		self.assertEqual(awk_zero_int, string_utils.cint(self.awk_zero))

if __name__ == "__main__":
	unittest.main()
