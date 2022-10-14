n = int(input('Введите n:'))
k = int(input('Введите k:'))
x = 30

if n == x:
    print(n, True)
elif k == x:
    print(k, True)
elif k + n == x:
    print(k, ' + ', n, True)
else:
    print('Не соответсвует условию.')
