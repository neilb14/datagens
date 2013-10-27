import datetime
import random
from datetime import timedelta

class TimeSeriesStrategy:
	def __init__(self, starting):
		self.last_value = starting


	def build(self, record):
		duration = random.randint(1,60*30)
		result = self.last_value + timedelta(seconds=duration)
		self.last_value = result
		return result
