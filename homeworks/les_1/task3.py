"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

print('#' * 20)
print("Вариант работы с числом")
while True:
    user_num = input('введите целое число\n')
    if user_num.isdigit():
        user_num = int(user_num)
        break
    print('Ошибка введено не число')

count = 0
tmp = user_num

while tmp:
    # tmp = tmp // 10
    tmp //= 10
    count += 1

nn_div = 10 ** count + 1
nnn_div = (10 ** (count * 2)) + nn_div
result = user_num + (user_num * nn_div) + (user_num * nnn_div)

print(result)

print('#' * 20)
print("Вариант работы со строкой")
while True:
    user_num = input('введите целое число\n')
    if user_num.isdigit():
        break
    print('Ошибка введено не число')

result = int(user_num) + int(user_num * 2) + int(user_num * 3)
print(result)
