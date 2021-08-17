file = open("file_5.txt", "w", encoding='utf-8')
str_text = ('1 2 3 4 5 6 7 8 9')
file.writelines(str_text)
file.close()

with open('file_5.txt', 'r') as f:
    my_num = str_text.split()
    print(sum(map(int, my_num)))