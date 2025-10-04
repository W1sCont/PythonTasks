# множини

# empty_set = set() # створення порожньої множини
# numbers = {1, 10, 1, 100, 3, 65, 10, 100, 1, 3, 65, 10, 100, 1, 5}

# numbers.discard(5)
# # numbers.update({5, 66, 77, 88, 121})
# union_result = numbers.union({5, 66, 77, 88, 121})
# # numbers.add(23)
# print(union_result)
# print(numbers)

# унікальні методи
worker_1 = {"Python", "C++", "JavaScript", "Pearl"}
worker_2 = {"Python", "C++", "React", "Java", "Kotlin"}

print(worker_1.difference(worker_2))
# worker_1.difference()
print(worker_1.intersection(worker_2))
print(worker_1.symmetric_difference(worker_2))



'''
[1, 2, 3] list(список) - індексована послідовність елементів
(1, 2, 3) tuple(кортеж) - незмінювана індексована послідовність елементів (закритий список)
{'key':'value'} dict(словник) - послідовність елементів парою (ключ: значеннія), аналог хеш-таблиць
{1, 2, 3} set(множина) - НЕВПОРЯДКОВАНА послідовність УНІКАЛЬНИХ елементів
'''

# 1. Створення множини
empty_set = set()  # створення порожньої множини
numbers = {1, 10, 1, 100, 3, 65, 10, 100, 1, 3, 65, 10, 100, 1, 5, 4, 3, 7, 6}

# 2. Робота з індексами
# В множині НЕМАЄ індексів

# 3. Методи множин

# Стандартні
# numbers.clear()
# numbers = numbers.copy()

numbers.add(25)  # додає елемент до множини
numbers.add(1)  # якщо елемент вже є - нічого не відбувається

numbers.remove(100)  # аналог list.remove() - видаляє по значенню
numbers.discard(5)  # те саме, тільки на відміну від remove() не повертає помилки, якщо елемента немає

del_el = numbers.pop()  # видаляє та повертає елемент
print(f'Видалений елемент: {del_el}')

numbers.update({1, 5, 100, 35, 40})  # об'єднання множини з іншою послідовністю(аналог list.extend())
union_result = numbers.union({1000, 2000, 3000})  # на відміну від update, результат об'єднання повертається новою множиною
print(f'Результат union: {union_result}')

# 4. Унікальні методи
worker_1 = {'Python', 'C++', 'Javascript', 'Pearl'}  # множина А
worker_2 = {'C++', 'Java', 'Kotlin', 'React', 'Python'}  # множина Б

print(worker_1.difference(worker_2))  # елементи А, яких немає у Б
print(worker_2.difference(worker_1))  # елементи Б, яких немає у А (метод не дзеркальний)

print(worker_1.intersection(worker_2))  # спільні елементи обох множин
print(worker_2.intersection(worker_1))  # метод дзеркальний

print(worker_1.symmetric_difference(worker_2))  # всі елементи, що не спільні

# 5. Перетворення
l = [10, 20, 10, 20, 30, 40, 10, 50, 20]
print(list(set(l)))

d = {
    'key1': 10,
    'key2': 20,
    'key3': 30
}

print(set(d))
print(set('Hello, world!'))
print(list('Hello, world!'))

# 6. frozenset()
numbers_frozen = frozenset({1, 2, 3, 4, 5})

print(numbers_frozen)

# Різниця між ним та сетом така ж сама, як і різниця між списком та кортежем
