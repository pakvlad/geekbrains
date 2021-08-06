from itertools import count
number = int(input('Введите стартовое число: '))
for el in count(number):
    if el > 100:
        break
    else:
       print(el)

from itertools import cycle

my_spisok = ['Зима','Весна', 'Лето', 'Осень']
с = 0
for el in cycle(my_spisok):
    if с > 10:
        break
    print(el)
    с += 1
