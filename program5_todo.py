# Программа: Простой TODO список

print("=== МОЙ TODO СПИСОК ===\n")

# Список задач
tasks = []

while True:
    print("\n--- МЕНЮ ---")
    print("1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Удалить задачу")
    print("4. Выход")
    
    choice = input("\nВыбери действие (1-4): ")
    
    if choice == "1":
        # Добавить задачу
        task = input("Введи задачу: ")
        tasks.append(task)
        print(f"✅ Задача добавлена: {task}")
    
    elif choice == "2":
        # Показать задачи
        if len(tasks) == 0:
            print("\n📝 Список пуст. Добавь задачи!")
        else:
            print("\n📝 ТВОИ ЗАДАЧИ:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    
    elif choice == "3":
        # Удалить задачу
        if len(tasks) == 0:
            print("\n❌ Список пуст. Нечего удалять!")
        else:
            print("\n📝 ТВОИ ЗАДАЧИ:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            
            num = int(input("\nНомер задачи для удаления: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"❌ Удалена: {removed}")
            else:
                print("❌ Неверный номер!")
    
    elif choice == "4":
        # Выход
        print("\n👋 Пока! Продуктивного дня!")
        break
    
    else:
        print("❌ Неверный выбор. Попробуй снова.")