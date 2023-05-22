a = 1
while a == 1:
    name = input('Введите имя...')
    age = int(input('Введите возраст...'))

    if age == 0 or age < 0:
        print('Ошибка, повторите ввод,', name)
    elif 0 < age < 10:
        print("Привет шкет,", name)
    elif 10 <= age <= 18:
        print('Как жизнь?', name)
    elif 18 < age < 100:
        print('Что желаете,', name)
    else:
        print(name, ', вы лжете - в наше время столько не живут...')