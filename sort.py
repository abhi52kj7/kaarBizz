import sys, csv ,operator

data = csv.reader(open('makemodels.csv'), delimiter = ',')
sortedlist = sorted(data, key=lambda row: row[0], reverse = False)

#print(sortedlist)

with open("makemodelssort.csv", "w", newline = '') as f:
	fileWriter = csv.writer(f)
	for line in sortedlist:
		fileWriter.writerow(line)