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

	def test_setWithMultipleItems(self):
		fields = ["red","blue","green","yellow"]
		self.strategy = s.SetStrategy(fields)
		results = [self.strategy.build({}),self.strategy.build({})]
		self.assertTrue(fields.index(results[0])>=0)
		self.assertTrue(fields.index(results[1])>=0)

if __name__ == "__main__":
    unittest.main()