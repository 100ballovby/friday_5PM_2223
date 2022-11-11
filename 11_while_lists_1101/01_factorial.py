f = int(input('Введите число: '))

# классическое решение факториала
factorial = 1
for i in range(1, f + 1):
    factorial *= i
print(f, '! = ', factorial)

# решение через while (1)
factorial = 1
while f >= 1:
    factorial *= f
    f -= 1
print(factorial)

# решение через while (2)
f = int(input('Введите число: '))
factorial = 1
i = 1
while i <= f:
    factorial *= i
    i += 1
print(f, '! = ', factorial)

