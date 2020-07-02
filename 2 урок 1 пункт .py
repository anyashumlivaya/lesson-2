my_list = [4, 3.5, "hello", True]
print (my_list)
len(my_list)
my_int = 6
my_float = 2.5
my_str = "привет"
my_tuple = ('c', '9')
my_dict = { 'a1': 10, 'a2': 20}
list = [my_list, my_int, my_float, my_str]
for i in list:
	print(f'{i} is {type(i)}')