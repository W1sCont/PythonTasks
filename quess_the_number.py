import random
import time

# програма загадує випадкове числов ід 1 до 100
# лщристувач пробує вгадати і отримує підказки більше менше
# як тільки вгадав отримує статистику к-сть спроб час проходження і тд

# як тільки закінчується гра програма пропонує почати ще одену гру 

#дз
# 1 якщо користувач вводить y продовження програми
# якщо n кінець програми
# 2 якщо користувач замість числа вводить 0 програма закривається


computer_number = random.randint(1, 10)  # випадкове число від 1 до 100
attempts = 0

start_time = time.time()


while True:
    user_number = int(input("Enter a number: "))
    if user_number == 0:
        break
    else:
        attempts += 1

    if computer_number > user_number:
        print("My number >")
    elif computer_number < user_number:
        print("My number <")
    else:
        end_time = time.time()
        result_time = end_time - start_time

        print(f"Grats {computer_number}. Your attempt {attempts}")
        print(f"result rime {round(result_time, 2)} sec")
        yn = input("Continue enter 'y', for break enter 'n' " )
        
        if yn == "y":
            continue
        elif yn == "n":
            break
        
            
            
            
            

        