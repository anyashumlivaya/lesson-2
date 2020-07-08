my_list = [3, 5, 5, 12, 3, 12, 15, 10, 15]
my_list2= [el for el in my_list if my_list.count(el) < 2]
print(my_list2)