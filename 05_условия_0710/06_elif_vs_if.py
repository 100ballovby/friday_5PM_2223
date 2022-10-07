n = 567

# если писать только с IF, то будут проверяться все ветки
# вне зависимости от их количества
if n % 7 == 0:
    print('divide by 7')
if n % 3 == 0:
    print('divide by 3')
else:
    print('nothing')


