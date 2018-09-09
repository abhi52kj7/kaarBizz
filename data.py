import csv
import math
from classes import *
from SearchClasses import *
from DataHelper import *

def getAllCarsName():
	carsName = set()
	with open('VehicleInventory.csv', 'r') as data:
		reader = csv.reader(data)

		next(reader)

		for line in reader:
			carsName.add(line[2])
	return carsName

def getCarNameQuery(query):
	carsName = dict()
	with open('VehicleInventory.csv', 'r') as data:
		reader = csv.reader(data)

		next(reader)

		for line in reader:
			if(query in line[2]):
				if(line[2] in carsName):
					models = carsName.get(line[2])
					if(line[3] not in models):
						models.append(line[3])
				else:
					carsName[line[2]] = list()
					carsName[line[2]].append(line[3])

	return carsName

def deg2rad(deg) :
	return deg * (math.pi/180)

def get_distance(lat_1, lng_1, lat_2, lng_2):
    d_lat = deg2rad(lat_2 - lat_1)
    d_lng = deg2rad(lng_2 - lng_1) 

    temp = (math.sin(d_lat / 2) ** 2 + math.cos(deg2rad(lat_1)) * math.cos(deg2rad(lat_2)) * math.sin(d_lng / 2) ** 2)
    return int(637100.0 * (2 * math.atan2(math.sqrt(temp), math.sqrt(1 - temp))))

def getNearestNeighbors(lat, lon, limit):
	dealers = list()
	with open('Dealers.csv', 'r') as data:
		reader = csv.reader(data)

		next(reader)

		for line in reader:
			obj = Dealer(int(line[0]),line[1],float(line[2]),float(line[3]),line[4],float(line[5]),int(line[6]))
			obj.disCurLocation = get_distance(float(lat), float(lon), float(line[2]), float(line[3]))
			dealers.append(obj);
		
	#dealers.sort(key=lambda x: x.disCurLocation)
	return dealers

def getDealerById(id, lat, lon):
	
	with open('Dealers.csv', 'r') as data:
		reader = csv.reader(data)

		next(reader)

		for line in reader:
			if line[0] == id :
				obj = Dealer(int(line[0]),line[1],float(line[2]),float(line[3]),line[4],float(line[5]),int(line[6]))
				obj.disCurLocation = get_distance(float(lat), float(lon), float(line[2]), float(line[3]))
				return obj

def getSearchResultsFromQuery(query):
	result = list()
	result.extend(getSearchCarMakefromQuery(query))
	result.extend(getSearchMakeModelfromQuery(query))
	result.extend(getSearchDealersfromQuery(query))
	
	return result

def getSearchDealersfromQuery(query):
	result = list()

	with open('Dealers.csv', 'r') as data:
		reader = csv.reader(data)
		count = 0
		next(reader)
		for line in reader:
			if(containsWord(line[1], query)):
				count += 1
				if count == 11:
					break
				obj = SearchDealer(int(line[0]), line[1], float(line[5]))
				result.append(obj)

	return result

def getSearchCarMakefromQuery(query):
	result = list()

	with open('Make.csv', 'r') as data:
		reader = csv.reader(data)
		count = 0
		next(reader)
		for line in reader:
			if(containsWord(line[1], query)):
				count += 1
				if count == 11:
					break
				obj = SearchCarMake(int(line[0]), line[1], line[2])
				result.append(obj)
			
	return result

def getSearchMakeModelfromQuery(query):
	result = list()

	with open('MakeModel.csv', 'r') as data:
		reader = csv.reader(data)
		count = 0
		next(reader)
		for line in reader:
			if(containsWord(line[2], query)):
				count += 1
				if count == 11:
					break
				obj = SearchMakeModel(int(line[0]), line[1], line[2], getBrandUrlFromMake(line[1]))
				result.append(obj)

	return result

#//////////////////////////////////////////////////////

def getDealerById(dtype, id, lat, lon, limit):
	result = list()
	if(dtype == "carMake"):
		result.extend(getDealerBymakeId(id, lat, lon, limit))
	elif(dtype == "makeModel"):
		result.extend(getDealerBymakeModelId(id, lat, lon, limit))
	elif(dtype == "dealer"):
		result.extend(getDealerBydealerId(id))
	
	return result


def getDealerBymakeId(makeId, lat, lon, limit):
	result = list()

	with open('Make.csv', 'r') as match, open('Orignal.csv', 'r') as data :
		match_reader = csv.reader(match)
		next(match_reader)
		data_reader = csv.reader(data)
		next(data_reader)

		for line in match_reader:
			if( line[0] == makeId ):
				makeName = line[1]
				for record in data_reader: 
					if (makeName == record[2]):
						obj = Car(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15], record[16], record[17])			
						obj.distanceFromCurrentLocation = get_distance(float(lat), float(lon), float(record[13]), float(record[14]))
	return result

def getDealerBymakeModelId(makeModelId, lat, lon, limit):
	result = list()

	with open('VehicleInventory.csv', 'r') as match, open('Dealers.csv', 'r') as data :
		match_reader = csv.reader(match)
		next(match_reader)
		data_reader = csv.reader(data)
		next(data_reader)

		dealerIds = set()

		for line in match_reader:
			if(line[2] == makeModelId):
				dealerId = line[10]
				if(dealerId in dealerIds): continue
				dealerIds.add(dealerId)
				data.seek(0)
				next(data_reader)
				for record in data_reader: 
					if (dealerId == record[0]):
						obj = Dealer(int(record[0]),record[1],float(record[2]),float(record[3]),record[4],float(record[5]),int(record[6]))
						obj.disCurLocation = get_distance(float(lat), float(lon), float(record[2]), float(record[3]))
						result.append(obj)
						break	
									
	return result

def getDealerBydealerId(dealerId):
	result = list()

	with open('Dealers.csv', 'r') as match, open('VehicleInventory.csv', 'r') as data :
		match_reader = csv.reader(match)
		next(match_reader)
		data_reader = csv.reader(data)
		next(data_reader)

		for line in match_reader:
			if(dealerId == line[0]):
				count = 0
				data.seek(0)
				next(data_reader)
				obj = Dealer(int(line[0]),line[1],float(line[2]),float(line[3]),line[4],float(line[5]),int(line[6]))
				for record in data_reader: 	
					if (dealerId != record[10]): continue
					count +=1
				obj.makemodels = count	
				result.append(obj)
			break	

	return result

