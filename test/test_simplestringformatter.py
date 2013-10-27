import unittest
from datetime import datetime
from datagens import simplestringformatter as f

class SimpleStringFormatterTest(unittest.TestCase):
	def setUp(self):
		self.formatter = f.SimpleStringFormatter()

	def test_formatString(self):		
		self.assertEqual("mahlzeit!", self.formatter.format("mahlzeit!"))

	def test_formatInt(self):
		self.assertEqual("1605", self.formatter.format("1605"))

	def test_formatDatetime(self):
		self.assertEqual("2013-10-27 15:05:36.001234", self.formatter.format(datetime(2013, 10, 27, 15, 5, 36, 1234)))

if __name__ == "__main__":
    unittest.main()