import sys
from datetime import datetime
from datagens import recordbuilder, setstrategy, timeseriesstrategy

limit = sys.argv[2]
builder = recordbuilder.RecordBuilder()
with open(sys.argv[1], 'r') as config_file:
	code = config_file.readlines()
	for command in code:
		eval(command.strip(), globals(), locals())

results = []
for n in range(int(limit)):
	record = {}
	builder.start(record)
	results.append(record)

for row in results:
	str = ","
	fields = []
	keys = row.keys
	for k in row.keys():	
		fields.append(row[k])
	print(str.join(fields))
