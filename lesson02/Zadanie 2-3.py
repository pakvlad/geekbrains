my_season_list = ['Зима', 'Весна', 'Лето', 'Осень']
my_season_dict = {1:'Зима', 2:'Весна', 3:'Лето', 4:'Осень'}
mounth = int(input ("Введите месяц от 1 до 12: "))
if mounth == 12 or mounth == 1 or mounth == 2:
    print(my_season_list[0])
    print(my_season_dict.get (1))
elif mounth == 3 or mounth == 4 or mounth == 5:
    print(my_season_list[1])
    print(my_season_dict.get(2))
elif mounth == 6 or mounth == 7 or mounth == 8:
    print(my_season_list[2])
    print(my_season_dict.get(3))
elif mounth == 9 or mounth == 10 or mounth == 11:
    print(my_season_list[3])
    print(my_season_dict.get(4))
else:
    print('В году только 12 месяцев...А Вы не знали?')