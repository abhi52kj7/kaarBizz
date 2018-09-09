class Dealer:
	
	disCurLocation = 0
	makeModels = 0

	def __init__(self, id, name, lon, lat, mail, avgRating, peopleRated):
		self.id = id
		self.name = name
		self.lat = lat
		self.lon = lon
		self.mail = mail
		self.avgRating = avgRating
		self.peopleRated = peopleRated


class MakeModel:

	def __init__(self, make, model):
		self.make = make
		self.model = model


class MakeModels:

	def __init__(self, id, make, model):
		self.id = id
		self.make = make
		self.model = model

class Car:

	distanceFromCurrentLocation = 0

	def __init__(self,id,vin,make,model,year,price,trim,engine,body,color,transmission,dealerId,dealerName,lat,lon,email,rating,rateCount)
		self.id = id
		self.id = vin
		self.id = make
		self.id = model
		self.id = year
		self.id = price
		self.id = trim
		self.id = engine
		self.id = body
		self.id = color
		self.id = transmission
		self.id = dealerId
		self.id = dealerName
		self.id = lat
		self.id = lon
		self.id = email
		self.id = rating
		self.id = rateCount