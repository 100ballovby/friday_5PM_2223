n = int(input('Введите n: '))
num = 1
# while
print(1)
while (num ** 2) < n:
    num += 1
    print(num ** 2)

for i in range(n):
    if i ** 2 > n:
        break
    print(i ** 2)

