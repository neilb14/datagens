class CustomDateFormatter:
	def __init__(self, format_string):
		self.format_string = format_string

	def format(self, value):
		return value.strftime(self.format_string)