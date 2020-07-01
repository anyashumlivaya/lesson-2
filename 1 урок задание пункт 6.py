a = int(input("введите резулттаты первого дня в км  "))
b = int(input("введите общий километраж  "))
day = 1
if a>b:
	print(day)
while a<b:
	a = a + 0.1*a
	day += 1
	print(day)