import csv

def getBrandUrlFromMake(make):
	with open('Make.csv', 'r') as data:
		reader = csv.reader(data)

		next(reader)
		for line in reader:
			if(make == line[1]):
				return line[2]


def containsWord(text, pattern):
	text = text.lower()
	pattern = pattern.lower()
	if(text.startswith(pattern)):
		return True
	else:
		if(" " + pattern in text):
			return True
		else:
			return False