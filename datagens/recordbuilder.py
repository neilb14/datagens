from datagens import simplestringformatter

class RecordBuilder:
	def __init__(self):
		self.fields = []

	def add_field(self, name, strategy, formatter = simplestringformatter.SimpleStringFormatter()):
		self.fields.append({'name':name,'strategy':strategy, 'formatter':formatter})

	def start(self, record):
		for field in self.fields:
			record[field['name']] = field['formatter'].format(field['strategy'].build(record))

	def fieldNames(self):
		results = []
		for field in self.fields:
			results.append(field['name'])
		return results	
