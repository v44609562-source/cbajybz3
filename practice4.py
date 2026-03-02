# Practice 4: Работа со списками

print("=== СПИСКИ: ОСНОВЫ ===\n")

# 1. Создание списка
goals = ["iPhone 15", "Ideal body", "First $100", "Master AI", "Discipline"]
print("Мои цели:", goals)
print("Количество целей:", len(goals))

# 2. Доступ к элементам
print("\nПервая цель:", goals[0])
print("Последняя цель:", goals[-1])

# 3. Добавление элемента
goals.append("$15M к 30")
print("\nПосле добавления:", goals)

# 4. Вставка в определенное место
goals.insert(0, "Пройти неделю без пропусков")
print("После вставки в начало:", goals)

# 5. Удаление
goals.remove("iPhone 15")  # когда куплю
print("\nПосле удаления iPhone:", goals)

# 6. Сортировка
numbers = [10, 3, 7, 1, 5, 9, 2]
numbers.sort()
print("\nОтсортированные числа:", numbers)

# В обратном порядке
numbers.sort(reverse=True)
print("В обратном порядке:", numbers)

# 7. Цикл по списку
print("\n=== МОИ ЦЕЛИ (НУМЕРОВАННЫЙ СПИСОК) ===")
for i, goal in enumerate(goals, 1):
    print(f"{i}. {goal}")

# 8. Проверка наличия элемента
if "Discipline" in goals:
    print("\n✅ Дисциплина в списке целей!")
else:
    print("\n❌ Дисциплины нет в списке!")

# 9. Срезы (slices)
print("\nПервые 3 цели:", goals[:3])
print("Последние 2 цели:", goals[-2:])

# 10. Копирование списка
goals_backup = goals.copy()
print("\nБэкап целей:", goals_backup)

# 11. Практическая задача: список задач на сегодня
today_tasks = [
    "Прочитать Chapter 4",
    "Написать practice4.py",
    "Создать program16",
    "Отчёт учителю"
]

print("\n=== ЗАДАЧИ НА СЕГОДНЯ ===")
completed = 0

for i, task in enumerate(today_tasks, 1):
    print(f"{i}. [ ] {task}")
    
print(f"\nВыполнено: {completed}/{len(today_tasks)}")

# 12. Фильтрация списка
all_goals = ["iPhone", "MacBook", "Ideal body", "Car", "First $100"]
affordable_goals = []

for goal in all_goals:
    if "body" in goal.lower() or "$" in goal:
        affordable_goals.append(goal)

print("\nДоступные цели (не требуют денег):", affordable_goals)

print("\n=== ПРАКТИКА ЗАВЕРШЕНА ===")



