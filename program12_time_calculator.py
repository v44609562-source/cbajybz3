# Программа: Сколько времени до цели

import datetime

print("=== КАЛЬКУЛЯТОР ВРЕМЕНИ ===\n")

# Ввод
goal_money = int(input("Цель ($): "))
hours_per_day = int(input("Часов учёбы в день: "))

# Расчёты (примерные)
# Предположим: 100 часов = первые $100
# 500 часов = первые $1000
# 1000 часов = $5000+

if goal_money <= 100:
    hours_needed = 100
elif goal_money <= 1000:
    hours_needed = 500
elif goal_money <= 5000:
    hours_needed = 1000
else:
    hours_needed = 2000

days_needed = hours_needed / hours_per_day
weeks = days_needed / 7
months = days_needed / 30

print(f"\n=== РЕЗУЛЬТАТ ===")
print(f"Для цели ${goal_money}/мес нужно ~{hours_needed} часов обучения")
print(f"\nПри {hours_per_day} часах в день:")
print(f"📅 Дней: {int(days_needed)}")
print(f"📅 Недель: {int(weeks)}")
print(f"📅 Месяцев: {round(months, 1)}")

today = datetime.date.today()
target_date = today + datetime.timedelta(days=int(days_needed))

print(f"\n🎯 Примерная дата достижения: {target_date.strftime('%d.%m.%Y')}")

if months <= 3:
    print("\n🔥 Реально! Давай!")
elif months <= 6:
    print("\n💪 Амбициозно, но возможно!")
else:
    print("\n⚡ Долгий путь, но ты справишься!")