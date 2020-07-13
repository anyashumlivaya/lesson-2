people = {'петров': 25000, 'иванов': 210000, 'сидоров': 45000, 'петров2': 15000, 'сидоров2': 41000, 'иванов2': 56000, 'петров3': 12000, 'сидоров3': 100000, 'иванов3': 7000, 'петров4': 89000}
try:
	file_obj = open("file3.txt", 'w') 
	for last_name, salary in firm.items(): 
	file_obj.write(last_name + ':' + str(salary) + "\n")
	except IOError:
		print("ошибка ввода!")
		finally: file_obj.close()
		summa = 0
		count = 0
		persons = []
		with open("file3.txt", "r") as file_obj: 
			for line in file_obj: 
			print(line, end="")
			tokens = line.split(':')
			if int(tokens[1]) <= 20000:
				persons.append(tokens[0])
			summa += int(tokens[1]) 
			count += 1
		result = summa / count
		print(f"persons: {persons}")
		print(f"averate: {result}")
			