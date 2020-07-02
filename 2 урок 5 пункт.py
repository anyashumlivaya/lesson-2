number = int(input("  введите число - "))
list = [5, 3, 2, 1]
a = list.count(number)
for element in list:
	if a>0:
		b = list.index(number)
		list.insert(a+b, number)
		break
		else:
			if number>element:
				c = list.index(nomer)
				list.insert(c, number)
				break
		
			