import requests

print("=== КОНВЕРТЕР ВАЛЮТ ===")
print("Используем реальные курсы с API\n")

def get_rates():
    """Получаем реальные курсы валют"""
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url, timeout=5)
        data = response.json()
        return data["rates"]
    except:
        print("❌ Нет интернета, используем примерные курсы")
        return {
            "USD": 1,
            "EUR": 0.92,
            "BYN": 3.27,
            "RUB": 90.5,
            "UAH": 41.2
        }

def convert(amount, from_currency, to_currency, rates):
    """Конвертация валют"""
    if from_currency not in rates or to_currency not in rates:
        return None
    
    # Сначала переводим в USD, потом в нужную валюту
    in_usd = amount / rates[from_currency]
    result = in_usd * rates[to_currency]
    return round(result, 2)

# Загружаем курсы
print("Загружаю курсы валют...")
rates = get_rates()
print("✅ Курсы загружены!\n")

# Основные валюты
main_currencies = ["USD", "EUR", "BYN", "RUB", "UAH"]

while True:
    print("\n--- МЕНЮ ---")
    print("1. Конвертировать валюту")
    print("2. Посмотреть курсы")
    print("3. Сколько нужно заработать (в BYN)")
    print("4. Выход")
    
    choice = input("\nВыбери (1-4): ")
    
    if choice == "1":
        print("\nВалюты:", ", ".join(main_currencies))
        
        from_cur = input("Из какой валюты: ").upper()
        to_cur = input("В какую валюту: ").upper()
        amount = float(input("Сумма: "))
        
        result = convert(amount, from_cur, to_cur, rates)
        
        if result:
            print(f"\n💰 {amount} {from_cur} = {result} {to_cur}")
        else:
            print("❌ Неверная валюта")
    
    elif choice == "2":
        print("\n=== КУРСЫ К USD ===")
        for cur in main_currencies:
            if cur in rates:
                print(f"1 USD = {rates[cur]} {cur}")
    
    elif choice == "3":
        print("\n=== КАЛЬКУЛЯТОР ЦЕЛИ ===")
        goal_usd = float(input("Цель в USD (например 10000): "))
        
        print(f"\n${goal_usd}/мес = ")
        for cur in ["BYN", "EUR", "RUB"]:
            if cur in rates:
                amount = convert(goal_usd, "USD", cur, rates)
                print(f"  {amount} {cur}")
        
        print(f"\n💡 Это {goal_usd * 12:,.0f} USD в год")
        print(f"Или {convert(goal_usd * 12, 'USD', 'BYN', rates):,.0f} BYN в год")
    
    elif choice == "4":
        print("\n👋 Пока!")
        break
    
    else:
        print("❌ Неверный выбор")