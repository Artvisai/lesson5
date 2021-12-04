def fib(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    return fib(num - 1) + fib(num - 2)


try:
    n = int(input('Input number of position: '))
    if n < 1:
        raise ValueError
    print('{}-th Fibonacci number is {}'.format(n, fib(n)))
except ValueError:
    print('It must be a positive integer!')