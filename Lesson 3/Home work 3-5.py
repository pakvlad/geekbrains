# Задание №5

def my_func():
    arg1 = False
    sum = 0
    while arg2 == False:
        numbers = input('Введите числа через проблел или Q чтобы закончить программу: ').split()
        arg3 = 0
        for arg2 in range(len(numbers)):
            if numbers[arg2] == 'Q' or numbers[arg2] == 'q':
                arg1 = True
                break
            else:
                arg3 = arg3 + int(numbers[arg2])
        sum = sum + arg3
        print(f'Сумма введенных чисел составляет: {sum}')
    print(f'Общая сумма введеных чисел составляет: {sum}')
my_func()