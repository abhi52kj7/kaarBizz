class SearchDealer:

	def __init__(self, id, name, avgRating):
		self.id = id
		self.name = name
		self.avgRating = avgRating
		self.resultType = "dealer"

class SearchCarMake:

	def __init__(self, id, name, brandUrl):
		self.id = id
		self.name = name
		self.brandUrl = brandUrl
		self.resultType = "carMake"

class SearchMakeModel:

	def __init__(self, id, makeName, modelName, brandUrl):
		self.id = id
		self.makeName = makeName
		self.modelName = modelName
		self.brandUrl = brandUrl
		self.resultType = "makeModel"