# Программа: Счётчик дней до цели

import datetime

print("=== СЧЁТЧИК ДО ТВОЕЙ ЦЕЛИ ===\n")

# Сегодня
today = datetime.date.today()

# Твоя цель: первые $100 через 3 месяца
goal_date = datetime.date(2026, 5, 7)  # примерно через 3 месяца

# Расчёт
days_left = (goal_date - today).days
weeks_left = days_left // 7

print(f"Сегодня: {today.strftime('%d.%m.%Y')}")
print(f"Цель: первые $100 до {goal_date.strftime('%d.%m.%Y')}")
print(f"\nОсталось дней: {days_left}")
print(f"Это примерно {weeks_left} недель")

# Мотивация
if days_left > 60:
    print("\n💪 Времени много. Работай стабильно каждый день.")
elif days_left > 30:
    print("\n⚡ Времени достаточно. Не расслабляйся.")
else:
    print("\n🔥 Мало времени. Ускоряйся!")

# Что нужно делать
daily_hours = 3  # минимум
total_hours_left = days_left * daily_hours

print(f"\nЕсли работать по {daily_hours} часа в день:")
print(f"Всего часов обучения: {total_hours_left}")
print(f"Это {total_hours_left // 100} сотен часов практики!")

print("\n📌 ЗАВТРА ПРОДОЛЖАЙ. БЕЗ ОПРАВДАНИЙ.")