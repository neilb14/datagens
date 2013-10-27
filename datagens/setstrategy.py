class SetStrategy:
	def __init__(self, items):
		self.items = items
		self.next_index = 0

	def build(self, record):
		if len(self.items) <= 0:
			return ''
		if len(self.items) <= self.next_index:
			self.next_index = 0
		result = self.items[self.next_index]
		self.next_index += 1
		return result
