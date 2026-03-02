import json
import os
import random
from datetime import datetime

FILE = "expenses.json"

    
def load_expense():
    if os.path.exists(FILE):
        with open(FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return[]

def save_expense(data):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent = 2)

def add_expense():
    categories = ["Еда", "Транспорт", "Развлечения", "Обучение", "Здоровье"]
    print("Категории:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    choice = int(input("Выбери: "))
    category = categories[choice - 1]
    amount = float(input("сколько:"))
    discription  = input("Где:")
    data  = datetime.now().strftime("%d.%m.%Y")
    expense =  load_expense()



    spent={
        "id": random .randint(1000, 9999),
        "category": category,
        "amount": amount,
        "description": discription, 
        "date":  data,
        "created": datetime.now().strftime("%d.%m.%Y %H:%M")  

}
    
    expense.append(spent)
    save_expense(expense)
    print(f"\n✅ Добавлено! ID: {spent['id']}")



def show_all():
    expense = load_expense()
    if not expense:
        print("no expense")
        return
    print (f"\n=== МОИ РАСХОДЫ ({len(expense)}) ===\n")
    total_sum = 0 
    for item in  expense:
        date = item.get('date', 'Нет даты')
        category = item.get('category', 'Разное')
        amount = item.get('amount', 0)
        description = item.get('description', '')
        total_sum += amount
        print(f"{date} | [{category}] {amount} BYN")
        print(f"  {description}\n")
    print("-" * 25) # Просто красивая линия
    print(f"Итого: {total_sum} BYN")

def stats_by_category():
    expense = load_expense()
    if not expense:
        print("Данных для статистики нет.")
        return
    category_map = {}
    total_sum = 0
    for item in expense:
        cat = item.get('category', 'Разное')
        amount = item.get('amount', 0)
        if cat not in category_map:
            category_map[cat] = 0
        category_map[cat] += amount
        total_sum += amount
    print("\n📊 СТАТИСТИКА ПО КАТЕГОРИЯМ\n")
    for car, sum_val in category_map.items():
        percent= (sum_val/total_sum)*100
        bar_length = int(percent/5)
        bar = "█" * bar_length + "░" * (20 - bar_length)
        print(f"{cat}: {sum_val} BYN ({percent:.1f}%)")
        print(F"{bar}\n")
        print(f"итогоЖ {total_sum} BYN")

def  stats_by_month():
    expense = load_expense()
    if not expense:
        print("База пуста.")
        return
    print("\n--- Выберите номер месяца (01-12) ---")
    month = input("Введите месяц (например, 02): ")
    filtered = [e for e in expense if f".{month}." in e.get("date","")]
    if not filtered:
        print(f"За месяц {month} расходов не найдено.")
        return
    total_count = len(filtered)
    total_sum = sum(item.get ('amount', 0 ) for item in filtered)
    average_check = total_sum/total_count
    category_map = {}
    for item in filtered:
        cat = item.get('category','разное')
        category_map[cat] = category_map.get(cat, 0) + item.get('amount',0)
    print(f"\n📅 СТАТИСТИКА ЗА МЕСЯЦ {month}")
    print(f"Всего расходов: {total_count}")
    print(f"Сумма: {total_sum} BYN")
    print(f"Средний чек: {average_check:.1f} BYN")   
    print("\nПо категориям:")
    for cat, sum_val in category_map.items():
        print(f"  {cat}: {sum_val} BYN")


def delete_expense():
    expense = load_expense()
    show_all()
    expense_id = int(input("\n ID expense for delete:"))
    for i, item in enumerate(expense):
        if item["id"] == expense_id:
            confirm = input(f"Удалить {item['amount']} BYN? (yes/no): ")
            if confirm.lower() == "yes":
                expense.pop(i)
                save_expense(expense)
                print("\n✅ Клиент удалён")
            else:
                print("\n❌ Отменено")
            return
        print("\n❌ Клиент не найден") 

print("=== menu expense ===\n")
while True:
    print("---menu---")
    print("1. Добавить расходы")
    print("2. Показать все расходы")
    print("3. Сортировка по месяцу")
    print("4. Сортировка по тратам ")
    print("5. удалить трату ")
    print("6. Выход ")
   
    choice = input("\nВыбери (1-6): ")
    if choice == "1":
       add_expense()
    elif choice == "2":
        show_all()
    elif choice == "3":
        stats_by_month()
    elif choice == "4":
        stats_by_category()
    elif choice == "5":
        delete_expense()
    elif choice == "6":
         print("\n👋 Пока!")
         break
    else:
        print("❌ Неверный выбор")