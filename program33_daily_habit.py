# Простой трекер ежедневной привычки

import json
import os
from datetime import datetime

FILE = "habit_data.json"

def load():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    return {"dates": [], "streak": 0}

def save(data):
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=2)

def check_in():
    data = load()
    today = datetime.now().strftime("%Y-%m-%d")
    
    if today in data["dates"]:
        print("✅ Уже отметился сегодня!")
        return
    
    data["dates"].append(today)
    data["streak"] += 1
    save(data)
    
    print(f"🔥 День {data['streak']}!")

def stats():
    data = load()
    print(f"\n📊 Всего дней: {len(data['dates'])}")
    print(f"🔥 Текущий streak: {data['streak']}")

while True:
    print("\n1. Отметиться\n2. Статистика\n3. Выход")
    c = input("Выбор: ")
    if c == "1": check_in()
    elif c == "2": stats()
    elif c == "3": break