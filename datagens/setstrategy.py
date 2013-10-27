import random

class SetStrategy:
	def __init__(self, items):
		self.items = items

	def build(self, record):
		if len(self.items) <= 0:
			return ''
		return random.sample(self.items, 1)[0]
