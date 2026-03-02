import json
import os
import random
from datetime import datetime

FILE = "clients.json"



def load_data():
    if os.path.exists(FILE):
        with open(FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return [] 

def load_clients():
    if os.path.exists(FILE):
        with open(FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_clients(data):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_client():
    clients=load_clients()
    name = input("Имя: ")
    email= input("Email: ")
    phone= input("Телефон: ")

    client = {
        "id": random.randint(1000,9999),
        "name": name,
        "email": email,
        "phone": phone,
        "status": "new",
        "created": datetime.now().strftime("%d.%m.%Y %H:%M")  

    }

    clients.append(client)
    save_clients(clients)
    print(f"\n✅ Клиент добавлен! ID: {client['id']}")

def show_all():
    clients = load_clients()

    if not clients:
        print("no client")
        return
    
    priority = {
        "new": 1,
        "contact": 2,
        "offer": 3,
        "close": 4,
    }

    sorted_clients = sorted(clients, key=lambda c: priority.get(c["status"],999))

    print (f"\n=== МОИ КЛИЕНТЫ ({len(clients)}) ===\n")

    for client in sorted_clients:
        print(f"[{client['status']}] ID: {client['id']} | {client['name']}")
        print(f"  📧 {client['email']}")
        print(f"  📱 {client['phone']}\n")
        print(f"  📅 Добавлен: {client.get('created', 'неизвестно')}\n")

def search_client():
    clients = load_clients()
    keyword = input("search:").lower()
    found = [c for c in clients if keyword in c ["name"].lower()]

    if found:
        print(f"🔍 Найдено: {len(found)}\n")
        for c in found:
            print(f"[{c['status']}] {c['name']} | {c['email']}")
    else:
        print("❌ Ничего не найдено")

def change_status():
    clients = load_clients()
    client_id = int(input("id clients"))
    for client in clients:
        if client ["id"] == client_id:
            client["status"] = input("new status")
            save_clients(clients)
            break

def stats():
    clients = load_clients()
    total = len(clients)
    statuses = {}
    for c in clients:
        status = c["status"]
        statuses[status] = statuses.get(status, 0) +1

    print(f"Всего: {total}\n")
    for status, count in statuses.items():
        percent= (count/total) * 100
        print(f"{status}:{count}({percent:.0f}%)")

def delete_client():
    clients = load_clients()
    show_all()
    client_id = int(input("\nID клиента для удаления: "))
    for i, client in enumerate(clients):
        if client ["id"] == client_id:
            confirm = input(f"Удалить {client['name']}? (да/нет): ")
            if confirm.lower() == "да":
                clients.pop(i)
                save_clients(clients)
                print("\n✅ Клиент удалён")
            else:
                print("\n❌ Отменено")
            return
    print("\n❌ Клиент не найден") 
         
print("=== MINI CRM ===\n")
while True:
    print("--- МЕНЮ ---")
    print("1.  Добавить клиента")
    print("2. Показать всех клиентов")
    print("3.  Поиск по имени")
    print("4. Изменить статус")
    print("5. Статистика")
    print("6. удалить клиента")
    print("7. выход")
    
    choice = input("\nВыбери (1-7): ")
    if choice == "1":
        add_client()
    elif choice == "2":
        show_all()
    elif choice == "3":
        search_client()
    elif choice == "4":
        change_status()
    elif choice == "5":
        stats()
    elif choice == "6":
        delete_client()
    elif choice == "7":
         print("\n👋 Пока!")
         break
    else:
        print("❌ Неверный выбор")