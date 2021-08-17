file = open("second_file.txt", "w", encoding='utf-8')
str_text = ['Привет мир!\n', 'Я так рад\n', 'У меня есть ты\n']
file.writelines(str_text)
file.close()

with open('second_file.txt') as f:
    line_count = 0
    for line in f:
        line_count += 1
print('Количество строк в документе: ', line_count)

with open('second_file.txt','r') as f:
    for line in f.readlines():
        words = len(line.split())
        print('Количество слов в строке: ', words)