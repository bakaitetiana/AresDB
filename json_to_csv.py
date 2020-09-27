import json
import csv
import sys

count = 0
line_counter = 0
for file in open("2_data.json"):
	line_counter+=1
	tempJ = open('temp.json', 'w')
	tempJ.write(file)
	tempJ.close()
	thefile = open('temp.json')
	try:
		data = json.load(thefile)
	except:
		print(line_counter, sys.exc_info())

	data_file = open("2_data.csv", "a", newline='')
	csv_writer = csv.writer(data_file)
	for data_line in data.values():
			for item in data_line:
				if count == 0:
					header = item.keys()
					csv_writer.writerow(header)
					count+=1
				csv_writer.writerow(item.values())



	data_file.close()
	thefile.close()