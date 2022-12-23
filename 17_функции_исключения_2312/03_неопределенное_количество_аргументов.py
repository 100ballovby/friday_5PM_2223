def print_nums(*args):
    print(type(args))  # <class 'tuple'> - кортеж (похож на список)
    for number in args:
        print(number, end=', ')

print_nums(4, 5, 2)
print()
print_nums(6, 12, 90, 23, 17, 5, -8, 20, 4, 2)
print()

def add_all(*nums):
    res = 0
    for i in nums:
        res += i
    return res


print(add_all(3, 12, 8, 7, 9, 4))
print(add_all(4, 2))
print(add_all(4))
print(add_all(7,  7,  6,  9,  7,  10,  2,  3,  8,  9,  3,  1,  4,  4,  8,  7,  6,  2,  4,  8,  8,  5,  9,  5,  3,  10,  2,  2,  8,  7,  8,  2,  2,  9,  3,  4,  3,  4,  6,  7,  8,  8,  8,  4,  7,  1,  1,  1,  9,  8,  3,  2,  8,  3,  9,  4,  3,  7,  9,  7,  8,  2,  6,  7,  10,  5,  6,  10,  5,  6,  5,  5,  10,  1,  8,  10,  3,  1,  10,  4,  6,  10,  9,  7,  10,  10,  5,  8,  5,  9,  7,  1,  9,  4,  2,  9,  3,  1,  6,  6))
