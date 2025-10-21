# Завдання:
# Створи клас Book, який має:

# атрибути: title, author, pages

# метод get_info(), який повертає рядок виду
# "Назва: <title>, Автор: <author>, Сторінок: <pages>"

# Додатково:
# створи кілька об’єктів Book і виведи інформацію про кожну через метод get_info().

class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return print(f"Назва: {self.title}, Автор: {self.author}, Сторінок: {self.pages}")
    


book_1 = Book("Harry Shproter", "J. Rogalic", 333)
book_2 = Book("Rocket 1", "F.Gambit", 222)

book_1.get_info()
book_2.get_info()



# Завдання:
# Створи класи:

# Engine — має потужність (horsepower)

# Car — має модель і двигун як об’єкт Engine

# Garage — може містити список автомобілів і метод show_all().


# engine = Engine(150)
# car = Car("Toyota", engine)
# garage = Garage()
# garage.add_car(car)
# garage.show_all()


# Результат: 
# У гаражі:
# Toyota (150 к.с.)



class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def get_engin(self):
        return self.horsepower


class Car:
    def __init__(self, auto: str, horsepower: Engine):
        self.auto = auto
        self.horsepower = horsepower

        if type(horsepower) is not Engine:
            raise ValueError(f"{horsepower} isnt engin value")
        
        return auto and horsepower
        
class Garage:
    def __init__(self):
        self.garage = []


    def add_car(self, car: Car):
        self.garage = car


    def show_all(self):
        return print(f"У гаражі: \n{garage} {Engine.get_engin}к.с. ) ")




# engine = Engine(150)
# car = Car("Toyota", engine)
# garage = Garage()
# garage.add_car(car)
# garage.show_all()



# Створи класи:

# Pet — має name, species, age

# Owner — має name, phone, pets (список об’єктів Pet)

# Методи:

# у Owner:

# add_pet(pet) — додає тварину до списку


# owner = Owner("Олег", "+380671112233")
# dog = Pet("Бім", "собака", 3)
# cat = Pet("Мурчик", "кіт", 2)
# owner.add_pet(dog)
# owner.add_pet(cat)
# owner.show_pets()


# Результат: 
# Олег має:
# - Бім (собака, 3 роки)
# - Мурчик (кіт, 2 роки)