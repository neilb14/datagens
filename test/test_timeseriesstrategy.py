import unittest
from datetime import datetime
from datagens import timeseriesstrategy as s

class TimeSeriesStrategyTest(unittest.TestCase):
	def test_randomDuration(self):
		start_date = datetime(2013,10,26,12,00,00,00)
		strategy = s.TimeSeriesStrategy(start_date)
		result = strategy.build({})
		self.assertTrue((result - start_date).total_seconds() > 0)

if __name__ == "__main__":
    unittest.main()