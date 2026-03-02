import anthropic
import os

# Если нет API ключа — пропусти эту программу
# Это просто концепция как работают агенты

print("=== ПРОСТОЙ AI АГЕНТ ===\n")

# Инструменты (tools)
def calculator(expression):
    """Калькулятор"""
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Ошибка вычисления"

def get_weather(city):
    """Погода (упрощённо)"""
    import requests
    try:
        url = f"http://wttr.in/{city}?format=%t"
        response = requests.get(url, timeout=5)
        return response.text
    except:
        return "Не удалось получить погоду"

def search_web(query):
    """Поиск (симуляция)"""
    # В реальности здесь был бы API Google
    responses = {
        "курс доллара": "1 USD = 3.27 BYN",
        "население минска": "~2 миллиона человек",
        "python": "Язык программирования"
    }
    return responses.get(query.lower(), f"Информация про '{query}' не найдена")

# Описание инструментов для AI
TOOLS = """
Доступные инструменты:

1. calculator(expression) - посчитать математическое выражение
   Пример: calculator("2 + 2 * 3")

2. get_weather(city) - узнать погоду в городе
   Пример: get_weather("Minsk")

3. search_web(query) - поиск информации
   Пример: search_web("курс доллара")
"""

def execute_tool(tool_name, args):
    """Выполняет инструмент"""
    if tool_name == "calculator":
        return calculator(args)
    elif tool_name == "get_weather":
        return get_weather(args)
    elif tool_name == "search_web":
        return search_web(args)
    else:
        return "Неизвестный инструмент"

# Простой агент (без настоящего LLM, просто логика)
def simple_agent(user_goal):
    """Упрощённый агент - показывает концепцию"""
    
    print(f"🎯 Цель: {user_goal}\n")
    print("🤖 Агент думает...\n")
    
    # Простая логика (в реале здесь был бы LLM)
    goal_lower = user_goal.lower()
    
    if "посчитай" in goal_lower or "сколько" in goal_lower:
        # Ищем выражение
        import re
        match = re.search(r'[\d\+\-\*/\(\)\s]+', user_goal)
        if match:
            expression = match.group()
            print(f"📋 Шаг 1: Использую calculator('{expression}')")
            result = calculator(expression)
            print(f"✅ Результат: {result}\n")
            return f"Ответ: {result}"
    
    elif "погода" in goal_lower:
        # Ищем город
        if "минск" in goal_lower:
            city = "Minsk"
        elif "москва" in goal_lower:
            city = "Moscow"
        else:
            city = "Minsk"
        
        print(f"📋 Шаг 1: Использую get_weather('{city}')")
        result = get_weather(city)
        print(f"✅ Результат: {result}\n")
        return f"Погода в {city}: {result}"
    
    elif "курс" in goal_lower or "доллар" in goal_lower:
        print("📋 Шаг 1: Использую search_web('курс доллара')")
        result = search_web("курс доллара")
        print(f"✅ Результат: {result}\n")
        return result
    
    else:
        return "Не могу обработать этот запрос (агент слишком простой)"

# Тестирование
print("=== ДЕМОНСТРАЦИЯ АГЕНТА ===\n")

examples = [
    "Посчитай сколько будет 125 * 8 + 42",
    "Какая погода в Минске?",
    "Узнай курс доллара"
]

for example in examples:
    result = simple_agent(example)
    print(f"💬 Ответ пользователю: {result}\n")
    print("-" * 50 + "\n")

# Интерактивный режим
print("\n=== ПОПРОБУЙ САМ ===")
print("Примеры запросов:")
print("- Посчитай 50 * 20")
print("- Какая погода в Минске?")
print("- Курс доллара\n")

while True:
    user_input = input("Твой запрос (или 'выход'): ")
    
    if user_input.lower() == "выход":
        break
    
    result = simple_agent(user_input)
    print(f"\n🤖 {result}\n")