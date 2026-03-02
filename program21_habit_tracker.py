# Program 21: Трекер привычек (как в приложениях)

import json
import os
from datetime import datetime, timedelta

FILENAME = "habits.json"

def load_habits():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_habits(habits):
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(habits, f, ensure_ascii=False, indent=2)

def add_habit():
    habits = load_habits()
    
    name = input("\nНазвание привычки: ")
    goal = input("Сколько раз в неделю? (1-7): ")
    
    habits[name] = {
        "goal": int(goal),
        "history": []
    }
    
    save_habits(habits)
    print(f"✅ Привычка '{name}' добавлена!")

def check_in():
    habits = load_habits()
    
    if not habits:
        print("❌ Нет привычек. Добавь сначала.")
        return
    
    print("\n=== ТВОИ ПРИВЫЧКИ ===")
    habit_list = list(habits.keys())
    
    for i, name in enumerate(habit_list, 1):
        print(f"{i}. {name}")
    
    choice = int(input("\nКакую привычку выполнил? ")) - 1
    habit_name = habit_list[choice]
    
    today = str(datetime.now().date())
    
    if today in habits[habit_name]["history"]:
        print("✅ Ты уже отметился сегодня!")
        return
    
    habits[habit_name]["history"].append(today)
    save_habits(habits)
    
    print(f"🔥 Отлично! '{habit_name}' выполнена сегодня!")
    
    # Проверка streak
    streak = calculate_streak(habits[habit_name]["history"])
    print(f"⚡ Streak: {streak} дней подряд!")

def calculate_streak(history):
    if not history:
        return 0
    
    history = sorted(history, reverse=True)
    streak = 0
    
    for i, date_str in enumerate(history):
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        expected_date = datetime.now().date() - timedelta(days=i)
        
        if date == expected_date:
            streak += 1
        else:
            break
    
    return streak

def show_stats():
    habits = load_habits()
    
    if not habits:
        print("❌ Нет привычек")
        return
    
    print("\n=== СТАТИСТИКА ПРИВЫЧЕК ===\n")
    
    for name, data in habits.items():
        goal = data["goal"]
        history = data["history"]
        
        # Эта неделя
        today = datetime.now().date()
        week_start = today - timedelta(days=today.weekday())
        
        this_week = [d for d in history if datetime.strptime(d, "%Y-%m-%d").date() >= week_start]
        
        # Streak
        streak = calculate_streak(history)
        
        # Процент выполнения
        percent = (len(this_week) / goal) * 100 if goal > 0 else 0
        
        print(f"📌 {name}")
        print(f"   Цель: {goal} раз/неделю")
        print(f"   Эта неделя: {len(this_week)}/{goal}")
        print(f"   Прогресс: {percent:.0f}%")
        print(f"   Streak: {streak} дней 🔥")
        
        # Прогресс-бар
        filled = int(percent / 5)
        bar = "█" * min(filled, 20) + "░" * max(20 - filled, 0)
        print(f"   [{bar}]")
        
        if percent >= 100:
            print("   🎉 Цель недели выполнена!")
        elif percent >= 70:
            print("   💪 Почти там!")
        
        print()

# Меню
while True:
    print("\n--- HABIT TRACKER ---")
    print("1. Добавить привычку")
    print("2. Отметить выполнение")
    print("3. Статистика")
    print("4. Выход")
    
    choice = input("\nВыбери (1-4): ")
    
    if choice == "1":
        add_habit()
    elif choice == "2":
        check_in()
    elif choice == "3":
        show_stats()
    elif choice == "4":
        print("\n👋 Продолжай строить привычки!")
        break
    else:
        print("❌ Неверный выбор")