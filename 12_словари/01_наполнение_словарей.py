"""
Чтобы добавить в словарь новую пару ключ-значение, нужно:
1. Обратиться к словарю по его имени
2. В квадратных скобках указать ключ, !которого в словаре нет!
3. Присвоить этому ключу новое значение через =
"""
my_d = {}
my_d['audi'] = 563178
print(my_d['audi'])
# ключи в словаре не могут повторяться
my_d['audi'] = 'машина'  # здесь я переписал значение ключа audi
print(my_d['audi'])


