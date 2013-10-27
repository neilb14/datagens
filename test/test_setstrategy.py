import unittest
from datagens import setstrategy as s

class SetStrategyTest(unittest.TestCase):
	def test_emptySet(self):
		self.strategy = s.SetStrategy([])
		result = self.strategy.build({})
		self.assertEqual('',result)

	def test_setWithOneItem(self):
		self.strategy = s.SetStrategy(["red"])
		result = self.strategy.build({})
		self.assertEqual("red", result)

	def test_setWithTwoItems(self):
		self.strategy = s.SetStrategy(["red", "blue"])
		results = [self.strategy.build({}),self.strategy.build({})]
		self.assertEqual("red", results[0])
		self.assertEqual("blue", results[1])

	def test_rollBackToStartOfSet(self):
		self.strategy = s.SetStrategy(["red", "blue"])
		results = [self.strategy.build({}), self.strategy.build({}), self.strategy.build({})]
		self.assertEqual("red", results[0])
		self.assertEqual("blue", results[1])
		self.assertEqual("red", results[2])

if __name__ == "__main__":
    unittest.main()