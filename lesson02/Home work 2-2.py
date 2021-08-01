number = int(input("Введите количество элементов которое будет в списке: "))
my_list = []
x = 0
y = 0
while x < number:
    my_list.append(input("Введите следующее значение для созданного списка: "))
    x += 1
for el in range(int(len(my_list)/2)):
        my_list[y], my_list[y + 1] = my_list[y + 1], my_list[y]
        y += 2
print(my_list)