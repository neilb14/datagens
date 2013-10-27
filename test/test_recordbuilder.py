import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock
from datagens import recordbuilder as rb

class RecordBuilderTest(unittest.TestCase):
	def setUp(self):
		self.builder = rb.RecordBuilder()
		self.results = {}

	def test_builderWithNoConfiguration(self):
		self.builder.start(self.results)
		self.assertEqual(0,len(self.results))

	def test_builderAddsANewColumn(self):
		strategy = Mock()
		strategy.build = MagicMock(return_value = "Monkey")
		self.builder.add_field('name', strategy)
		self.builder.start(self.results)
		self.assertEqual(1,len(self.results))
		self.assertEqual(self.results['name'], 'Monkey')
		strategy.build.assert_called_with(self.results)

	def test_builderReturnsFieldNamesInTheOrderTheyWereDefined(self):
		self.builder.add_field('color', Mock())
		self.builder.add_field('sound', Mock())
		self.builder.add_field('smell', Mock())
		fields = self.builder.fieldNames()
		self.assertEqual(0, fields.index('color'))
		self.assertEqual(1, fields.index('sound'))
		self.assertEqual(2, fields.index('smell'))


if __name__ == "__main__":
    unittest.main()