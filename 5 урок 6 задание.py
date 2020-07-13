import json
study = {}
with open('file6.txt', 'r') as init_f: 
for line in init_f:
	subject, lecture, practice, lab = line.split()
	study[subject] = int(lecture) + int(practice) + int(lab)
	print(f'количество занятий по предмету - \n {study}')