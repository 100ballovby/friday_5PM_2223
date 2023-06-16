class Human:  # родовое понятие
    name = ''  # данные классы (переменные/параметры класса)
    age = 0  # данные классы (переменные/параметры класса)
    color_hair = ''  # данные классы (переменные/параметры класса)

    def greeting(self):  # метод greeting вызывается для КАЖДОГО экземпляра класса по отдельности
        print(f'Hello, my name is { self.name }! What is yours?')


zhora = Human()  # экземпляр (объект класса) - видовое понятие
zhora.name = 'George'
zhora.age = 15
zhora.color_hair = 'black'

zhora.greeting()

oksana = Human()
oksana.name = 'Oksana'
oksana.age = 20
oksana.color_hair = 'white'

oksana.greeting()
zhora.greeting()

