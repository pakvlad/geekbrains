# Задание №2

def my_func(name, surname, birth, city, email, tel):
    name = str(input('Введите имя: '))
    surname = str(input('Ваша фамилию: '))
    birth = int(input('Ваш год рождения: '))
    city = str(input('Ваш город проживания: '))
    email = str(input('Ваш электронный адрес: '))
    tel = int(input('Ваш номер телефона: '))
    return(name, surname, birth, city, email, tel)
print(my_func('name', 'surname', 'birth', 'city', 'email', 'tel'))