class RecordBuilder:
	def __init__(self):
		self.fields = []

	def add_field(self, name, strategy):
		self.fields.append({'name':name,'strategy':strategy})

	def start(self, record):
		for field in self.fields:
			record[field['name']] = field['strategy'].build(record)