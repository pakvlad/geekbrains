goods = int(input("Введите количество товара: "))
n = 1
my_dict = []
my_list = []
while n <= goods:
    my_dict = dict({'Название:': input("Введите название товара: "), 'Цена:': input("Введите цену товара в рублях: "),
                    'Количество:': input('Введите количество товара: '), 'eд.изм:': input("Введите единицу измерения товара: ")})
    my_list.append((n, my_dict))
    n += 1
for i in my_list:
    print(i)
my_analys = {'Название:': [], 'Цена:': [], 'Количество:': [], 'eд.изм:': []}
for num, item in my_list:
    my_analys['Название:'].append(item['Название:'])
    my_analys['Цена:'].append(item['Цена:'])
    my_analys['Количество:'].append(item['Количество:'])
    my_analys['eд.изм:'].append(item['eд.изм:'])
for key, value in my_analys.items():
    print(key,value)
