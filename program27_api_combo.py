import requests
from datetime import datetime

print("=== ЛИЧНЫЙ АССИСТЕНТ ===\n")

def get_weather(city="Minsk"):
    """Получить погоду"""
    try:
        url = f"http://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        current = data["current_condition"][0]
        temp = current["temp_C"]
        desc = current["weatherDesc"][0]["value"]
        
        return {
            "temp": temp,
            "description": desc,
            "city": city
        }
    except:
        return None

def get_currency_rate(from_cur="USD", to_cur="BYN"):
    """Курс валют"""
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_cur}"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        if to_cur in data["rates"]:
            return data["rates"][to_cur]
        return None
    except:
        return None

def get_motivation():
    """Случайная мотивация"""
    import random
    quotes = [
        "🔥 Ты не бросаешь. Это делает тебя сильнее.",
        "💪 Каждый день = шаг к цели.",
        "⚡ Тяжело? Хорошо. Легко было бы — все бы делали.",
        "🚀 Через 3 месяца ты поблагодаришь себя.",
        "🎯 Маленькие шаги = большой результат.",
        "💎 Ты строишь будущее. Не останавливайся.",
        "🔝 Топ-10% — это постоянство, не талант.",
        "⭐ Ты делаешь больше чем мечтатели.",
        "какая тебе мотивация жирный хуесос"
    ]
    return random.choice(quotes)

def morning_briefing():
    """Утренняя сводка"""
    print("☀️ ДОБРОЕ УТРО!\n")
    
    # Дата
    today = datetime.now()
    print(f"📅 {today.strftime('%A, %d %B %Y')}")
    print(f"⏰ {today.strftime('%H:%M')}\n")
    
    # Погода
    print("🌤️ ПОГОДА:")
    weather = get_weather("Minsk")
    if weather:
        print(f"   {weather['city']}: {weather['temp']}°C")
        print(f"   {weather['description']}\n")
    else:
        print("   ❌ Не удалось загрузить\n")
    
    # Валюты
    print("💰 КУРСЫ:")
    usd_byn = get_currency_rate("USD", "BYN")
    eur_byn = get_currency_rate("EUR", "BYN")
    
    if usd_byn:
        print(f"   1 USD = {usd_byn:.2f} BYN")
    if eur_byn:
        print(f"   1 EUR = {eur_byn:.2f} BYN")
    
    # Твои цели
    print("\n🎯 ТВОИ ЦЕЛИ:")
    print("   • Первые $100/мес")
    print("   • 30 программ на GitHub")
    print("   • Streak 7 дней")
    
    # Мотивация
    print(f"\n{get_motivation()}")

def goal_calculator():
    """Калькулятор цели"""
    print("\n💰 КАЛЬКУЛЯТОР ФИНАНСОВОЙ ЦЕЛИ\n")
    
    goal_usd = float(input("Цель в USD/мес: "))
    current_usd = float(input("Текущий доход USD/мес: "))
    
    # Конвертация в BYN
    rate = get_currency_rate("USD", "BYN")
    
    if rate:
        goal_byn = goal_usd * rate
        current_byn = current_usd * rate
        
        print(f"\n📊 АНАЛИЗ:")
        print(f"Цель: ${goal_usd} ({goal_byn:.0f} BYN)")
        print(f"Сейчас: ${current_usd} ({current_byn:.0f} BYN)")
        
        needed_usd = goal_usd - current_usd
        needed_byn = needed_usd * rate
        
        print(f"\nНужно заработать: ${needed_usd} ({needed_byn:.0f} BYN)")
        
        # Прогноз времени
        growth = float(input("\nРост в месяц (USD): "))
        months = needed_usd / growth if growth > 0 else 0
        
        print(f"\n⏱️ При росте ${growth}/мес:")
        print(f"Достигнешь цели за: {months:.1f} месяцев")
        print(f"Это примерно {months/12:.1f} года")

# Меню
while True:
    print("\n--- МЕНЮ ---")
    print("1. Утренняя сводка")
    print("2. Только погода")
    print("3. Только валюты")
    print("4. Мотивация")
    print("5. Калькулятор цели")
    print("6. Выход")
    
    choice = input("\nВыбери (1-6): ")
    
    if choice == "1":
        morning_briefing()
    
    elif choice == "2":
        city = input("Город (Enter = Minsk): ") or "Minsk"
        weather = get_weather(city)
        if weather:
            print(f"\n🌤️ {weather['city']}: {weather['temp']}°C, {weather['description']}")
        else:
            print("❌ Ошибка")
    
    elif choice == "3":
        print("\n💰 КУРСЫ К USD:")
        for cur in ["BYN", "EUR", "RUB", "UAH"]:
            rate = get_currency_rate("USD", cur)
            if rate:
                print(f"1 USD = {rate:.2f} {cur}")
    
    elif choice == "4":
        print(f"\n{get_motivation()}")
    
    elif choice == "5":
        goal_calculator()
    
    elif choice == "6":
        print("\n👋 Продуктивного дня!")
        break
    
    else:
        print("❌ Неверный выбор")