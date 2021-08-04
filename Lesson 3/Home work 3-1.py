# Задание №1

def my_func():
    try:
        arg1 = int(input('Ваше делимое: '))
        arg2 = int(input('Ваш делитель: '))
    except ValueError:
        return
    if arg2 == 0:
        print('А на ноль не делится! =)')
    else:
        s_full = arg1/arg2
        return s_full
print(my_func())