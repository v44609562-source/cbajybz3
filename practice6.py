# Practice 5: Словари

# 1. Базовые операции
person = {
    "name": "Марк",
    "age": 16,
    "city": "Беларусь",
    "goals": ["$15M", "Топ-10%", "Ideal body"]
}

# Доступ к данным
print("Имя:", person["name"])
print("Цели:", person["goals"])

# Добавление ключа
person["skill"] = "Python"
print("Навык:", person["skill"])

# 2. Методы словарей
print("\nВсе ключи:", list(person.keys()))
print("Все значения:", list(person.values()))

# 3. Цикл по словарю
print("\n=== МОЙ ПРОФИЛЬ ===")
for key, value in person.items():
    print(f"{key}: {value}")

# 4. Проверка ключа
if "skill" in person:
    print("\nНавык найден!")

# 5. get() — безопасное получение
salary = person.get("salary", "Пока $0")
print("Зарплата:", salary)

# 6. Вложенные словари
learning_plan = {
    "Python": {
        "level": "beginner",
        "hours_done": 26,
        "goal": 200
    },
    "AI": {
        "level": "beginner", 
        "hours_done": 10,
        "goal": 500
    }
}

print("\n=== ПЛАН ОБУЧЕНИЯ ===")
for subject, data in learning_plan.items():
    progress = (data["hours_done"] / data["goal"]) * 100
    print(f"\n{subject}:")
    print(f"  Уровень: {data['level']}")
    print(f"  Прогресс: {data['hours_done']}/{data['goal']} часов ({progress:.1f}%)")
    
    bar = "█" * int(progress/5) + "░" * (20-int(progress/5))
    print(f"  [{bar}]")

# 7. Практическая задача: подсчёт слов
text = "python python ai python ai programming ai python"
words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\n=== ПОДСЧЁТ СЛОВ ===")
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {count} раз")