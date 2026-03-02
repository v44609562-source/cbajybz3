# program25_bmi_calculator.py

print("=== КАЛЬКУЛЯТОР ИНДЕКСА МАССЫ ТЕЛА ===\n")

def calculate_bmi(weight, height):
    """Вычисляет BMI"""
    bmi = weight / (height ** 2)
    return round(bmi, 1)

def get_category(bmi):
    """Определяет категорию"""
    if bmi < 18.5:
        return "Недостаточный вес", "⚠️"
    elif bmi < 25:
        return "Нормальный вес", "✅"
    elif bmi < 30:
        return "Избыточный вес", "⚠️"
    else:
        return "Ожирение", "❌"

def ideal_weight_range(height):
    """Идеальный вес для роста"""
    min_weight = 18.5 * (height ** 2)
    max_weight = 24.9 * (height ** 2)
    return round(min_weight, 1), round(max_weight, 1)

# Главная программа
while True:
    print("\n--- МЕНЮ ---")
    print("1. Рассчитать BMI")
    print("2. Узнать идеальный вес")
    print("3. Трекер прогресса (цель)")
    print("4. Выход")
    
    choice = input("\nВыбери (1-4): ")
    
    if choice == "1":
        weight = float(input("\nВес (кг): "))
        height = float(input("Рост (метры, например 1.75): "))
        
        bmi = calculate_bmi(weight, height)
        category, emoji = get_category(bmi)
        
        print(f"\n{emoji} BMI: {bmi}")
        print(f"Категория: {category}")
        
        if bmi < 18.5:
            print("💡 Рекомендация: набрать вес")
        elif bmi > 25:
            print("💡 Рекомендация: снизить вес")
        else:
            print("💡 Отличный результат!")
    
    elif choice == "2":
        height = float(input("\nРост (метры): "))
        min_w, max_w = ideal_weight_range(height)
        
        print(f"\n📊 Идеальный вес для {height}м:")
        print(f"От {min_w} кг до {max_w} кг")
    
    elif choice == "3":
        current = float(input("\nТекущий вес (кг): "))
        goal = float(input("Целевой вес (кг): "))
        
        diff = abs(current - goal)
        direction = "сбросить" if current > goal else "набрать"
        
        print(f"\n🎯 Нужно {direction}: {diff} кг")
        
        weeks = diff / 0.5  # 0.5 кг в неделю — здоровый темп
        print(f"При темпе 0.5кг/нед: {int(weeks)} недель")
        print(f"Это примерно {int(weeks/4)} месяцев")
    
    elif choice == "4":
        print("\n👋 Удачи в достижении цели!")
        break
    
    else:
        print("❌ Неверный выбор")