"""
Вводится число, необходимо посчитать
сумму цифр этого числа
"""
n = int(input('Введите число: '))
summ = 0
while n != 0:  # как только число будет равно 0, цикл остановится 
    summ += n % 10  # забрать разряд единиц и добавить его к сумме
    n //= 10  # делю число на 10 целочисленно 123 // 10 = 12

print("=", summ)

