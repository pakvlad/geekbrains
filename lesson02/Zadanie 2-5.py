my_list = [7, 5, 3, 3, 2]
number = int(input('Введите число которое хотели бы добавить в список: '))
my_list.append(number)
print(sorted(my_list, reverse=True))