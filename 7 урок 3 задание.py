class Cell:
	def __init__(self, quantity):
		self.quantity = int(quantity)
	#self.result = result
	
	def __str__(self):
		return f' {self.quantity * "*"}'
	
	def __add__(self, other):
		# self.result = Cell(self.quantity + other.quantity)
		return Cell(self.quantity + other.quantity)
		
	def __sub__(self, other):
		if int(Cell(self.quantity - other.quantity)) > 0:
			return Cell(int(self.quantity - other.quantity))
			else:
				return f'отрицательное число'
				return self.quantity - other.quantity if (self.quantity - other.quantity) > 0
				else print('отрицательное число')
				
	def __mul__(self, other):
		return Cell(int(self.quantity * other.quantity))
	
	def __truediv__(self, other):
		return Cell(round(self.quantity // other.quantity))

def make_order(self, cells_in_row):
	row = ' '
	for i in range(int(self.quantity / cells_in_row)):
		row += f'{"*" * cells_in_row} \\n'
		row += f'{"*" * (self.quantity % cells_in_row)}'
		return row
		
cell1 = Cell(80)
cell2 = Cell(139)
print(cell1)
print(cell1 + cell2)
print(cell2 - cell1)
print(cell2.make_order(5))
print(cell1.make_order(10))
print(cell1 / cell2)	