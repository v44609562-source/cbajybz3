# Библиотека промптов для разных задач

import json
import os

FILE = "prompts.json"

def load_prompts():
    if os.path.exists(FILE):
        with open(FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_prompts(data):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_prompt():
    prompts = load_prompts()
    
    print("\n=== ДОБАВИТЬ ПРОМПТ ===")
    category = input("Категория (код/контент/бизнес/другое): ")
    name = input("Название: ")
    template = input("Шаблон промпта: ")
    
    if category not in prompts:
        prompts[category] = []
    
    prompts[category].append({
        "name": name,
        "template": template
    })
    
    save_prompts(prompts)
    print("✅ Промпт сохранён!")

def show_prompts():
    prompts = load_prompts()
    
    if not prompts:
        print("❌ Нет промптов")
        return
    
    print("\n=== БИБЛИОТЕКА ПРОМПТОВ ===\n")
    
    for category, items in prompts.items():
        print(f"📁 {category.upper()}")
        for i, prompt in enumerate(items, 1):
            print(f"  {i}. {prompt['name']}")
            print(f"     {prompt['template'][:60]}...")
        print()

def search_prompt():
    prompts = load_prompts()
    keyword = input("Поиск: ").lower()
    
    found = []
    for category, items in prompts.items():
        for prompt in items:
            if keyword in prompt['name'].lower() or keyword in prompt['template'].lower():
                found.append((category, prompt))
    
    if found:
        print(f"\n🔍 Найдено: {len(found)}\n")
        for cat, p in found:
            print(f"[{cat}] {p['name']}")
            print(f"{p['template']}\n")
    else:
        print("❌ Ничего не найдено")

# Стартовые промпты
def init_library():
    prompts = {
        "код": [
            {
                "name": "Объяснить код",
                "template": "Объясни этот код простыми словами, как будто мне 16 лет: [КОД]"
            },
            {
                "name": "Найти баги",
                "template": "Проверь этот код на ошибки и предложи исправления: [КОД]"
            }
        ],
        "контент": [
            {
                "name": "Пост для соцсетей",
                "template": "Напиши пост для [ПЛАТФОРМА] на тему [ТЕМА]. Стиль: [СТИЛЬ]. Длина: [ДЛИНА]"
            }
        ],
        "бизнес": [
            {
                "name": "Холодное письмо",
                "template": "Напиши холодное письмо для [НИША]. Предложение: [ЧТО ПРЕДЛАГАЮ]. Цель: [ЦЕЛЬ]"
            }
        ]
    }
    
    if not os.path.exists(FILE):
        save_prompts(prompts)
        print("✅ Библиотека инициализирована с базовыми промптами")

# Меню
init_library()

while True:
    print("\n--- PROMPT LIBRARY ---")
    print("1. Показать все")
    print("2. Добавить промпт")
    print("3. Поиск")
    print("4. Выход")
    
    choice = input("\nВыбор: ")
    
    if choice == "1":
        show_prompts()
    elif choice == "2":
        add_prompt()
    elif choice == "3":
        search_prompt()
    elif choice == "4":
        print("👋 Удачи с промптами!")
        break