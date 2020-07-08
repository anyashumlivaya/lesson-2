def simple_calc( ):
	x = float(input('Введите количество отработанных часов : '))
	y = float(input('Введите оплату за 1 час : '))
	z = float(input('Укажите размер премии - '))
	wage = x*y
	return wage + z
	print (f'зарплата {simple_calc() }')