import unittest
from datagens import recordbuilder as rb

class RecordBuilderTest(unittest.TestCase):
	def setUp(self):
		self.builder = rb.RecordBuilder()
		self.results = {}

	def test_builderWithNoConfiguration(self):
		self.builder.start(self.results)
		self.assertEqual(0,len(self.results))

	def test_builderAddsANewColumn(self):
		self.builder.add_field('feature')
		self.builder.start(self.results)
		self.assertEqual(1,len(self.results))
		self.assertEqual(self.results['feature'], 'Moose')


if __name__ == "__main__":
    unittest.main()