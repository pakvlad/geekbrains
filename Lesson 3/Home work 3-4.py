# Задание №4
def my_func(arg1,arg2):
    return 1 / arg1 ** abs(arg2)
print(f'Результат - {my_func(int(input("Введите число: ")), int(input("Введите отрицательное число, для возведения в степень: ")))}')