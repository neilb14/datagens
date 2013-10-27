import unittest
from datetime import datetime
from datagens import customdateformatter as f

class CustomDateFormatterTest(unittest.TestCase):
	def test_formatDatePart(self):	
		formatter = f.CustomDateFormatter("%Y%m%d")		
		self.assertEqual("20131026", formatter.format(datetime(2013,10,26,15,5,35,1234)))
		self.assertEqual("19780214", formatter.format(datetime(1978,2,14,15,5,35,1234)))

if __name__ == "__main__":
    unittest.main()