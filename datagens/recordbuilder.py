class RecordBuilder:
	def __init__(self):
		self.fields = []

	def add_field(self, name):
		self.fields.append(name)

	def start(self, record):
		for field in self.fields:
			record[field] = 'Moose'