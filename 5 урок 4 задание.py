translater = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
my_list = []
result = []
try:
	file_obj = open("file4.txt", 'r') 
	for line in file_obj:
		tokens = line.split(" - ")
		print(tokens) 
		if tokens[0] in translater:
			word = translater[tokens[0]] 
			result.append(word +' - '+ tokens[1])
			print(result)
except IOError:
		 print("ошибка ввода!")
finally: file_obj.close()
try: 
		 file_input = open("file4.txt", "w") 
		 file_input.writelines(result)
except IOError:
		 	print("ошибка ввода!")
finally:
		 	file_input.close()