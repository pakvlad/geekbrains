words = str(input('Введите любые слова разделенные пробелами: '))
x = words.split()
y = 1
for i in x:
    print(y, i[:10])
    y += 1