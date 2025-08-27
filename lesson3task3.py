# Завдання 3
# Користувач вводить з клавіатури якусь кількість метрів.
# Виведіть результат конвертування метрів у сантиметри, де-
# циметри, міліметри, милі.
num = int(input("Enter the number of meters: "))

print(num, "meters = ", num * 100, "cm")
print(num, "meters = ", num * 10, "dm")
print(num, "meters = ", num * 1000, "mm")
print(num, "meters = ", num / 1609, "mi")
