my_str = input(" напишите любое слово  ")
a = my_str.split('   ')
print(a)
for b, el in enumerate(a, 1):
	if len(el) > 10:
		el = el[0:10]
		print(f"{b}. - {el}")