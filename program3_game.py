# Программа 3: Игра "Угадай число"

import random

print("=== ИГРА: УГАДАЙ ЧИСЛО ===")
print("Я загадал число от 1 до 100")
print("У тебя 7 попыток\n")

# Загадываем случайное число
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

# Игровой цикл
while attempts < max_attempts:
    # Спрашиваем число
    guess = int(input("Попытка " + str(attempts + 1) + ": "))
    attempts = attempts + 1
    
    # Проверяем
    if guess == secret_number:
        print("\n🎉 ПОБЕДА! Ты угадал!")
        print("Попыток потрачено:", attempts)
        break
    elif guess < secret_number:
        remaining = max_attempts - attempts
        print("❌ Моё число БОЛЬШЕ! Осталось попыток:", remaining)
    else:
        remaining = max_attempts - attempts
        print("❌ Моё число МЕНЬШЕ! Осталось попыток:", remaining)
else:
    print("\n💀 ПРОИГРАЛ! Попытки кончились.")
    print("Загаданное число было:", secret_number)

print("\n--- ИГРА ОКОНЧЕНА ---")