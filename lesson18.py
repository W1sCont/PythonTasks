
class Human:
    def __init__(self, name: str, age: int):  # магічний метод init
        self.name = name
        self.age = age
        self.money = 150

    def __str__(self):  # спрацьовує, коли об'єкт перетворюється на строку
        return f'Людина {self.name}'

    def __int__(self):  # спрацьовує, коли об'єкт перетворюється на ціле число
        return self.age

    def __len__(self):
        return len(self.name)

    def say_hi(self):
        return f'Привіт, я {self.name}. Мені {self.age} років!'

    def birthday(self, years: int):
        self.age += years
        print(f'{self.name} виповнилося {self.age} років!')


class Auto:
    def __init__(self, mark: str, max_passengers=4):
        self.mark = mark
        self.max_passengers = max_passengers

        self.passengers: list[Human] = []  # список Human`ів

    def __len__(self):
        return len(self.passengers)

    def add_passenger(self, human: Human):
        if type(human) is not Human:
            raise ValueError(f'В авто {self.mark} можна посадити тільки людину!')

        if human in self.passengers:
            print('Ця людина вже є у машині!')
            return

        if len(self.passengers) >= self.max_passengers:
            print(f'Авто {self.mark} вже переповнене!')
            return

        self.passengers.append(human)
        print(f'Людину додано до автомобіля {self.mark}')

    def print_passengers(self):
        print(f'Перелік пасажирів {self.mark}: ')
        for human in self.passengers:
            print(human.say_hi())


bob = Human('Bob', 25)  # ініціалізація класу (створення екземпляру(об'єкту класу))
alice = Human('Alice', 20)
john = Human('John', 35)
jason = Human('Jason', 15)


alice.birthday(5)
alice.birthday(3)

# alice.name = 'Alice'  # Груба помилка!!!!!
# alice.age = "Bob"  # Груба помилка!!!!!

# print(alice.name)  # звернення до атрибутів класу
# print(alice.age)

print(bob.say_hi())  # -> Human.say_hi(bob)
print(alice.say_hi())  # -> Human.say_hi(alice)

print(bob)
print(alice)

print(int(bob))

print(len(alice))

print('==============================')

bmw = Auto('BMW M3', max_passengers=3)

bmw.add_passenger(bob)
bmw.add_passenger(bob)  # вже є у машині (

bmw.add_passenger(john)
bmw.add_passenger(alice)

bmw.add_passenger(jason)  # не влізає(

bmw.print_passengers()



# СЛОВНИК ООП

# 1. Клас - шаблон поведінки об'єкта. Приклади: str, int, Human, Animal
# 2. Об'єкт - конкретний екземпляр класу. Приклади: "Hello", 15, Сергій, Слон

# 1 class -> ∞ object

# 3. Атрибут - "характеристика" класу, або просто змінна, яка описана всередині нього.
# Приклад для Людини: age, name, height, money, gender і тд
# 4. Метод - "дія" класу, або просто функція, що описана всередині нього
# Приклад для Людини: sleep(), eat(), walk(), say() і тд
# 5. self - посилання на конкретний об'єкт, що викликає метод.

# 6. Магічні методи (dunder-методи) - спецільні зарезервовані методи, що починаються та
# закінчуються за "__" та автоматично викликаються при якихось обставинах та умовах.
# Приклад: __init__ викликається при ініціалізації нового екземпляру (об'єкту)
