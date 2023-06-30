import random as r

class Person:
    id = 0
    def __init__(self, c):
        self.id = Person.id
        Person.id += 1
        self.command = c


class Hero(Person):
    def __init__(self, c):
        super().__init__(c)
        self.level = 1
    def uplevel(self):
        self.level += 1


class Soldier(Person):
    def __init__(self, c):
        super().__init__(c)
        self.myHero = None

    def follow(self, hero):
        self.myHero = hero.id


h1 = Hero(1)
h2 = Hero(2)

army1 = []
army2 = []

for i in range(20):
    n = r.randint(1, 2)
    if n == 1:
        army1.append(Soldier(n))
    else:
        army2.append(Soldier(n))

print(len(army1), len(army2))
if len(army1) > len(army2):
    h1.uplevel()
else:
    h2.uplevel()

army1[0].follow(h1)
print('армия 1: ')
for soldier in army1:
    print(soldier.id, end=' ')
print(f'солдат: {army1[0].id} следует за героем {army1[0].myHero}')

