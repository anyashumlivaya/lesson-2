my_list = [23, 2, 8, 1, 7, 4, 110]
my_new_list = [el for num, el in enumerate(my_list) if my_list [num -1] < my_list [num]]
print(f'Исходный список {my_list}')
print (f'Новый список {my_new_list}')