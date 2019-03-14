import unittest

from intro import *

class MyFirstTests(unittest.TestCase):
	""" MyFirstTests docstring """
	def test_hello_world(self):
		""" helloworld() unit_test """ 
		self.assertEqual(hello_world(), 'hello world')

	# def test_hello_you(self):
	# 	""" hello_you() unit_test """ 
	# 	self.assertEqual(hello_you('Karim'), 'Hi Karim!')

	# def test_hello_you_error(self):
	# 	""" hello_you() unit_test """ 
	# 	self.assertNotEqual(hello_you(123), '123 is not a valid firstname')

if __name__ == '__main__':
    unittest.main()
