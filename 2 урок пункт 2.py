list = ['1', '2', '3', '4', '5']
if len(list) % 2 == 0:
	i = 0 
	while i < len(list):
		el = list[i]
		list[i] = list[i+1]
		list[i+1]= el
		i += 2
else:
			i = 0
			while i < len(list) - 1:
				el = list[i]
				list[i] = list [i+1]
				list[i+1] = el
				i += 2
				print(list)