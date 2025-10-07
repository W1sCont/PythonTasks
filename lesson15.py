# генератори  (yield замість return)

# def powers(n: int):  # n =20 -> 1, 4, 9, 16, ....n2

#     for numbers in range(1, n + 1):
#         yield numbers ** 2   # перетворює функцію в генератор
        

# print(*powers(25))

# lambda  (анонімна функція)

# my_lambda = lambda a, b: a + b   # для прикладу, не має сенсу такий запис

# print(my_lambda(20, 10))


# humans = {
#     "Olga": 10,
#     "Vi": 20,
#     "Anna": 25
# }

# def sort_key(dict_el):
#     return dict_el[1]

# print(dict(sorted(humans.items(), key=sort_key))) 

# функція тут і зараз без записів повторень і тд

# print(dict(sorted(humans.items(), key=lambda dict_el: dict_el[1])))


# string = "Hello, world!"
# print("".join(map(lambda char: f"! {char}!", string)))


# за один рядок перемнодити все числа в списку
# numers = [10, 20, 30, 40, 50]

# import functools

# print(functools.reduce(lambda el1, el2: el1 * el2, numers))


# nums = []

# # def func():
# #     nums.append(1)

# # func()
# # func()
# # func()
# # func()

# # print(nums)

# def func(l: list):
#     l.append(1)

# func(nums)
# func(nums)

# print(nums)

# декоратори 

import time

# шаблон базового декоратора

def time_dekorator(function):
    def wrapper(*args, **kwargs):
        start = time.time()  # код додатковий
        result = function(*args, **kwargs) # оригінальна функція
        end = time.time()  # код 
        print(f"Час роботи {function.__name__}: {end - start} сек")
        return result

    return wrapper




@time_dekorator  # декорування функції у памяті
def timer(secs: int):
    while secs > 0:
        print(f"Залишилось {secs} сек. ")
        secs -= 1
        time.sleep(1)

# timer = time_dekorator(timer)

timer(5)








# замикання памяті --- почитати  =========