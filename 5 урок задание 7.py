import json
profit = {}
pr = {}
prof = 0
ave_profit = 0
i = 0
with open('file7.txt', 'r') as file:
	for line in file:
		name, enterprise, revenue, costs = line.split()
		profit[name] = int(revenue) - int(costs) 
		if profit.setdefault(name) >= 0:
			prof = prof + profit.setdefault(name)
			i += 1
		if i != 0:
			ave_profit = prof / i
			print(f'Прибыль средняя - {ave_profit:.2f}')
		else: 
		print(f'в среднем - убыток')
		pr = {'средняя прибыль': round(ave_profit)}
		profit.update(pr)
		print(f'Прибыль каждой компании - {profit}')
		with open('file7.json', 'w') as write_js: json
		dump(profit, write_js)
		js_str = json.dumps(profit)