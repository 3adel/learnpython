import unittest 
import calc

class TestCalc(unittest.TestCase):
	
	# method name is by convention test_*
	def test_add(self):
		result = calc.add(10, 5)
		self.assertEqual(result, 15)


if __name__ == '__main__':
	unittest.main()
