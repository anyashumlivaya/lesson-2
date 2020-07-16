class Worker:
	def __init__(self, name, surname, position, wage, bonus):
		self.name = name 
		self.surname = surname
		self.position = position
		self._salary = {"wage": wage, "bonus": bonus}
		class Position (Worker):
			def __init__(self, name, surname, position, wage, bonus):
				super().__init__(name, surname, position, wage, bonus)
			def get_full_name(self):
				return self.name + ' ' + self.surname
			def get_total_salary(self):
				return self._salary.get('wage') + self._salary.get('bonus') 

person = Position ('иван', 'иванов', 'плотник', 10000, 5000)
print(person.get_full_name(), person.get_total_salary())