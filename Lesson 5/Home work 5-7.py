import json

profit_company = {}
pr = {}
prof = 0
aver = 0
i = 0
with open('file_7.txt', 'r') as file_7:
    for line in file_7:
        name, firm, earning, damage = line.split()
        profit_company[name] = int(earning) - int(damage)
        if profit_company.setdefault(name) >= 0:
            prof = prof + profit_company.setdefault(name)
            i += 1
        if i != 0:
            aver = prof / i
            print(f'Средняя прибыль - {aver:.2f}')
        else:
            print(f'Средняя прибыль отсутствует - Все работают в убыток')
        pr = {'Средняя прибыль': round(aver)}
        profit_company.update(pr)
        print(f'Прибыль каждой компании - {profit_company}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit_company, write_js)
    js_str = json.dumps(profit_company)
    print(f'Создан файл с расширением json со следующим содержимым:/n'f'{js_str}')