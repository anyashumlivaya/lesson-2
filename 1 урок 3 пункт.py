number = int(input("введите число месяца - "))
print (number)
if (number)<= 12 and number >= 1:
	dict = {1: 'январь', 2: 'февраль', 3:'март', 4:'апрель', 5:'май', 6: 'июнь', 7:'июль', 8:'август', 9:'сентябрь', 10:'октябрь', 11: 'ноябрь', 12:'декабрь'}
	list = list(dict.values())
	for y, el in enumerate(list):
		if y == number -1:
			print(f" месяц {list[y]}")
			break
		