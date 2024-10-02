# Домашнее задание по теме "Try и Except".
# объявление функции add_everything_up принимает аргументы a, b любого типа
def add_everything_up(a, b):
    # блок try проверки работы кода на ошибки и  если ошибки нет вернет res
    try:
        # ввод промежуточных переменных типов int (c) и float (d)
        c = int()
        d = float()
        # условие проверки, что а и b - числа
        if (type(a) or type(b)) == type(c) or (type(a) or type(b)) == type(d):
            # присвоение переменной res суммы чисел с округлением до 3
            res = round(a + b, 3)
        else:
            res = a + b
        # возврат работы функции когда ошибки нет
        return res
    # блок except вернет строковое значение в случае разных типов переменных на входе
    except TypeError:
        # присвоение перменной res строковых значений суммы  a, b
        res = (str(a) + str(b))
        # возврат работы функции при разных типах входных данных45
        return res

# исходные данные:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('HELLO ', 'WORLD'))

