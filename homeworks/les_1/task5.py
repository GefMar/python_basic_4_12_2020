"""
 Запросите у пользователя значения выручки и издержек фирмы.
 Определите, с каким финансовым результатом работает фирма
 (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
 Выведите соответствующее сообщение.
 Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
 Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

while True:
    proceeds = input('Введите сумму выручки')
    if proceeds.isdigit():
        proceeds = int(proceeds)
        break
    print('Ошибка данных, введено не число')

while True:
    cost = input('Введите сумму издержек')
    if cost.isdigit():
        cost = int(cost)
        break
    print('Ошибка данных, введено не число')

fin_result = proceeds - cost

if fin_result > 0:
    ratio = proceeds / cost
    print(f'ваша прибыль равна: {fin_result}, вы молодец\nсоотношение состовляет {ratio}')
    while True:
        worker_count = input('Введите количество сотрудников')
        if worker_count.isdigit():
            worker_count = int(worker_count)
            break
        print('Ошибка данных, введено не число')
    profit_of_worker = fin_result / worker_count
    print(f'прибыль на одного сотрудника составляет: {profit_of_worker}')

elif not fin_result:
    print('нет не прибыли не убытков, странный бизнес')
else:
    print(f'Казна пустеет милорд, ваши убытки составили: {fin_result}')
