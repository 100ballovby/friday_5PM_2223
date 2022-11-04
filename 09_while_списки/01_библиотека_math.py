import math as m
# библиотека с математическими функциями

a = 2.413091283351
b = 2.987
print(b, '=', m.floor(b))  # округляет "в пол"
print(a, '=', m.ceil(a))  # округляет "в потолок"

# возвращает число, имеющее модуль как у X, а знак как у У
print(m.copysign(-89, 3))
# находит модуль числа X
print(m.fabs(-367))  # если нужно получить целое, оберните fabs в int

# возвращает целую и дробную часть Х
res = m.modf(-4.593)  # здесь генерируется кортеж (похож на список)
print(res[0], res[1])

# возвести число Х в степень У
print('2^3 =', m.pow(2, 3))

# найти квадратный корень
print('√49 =', m.sqrt(49))
# второй вариант нахождения корня - возвести число в степень 0.5
print('√49 =', m.pow(49, 0.5))

# число π
print('π =', m.pi)
