from itertools import count
from math import factorial
def fibo_gen():
	for el in count(1): 
		yield factorial(el)
	generator = fibo_gen()
	x = 0
	for i in generator:
		if x < 9:
			print(i)
			x += 1
		else:
				break