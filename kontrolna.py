# 1
# змінна це контейнер в памяті який зберігає записані дані
# при записі в змінну даних з іншим типом данних, змінна просто перезапишеться 
# 2
# оператор else не обов'язковий, програма просто не виведе нічого на екран якщо не буде виконана одна з вказаних умов

# 3
# str(string) строка, тип даних найбільш простий у використуванні
# int(integer) цілі числа, числа без остачі
# float дробові числа, при конвертації з str i int бувають помилки якщо не добре розуміти їх, треба вважати
# bool значення вірно(True) і не вірно(False) використовуються більше для порівняння
# None відсутність значення, в основному не використовують спеціально, частіше як помилка

# 4
# так конструкцію if - else можна комбінувати але потірбно використовувати її в обдуманих рішеннях щоб не перевантажувати программу

# 5
# text = input("Enter your text: ")
# num =  int(input("Enter a number: "))
# print(text * num)

# 6 
# num = int(input("Enter a number: "))
# print(-num)


# 7
# name = input("Enter yout name: ")
# print("Hello, " + name)

# 8
# word = input("Enter your word: ")
# text = "Hello, world and enter your text"
# print(word in text)

# 9 
# enemy = int(input("Введіть к-сть ворогів які скоро зникнуть: "))
# ammo = int(input("Введіть к-сть ваших патронів: "))
# if ammo / enemy >= 15:
#     print("Позицію успішно займете, вперед!")
# else:
#     print("Добреть патрони і повертайтесь!")

# 10
# fuel = int(input("Ввудіть к-сть пального: "))
# distance = int(input("Введіть скільки км вам необхідно проїхати: "))
# fuel_usage = int(input("Розхід пального на 100 км: "))
# result = (fuel_usage / distance) * 100
# print(f"Ви зможете проїхати: {result} км")

# 11
# print("We find numbers in your text:")
# text = input("Enter your text: ")
# if "1" in text:
#     print("found a number")
# elif "2" in text:
#     print("found a number")
# elif "3" in text:
#     print("found a number")
# elif "4" in text:
#     print("found a number")
# elif "5" in text:
#     print("found a number")
# elif "6" in text:
#     print("found a number")
# elif "7" in text:
#     print("found a number")
# elif "8" in text:
#     print("found a number")
# elif "9" in text:
#     print("found a number")
# elif "0" in text:
#     print("found a number")
# else:
#     print("no numbers")

# 12
# num = int(input("Введіть рік: "))
# if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
#      print("Високосний")
# else:
#     print("Не високосний")

