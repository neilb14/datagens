class RecordBuilder:
	def __init__(self):
		self.fields = []

	def add_field(self, name, strategy):
		self.fields.append({'name':name,'strategy':strategy})

	def start(self, record):
		for field in self.fields:
			record[field['name']] = str(field['strategy'].build(record))

	def fieldNames(self):
		results = []
		for field in self.fields:
			results.append(field['name'])
		return results