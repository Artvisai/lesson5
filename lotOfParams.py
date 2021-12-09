def summ(*args):
    """Функция, принимающая сколько угодно параметров и возвращающая их сумму"""
    if args:
        try:
            s = args[0]
            for i in args[1:]:
                s += i
            return s
        except TypeError:
            print("TypeError!")
            return 0
    else:
        return 0


print(summ())
print(summ(1, 2, 3, 4, 5))
print(summ('q', 'w', 'e', 'r', 't', 'y'))
print(summ('k', 0, 'm', 'm', 4, 'n', 'd', 0))