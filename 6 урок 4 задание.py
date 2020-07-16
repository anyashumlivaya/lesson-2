class Car:
	name = None
	speed = None
	color = None
	is_police = False
	def __init__(self, name, speed, color, is_police = False):
		self.name = name
		self.speed = speed
		self.color = color
		self.is_police = is_police
	def go(self):
		return f'{self.name} едет'
		
	def stop(self):
		return f'{self.name} остановилась'
		
	def turn(self, direction):
		return f'{self.name} свернула  " + direction'
		
	def speed(self):
		return f'скорость {self.name}  -  {self.speed}'
		
class TownCar(Car):
	def __init__(self, name, speed, color, is_police):
		super().__init__(name, speed, color, is_police)
		
	def speed(self):
		print (f'скорость town car {self.name} - {self.speed}')
		if self.speed > 40:
			return f'скорость {self.name} выше разрешенной для городского авто'
		else:
				return f'скорость {self.name} не превышает допустимую'
		
class SportCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(self, speed, color, name, is_police)
		
class WorkCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)
	
	def show_speed(self):
		print(f'скорость {self.name} - {self.speed}')
		if self.speed > 60:
			return f'скорость {self.name} выше разрешенной для рабочего авто'

class PoliceCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)
	
	def police(self):
		if self.is_police:
			return f'{self.name} машина полиции'
		else:
			return f'{self.name} не из полиции'

auto1 = SportCar(150, 'черная', 'ferrari', False)
auto2 = TownCar(60, '', 'белая', 'ford', False)
auto3 = WorkCar(70, 'серая', 'mazda', False)
auto4 = PoliceCar(110, 'белая', 'ваз', True)
print(auto1.speed())
print(auto2.speed())
print(auto3.police())
print(auto4.speed())