my_list = [7, 5, 3, 3, 2]
print(my_list)
number = int(input('Введите число которое хотели бы добавить в выше указанный список: '))
my_list.append(number)
print(sorted(my_list, reverse=True))