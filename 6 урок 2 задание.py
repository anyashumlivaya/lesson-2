class Road: 
	_length = None
	_width = None
	weight = None
	thickness = None
	def __init__(self, _length, _width):
		self._length = _length
		self._width = _width
		print('определяем массу асфальта')
		
		def intake(self):
			self.weight = 25
			self.thickness = 0.05
			intake = self.length * self.width * self.weight * self.thickness / 1000
			print(f'нужно {intake} тонн')
			
			road_buil = Road(10000, 3)
			road_buil.intake()