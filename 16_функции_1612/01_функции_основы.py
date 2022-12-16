def square_root(n):  # определяю функцию
    return n ** 0.5


def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

# чтобы функции работали, их нужно вызывать
res = square_root(49)
print(f'√49 = {res}')
print(f'√49 * 2 = {res * 2}')
print(f'√√49{square_root(res)}')

for i in range(11):
    r = factorial(i)
    print(f'{i}! = {r}')

print(factorial(90))


