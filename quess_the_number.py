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


computer_number = random.randint(1, 100)  # випадкове число від 1 до 100
attempts = 0

start_time = time.time()



while True:
    user_number = int(input("Введіть число дів 1 до 100: "))

    if user_number == 0:
        break
    else:
        attempts += 1

    if computer_number != user_number:
        print(f"" if 1 > abs(computer_number - user_number) < 10 else "Гаряче" if 11 > abs(computer_number - user_number) < 20 else "Тепло" if 21 > abs(computer_number - user_number) < 99 else "Холодно"   )
    else: 
        end_time = time.time()
        result_time = end_time - start_time

        print(f"Grats {computer_number}. Your attempt {attempts}")
        print(f"result rime {round(result_time, 2)} sec")
        yes_no = input("Продовжити введіть y, для завершення введіть n: ")
        
        if yes_no == "n":
            break
        elif yes_no == "y":
            computer_number = random.randint(1, 100)
            continue
        else:
            while True:
                yes_no = input("Продовжити введіть y, для завершення введіть n: ")
            
                if yes_no in "yn":
                    break
                else:
                    continue


            
        

            
            
            
            

        