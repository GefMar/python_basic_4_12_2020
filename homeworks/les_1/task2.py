"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

while True:
    user_time = input('введите количество секунд\n')
    if user_time.isdigit():
        user_time = int(user_time)
        break

    print('ошибка ввода, это не число')

hh, mm, ss = user_time // 3600, (user_time % 3600) // 60, (user_time % 3600) % 60

# hh = user_time // 3600
# mm = (user_time % 3600) // 60
# ss = (user_time % 3600) % 60


print(f'{hh:>02}:{mm:>02}:{ss:>02}')

print("{:>02}:{:>02}:{:>02}".format(hh, mm, ss))
