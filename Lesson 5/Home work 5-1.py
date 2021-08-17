file = open(input('Введите название файла: '), 'w')
while True:
    text = input('Введите строку в файл: ')
    if text == '': break
    file.write(s + '\n')
file.close()
