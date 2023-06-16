class Human:
    def __init__(self, f_name, l_name, gender, eye_col, age, height, weight):
        """
        конструктор класса Human, он описывает начальные параметры каждого человека
        :param f_name:
        :param l_name:
        :param gender:
        :param eye_col:
        :param hair_col:
        :param height:
        :param weight:
        """
        self.first_name = f_name  # параметр класса
        self.last_name = l_name  # параметр класса
        self.gender = gender  # параметр класса
        self.eye_color = eye_col  # параметр класса
        self.age = age  # параметр класса
        self.height = height  # параметр класса
        self.weight = weight  # параметр класса

    def greeting(self, friend_name):  # метод (поведение экземпляра класса) класса human
        print(f'Hello, {friend_name}! My name is {self.first_name}')

    def birthday(self):
        self.age += 1

zhora = Human('George', 'Klinton', 'Male', 'Green', 15, 160, 60)
oksana = Human('Oksana', 'Spirit', 'Female', 'Brown', 20, 165, 55)

zhora.greeting(oksana.first_name)
print(f'сейчас жоре: {zhora.age} лет. Но у него ДР')
zhora.birthday()
print(oksana.age)
print(f'сейчас жоре: {zhora.age} лет.')



