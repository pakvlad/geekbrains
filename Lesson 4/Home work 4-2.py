start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [u for i, u in enumerate(start_list) if i!= 0 and start_list[i-1] < start_list[i]]
print(f'Исходный список {start_list}')
print(f'Новый список {new_list}')