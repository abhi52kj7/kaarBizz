import csv
from classes import *

file_get = "Make.csv"
file_read = "MakeModel.csv"
file_out = "FinalMakeModel.csv"

with open(file_get,'r') as in_file, open(file_out,'w', newline = '') as out_file, open(file_read,'r') as read_out :

	make = csv.reader(in_file)
	makeModel = csv.reader(read_out)
	finalMakeModel = csv.writer(out_file)

	for line in makeModel:
		in_file.seek(0)
		for check in make:

			if line[1] == check[1]:
				line.append(check[3])
				finalMakeModel.writerow(line)						
