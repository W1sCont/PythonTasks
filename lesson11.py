# numbers = input(": ").split()
# result = []
# ====
# result = list(map(lambda el: int(el) **2 , numbers))
# print(result)
# ====
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i]) ** 2
# print(numbers)

# 424
# words = "New Yourk Heppy New Mexico a vision python New a vision"
# words = words.split()
 # ===
# memory = []
# counter = 0

# for w in words:
#     if w not in memory:
#         memory.append(w)
#         counter += 1

# print(counter)

# ===
# print(len(set(words)))

# 5
# a = [1, 2, 3, 4, 5]
# b = [10, 11, 12, 13, 14]
# c = [-1, 2, 5, -6, 7]

# result = [sum(el) for el in zip(a, b, c)]

# print(result)

# ===
# result = []
# for i in range(len(a)):
#     sum_of_numbers = a[i] + b[i]
#     result.append(sum_of_numbers)
# print(result)
# ===
# result = []
# for i, el in enumerate(a):
#     result.append(el + b[i])

# print(result)

# 3
# numbers = [1, 1, 4, 3, 5, 4, 7, 1, 4, 7 ]
# ===
# memory = []
# for el in numbers:
#     if numbers.count(el) % 2 != 0 and el not in memory:
#         memory.append(el)
# print(memory)
# ===
# for el in set(numbers):
#     if numbers.count(el) % 2 != 0:
#         print(el)

# ==== slovnyk ====

# user = ["Bob", 27, "admin", "qwerty123"]
# user = {
#     "name": "Bob",
#     "age": 27,
#     "login": "admin",
#     "password": "qwerty123"
#  }
# print(user["age"])
# user["age"] = 35

# user["job"] = "Google inc."

# del_item = user.popitem()

# print(user)


# === iteracija slovnyka ===

# for key in user:  # kluchi
#     print(key)

# for value in user.values():  # znachenia
#     print(value)

# for key, value in user.items(): # iteracja pary
#     print(f"{key}: {value}")

# === sortuvania slovnykiv ===

# humans = {
#     "Olga": 10,
#     "Vi": 53,
#     "Qwert": 23,
#     "Anna": 18,
#     "Anton": 27,
#     "John": 3
# }
# # name age

# print(dict(sorted(humans.items(), key=lambda el: el[1])))  # shablon po 1 indeksu (value)
# print(dict(sorted(humans.items(), key=lambda el: len(el[0])))) # shablon po 0 indeksu (key)

# workers = []
# worker = {
#     name: str,
#     age: int,
#     job: str,
#     skills: str
# }

workers = [
    {
        "name": "Petro",
        "age": 25,
        "job": "Google",
        "skills": ["Python", "C++", "Assembler"]
    },
    {
        "name": "Olga",
        "age": 35,
        "job": "Meta",
        "skills": ["Python","C#"]
    },
    {
        "name": "Ivan",
        "age": 54,
        "job": "Alpha",
        "skills": ["C++","C#", "JavaScript"]
    },
    {
        'name': 'Петро Петров',
        'age': 25,
        'job': 'Безробітний',
        'skills': ['Python', 'C++', 'C#', 'Java']
    },
    {
        'name': 'Ольга Ольгова',
        'age': 35,
        'job': 'Google inc',
        'skills': ['C++', 'C#', 'Assembler']
    },
    {
        'name': 'Сергій Сергієв',
        'age': 40,
        'job': 'Meta inc.',
        'skills': ['Python', 'Django', 'Pandas', 'TensorFlow', 'Keras']
    }
]

for ls in workers:
    print(f"* {ls["name"]}, {ls["age"]}\n\tМісце роботи: {ls["job"]} \n\tНавички:\n{'\n'.join(f"\t\t-{skill}" for skill in ls['skills'])}")
    

# for index, w in enumerate(workers):
#     print(f"{index}. {w["name"]}")
#     print(f"\t Місце роботи: {w["job"]}")
#     print(f"\t Навички:")
#     for skill in w["skills"]:
#         print(f"\t\t {skill}")