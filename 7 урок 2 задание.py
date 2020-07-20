class Clothes:
	def __init__(self, size, height):
		self.size = size
		self.height = height
		
		def get_square_c(self):
			return self.size / 6.5 + 0.5
			
		def get_square_j(self):
			return self.height * 2 + 0.3
			
			@property
			
			def get_sq_full(self):
			return str(f'расход ткани \n' f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

class Coat(Clothes):
	
	def __init__(self, size, height):
		super().__init__(size, height)
		self.square_c = round(self.size / 6.5 + 0.5)
		
	def __str__(self):
	return f'расход ткани - пальто {self.square_c}'

class Jacket(Clothes):
	def __init__(self, size, height):
		super().__init__(size, height)
		self.square_j = round(self.height * 2 + 0.3)
		
	def __str__(self):
		return f' расход ткани - костюм {self.square_j}'
		
coat = Coat(5, 13)
jacket = Jacket(7, 9)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(jacket.get_square_c())
print(jacket.get_square_j())
	