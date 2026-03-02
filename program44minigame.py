import random

play_again = "да"
total_game = 0
best_result = 999

print ("=== УГАДАЙ ЧИСЛО ===\n")
print("Выбери уровень:")
print("1. Легко (1-50)")
print("2. Средне (1-100)")
print("3. Сложно (1-500)")

while play_again == "да":
    level = input("Уровень (1-3): ")
    if level == "1":
        max_num = 50
        secret = random.randint(1, max_num)
        attempts = 0
        print(f"\nЯ загадал число от 1 до {max_num}")
        print("Попробуй угадать!\n")
        while True:
            quess = int(input("Твоя попытка: "))
            attempts += 1 
            if quess == secret:
                print(f"\n🎉 УГАДАЛ! За {attempts} попыток!")
                total_game += 1
                if attempts < best_result:
                    best_result == attempts
                else:
                    best_result == best_result
                break
            elif quess < secret:
                print("📈 Больше!")
            else:
                print("📉 Меньше!")
        print("\nЕщё раз? (да/нет)")
    elif level == "2":
        max_num = 100
        secret = random.randint(1, max_num)
        attempts = 0
        print(f"\nЯ загадал число от 1 до {max_num}")
        print("Попробуй угадать!\n")
        while True:
            quess = int(input("Твоя попытка: "))
            attempts += 1 
            if quess == secret:
                print(f"\n🎉 УГАДАЛ! За {attempts} попыток!")
                total_game += 1
                if attempts < best_result:
                    best_result == attempts
                else:
                    best_result == best_result
                break
            elif quess < secret:
                print("📈 Больше!")
            else:
                print("📉 Меньше!")
        print("\nЕщё раз? (да/нет)")
    else:
        max_num = 500
        secret = random.randint(1, max_num)
        attempts = 0
        print(f"\nЯ загадал число от 1 до {max_num}")
        print("Попробуй угадать!\n")
        while True:
            quess = int(input("Твоя попытка: "))
            attempts += 1 
            if quess == secret:
                print(f"\n🎉 УГАДАЛ! За {attempts} попыток!")
                total_game += 1
                if attempts < best_result:
                    best_result == attempts
                else:
                    best_result == best_result
                break
            elif quess < secret:
                print("📈 Больше!")
            else:
                print("📉 Меньше!")
        print("\nЕщё раз? (да/нет)")
    next_game = input(":")
    if next_game == play_again:
        continue
    else: 
        print("всего игры было сиграно:{total_game}")
        print("Your best result: {best_result}")
        print("good luck")
        break    

        