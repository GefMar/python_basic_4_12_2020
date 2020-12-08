"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

print('#' * 20)
print("вариант арифметический")
while True:
    user_num = input('введите целое число\n')
    if user_num.isdigit():
        user_num = int(user_num)
        break
    else:
        print('ошибка ввода, это не число')

result = 0
while user_num and result != 9:
    tmp = user_num % 10
    if tmp > result:
        result = tmp
    user_num //= 10

print(result)

print('#' * 20)
print("Вариант работы со строкой")
while True:
    user_num = input('введите целое число\n')
    if user_num.isdigit():
        break
    else:
        print('ошибка ввода, это не число')

result = 9
while result:
    if str(result) in user_num:
        break
    result -= 1
