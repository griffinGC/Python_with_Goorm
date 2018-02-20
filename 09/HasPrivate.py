class HasPrivate:
	def __init__(self):
		self.public = "Public"
		self.__private = "Private"
		
	def print_from_internal(self):
		print(self.public)
		print(self.__private)
		