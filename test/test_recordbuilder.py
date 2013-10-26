import unittest
from datagens import recordbuilder as rb

class RecordBuilderTest(unittest.TestCase):
	def test_firstThingsFirst(self):
		builder = rb.RecordBuilder()
		record = {}
		builder.start(record)
		self.assertEqual(record['feature'], 'Moose')

if __name__ == "__main__":
    unittest.main()