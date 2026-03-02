# Программа: Трекер прогресса обучения

print("=== ТРЕКЕР ПРОГРЕССА ===\n")

# Данные
name = input("Твоё имя: ")
goal = input("Твоя цель (например: '$10k/мес'): ")

print(f"\nПривет, {name}!")
print(f"Твоя цель: {goal}\n")

# Прогресс за сегодня
hours = float(input("Сколько часов учился сегодня? "))
programs = int(input("Сколько программ написал? "))
chapters = int(input("Сколько глав прочитал? "))

# Анализ
print("\n=== АНАЛИЗ СЕГОДНЯШНЕГО ДНЯ ===")

if hours >= 4:
    print(f"⭐ {hours} часов — отличная работа!")
elif hours >= 2:
    print(f"✅ {hours} часов — хороший темп!")
elif hours >= 1:
    print(f"⚠️ {hours} часов — мало, постарайся больше завтра.")
else:
    print(f"❌ {hours} часов — это почти ничего. Соберись!")

if programs > 0:
    print(f"💻 {programs} программ написано — продуктивно!")
else:
    print("❌ Ни одной программы — завтра исправь!")

if chapters > 0:
    print(f"📖 {chapters} глав прочитано — молодец!")
else:
    print("⚠️ Теории не было — не забывай читать!")

# Прогноз
print("\n=== ПРОГНОЗ ===")
days_to_goal = 90  # 3 месяца
total_hours = hours * days_to_goal
total_programs = programs * days_to_goal

print(f"Если будешь работать так же каждый день:")
print(f"- За 3 месяца: {total_hours} часов обучения")
print(f"- Программ напишешь: {total_programs}")

if total_hours >= 200:
    print("\n🔥 При таком темпе цель достижима!")
else:
    print("\n⚠️ Нужно больше стараться для достижения цели.")

print(f"\n💪 {name}, продолжай! Ты на правильном пути!")