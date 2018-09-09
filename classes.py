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

	disCurLocation = 0

	def __init__(self,id,vin,make,model,year,price,trim,engine,body,color,transmission,dealerId,dealerName,lat,lon,mail,avgRating,peopleRated):
		self.id = id
		self.vin = vin
		self.make = make
		self.model = model
		self.year = year
		self.price = price
		self.trim = trim
		self.engine = engine
		self.body = body
		self.color = color
		self.transmission = transmission
		self.dealerId = dealerId
		self.dealerName = dealerName
		self.lat = lat
		self.lon = lon
		self.mail = mail
		self.avgRating = avgRating
		self.peopleRated = peopleRated
