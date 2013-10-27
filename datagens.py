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

str = ","
fieldNames = builder.fieldNames()
print(str.join(fieldNames))
for row in results:
	fields = []
	for k in fieldNames:	
		fields.append(row[k])
	print(str.join(fields))
