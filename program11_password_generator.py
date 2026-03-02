# Программа 11: Генератор надёжных паролей

import random
import string

print("=== ГЕНЕРАТОР ПАРОЛЕЙ ===\n")

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Генерирует пароль по заданным параметрам"""
    
    # Формируем набор символов
    characters = ""
    
    if use_lower:
        characters += string.ascii_lowercase  # abcdefg...
    if use_upper:
        characters += string.ascii_uppercase  # ABCDEFG...
    if use_digits:
        characters += string.digits  # 0123456789
    if use_symbols:
        characters += string.punctuation  # !@#$%^&*...
    
    # Проверка что хоть что-то выбрано
    if not characters:
        return None
    
    # Генерируем пароль
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def check_password_strength(password):
    """Оценивает надёжность пароля"""
    
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    
    # Подсчёт баллов
    score = 0
    
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1
    
    # Оценка
    if score <= 2:
        return "❌ Слабый", score
    elif score <= 4:
        return "⚠️ Средний", score
    elif score <= 6:
        return "✅ Хороший", score
    else:
        return "🔥 Отличный", score

# Главное меню
while True:
    print("\n--- МЕНЮ ---")
    print("1. Сгенерировать пароль")
    print("2. Проверить надёжность пароля")
    print("3. Сгенерировать несколько паролей")
    print("4. Выход")
    
    choice = input("\nВыбери действие (1-4): ")
    
    if choice == "1":
        # Генерация одного пароля
        print("\n=== НАСТРОЙКИ ПАРОЛЯ ===")
        
        length = int(input("Длина пароля (8-32): "))
        if length < 8:
            length = 8
        if length > 32:
            length = 32
        
        use_lower = input("Маленькие буквы (a-z)? (да/нет): ").lower() == "да"
        use_upper = input("Большие буквы (A-Z)? (да/нет): ").lower() == "да"
        use_digits = input("Цифры (0-9)? (да/нет): ").lower() == "да"
        use_symbols = input("Символы (!@#$...)? (да/нет): ").lower() == "да"
        
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        
        if password:
            print(f"\n🔐 Твой пароль: {password}")
            
            # Проверка надёжности
            strength, score = check_password_strength(password)
            print(f"Надёжность: {strength} ({score}/7 баллов)")
        else:
            print("\n❌ Ошибка: выбери хотя бы один тип символов!")
    
    elif choice == "2":
        # Проверка пароля
        print("\n=== ПРОВЕРКА ПАРОЛЯ ===")
        password = input("Введи пароль для проверки: ")
        
        strength, score = check_password_strength(password)
        
        print(f"\nПароль: {password}")
        print(f"Длина: {len(password)} символов")
        print(f"Надёжность: {strength} ({score}/7 баллов)")
        
        # Рекомендации
        if score < 5:
            print("\n💡 РЕКОМЕНДАЦИИ:")
            if len(password) < 12:
                print("- Сделай пароль длиннее (минимум 12 символов)")
            if not any(c.isupper() for c in password):
                print("- Добавь большие буквы (A-Z)")
            if not any(c.islower() for c in password):
                print("- Добавь маленькие буквы (a-z)")
            if not any(c.isdigit() for c in password):
                print("- Добавь цифры (0-9)")
            if not any(c in string.punctuation for c in password):
                print("- Добавь символы (!@#$%)")
    
    elif choice == "3":
        # Несколько паролей
        print("\n=== ПАКЕТНАЯ ГЕНЕРАЦИЯ ===")
        
        count = int(input("Сколько паролей сгенерировать (1-10)? "))
        if count < 1:
            count = 1
        if count > 10:
            count = 10
        
        length = int(input("Длина каждого пароля (8-32): "))
        if length < 8:
            length = 8
        if length > 32:
            length = 32
        
        print("\nНастройки (да/нет для всех):")
        use_lower = input("Маленькие буквы? ").lower() == "да"
        use_upper = input("Большие буквы? ").lower() == "да"
        use_digits = input("Цифры? ").lower() == "да"
        use_symbols = input("Символы? ").lower() == "да"
        
        print(f"\n🔐 СГЕНЕРИРОВАННЫЕ ПАРОЛИ:\n")
        
        for i in range(count):
            password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            if password:
                strength, score = check_password_strength(password)
                print(f"{i+1}. {password} — {strength}")
            else:
                print(f"{i+1}. Ошибка генерации")
    
    elif choice == "4":
        print("\n👋 До встречи! Храни пароли в безопасности!")
        break
    
    else:
        print("\n❌ Неверный выбор. Попробуй снова.")

print("\n=== ПРОГРАММА ЗАВЕРШЕНА ===")
  