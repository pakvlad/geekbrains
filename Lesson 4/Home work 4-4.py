start_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'Базовый список: {start_list}')
print(f'Новый список:  {[u for u in start_list if start_list.count(u) == 1]}')