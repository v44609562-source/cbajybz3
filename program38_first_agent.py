print("=== МОЙ ПЕРВЫЙ AI АГЕНТ ===\n")

class SimpleAgent:
    def __init__(self):
        self.tools ={
            "calculator": self.calculator,
            "search": self.search,
            "weather": self.weather,
        }

    def calculator(self, expression):
        try:
            result = eval(expression)
            return f"Результат: {result}"
        except:
            return  "Ошибка вычисления"
    
    def search(self, query):
        responses = {
            "python": "Python — язык программирования",
            "ai": "AI — искусственный интеллект",
            "langchain": "LangChain — фреймворк для AI агентов"    
        }
        return responses.get(query.lower(), f"Информация про '{query}' не найдена")
    
    def weather(self, city):
        return  f"Погода в {city}: +5°C, облачно"
    
    def think(self, user_request):
        request = user_request.lower()

        if any(word in request for word in ["посчитай", "вычисли", "сколько"]):
            return "calculator"
        elif any (word in request for word in ["найди", "что такое", "расскажи"]):
            return "search"
        elif  "погода" in request:
            return "weather"
        else:
            return None 
    
    def extract(self, user_request, tool_name):
        if tool_name == "calculator":
            import re 
            match = re.search(r'[\d\+\-\*/\(\)\s]+', user_request)
            return match.group() if match else "2+2"
        elif tool_name == "search":
            words = user_request.lower().split()
            keywords = ["python", "ai", "langchain"]
            for word in words:
                if word in keywords:
                    return word 
            return "ai"
        
        elif tool_name == "weather":
            words = user_request.split()
            for word in words:
                if word.capitalize() in ["Минск", "Москва", "Киев"]:
                    return word.capitalize()
            return  "Минск"
            
    def run(self, user_request):
        print(f"Пользователь: {user_request}")
        print("Агент думает... 🤔\n")
        tool_name = self.think(user_request)
        if not tool_name:
            return "Не могу обработать этот запрос"
        print(f"📋 Решение: использую tool '{tool_name}'")
        params = self.extract(user_request, tool_name)
        print(f"📋 Параметры: {params}")
        tool = self.tools[tool_name]
        result = tool(params)
        print(f"✅ Результат: {result}\n")
        return result 

agent = SimpleAgent()
examples = [
    "Посчитай сколько будет 125 * 8",
    "Что такое Python?",
    "Какая погода в Минске?",
    "Найди информацию про LangChain"
]
print("=== ДЕМОНСТРАЦИЯ АГЕНТА ===\n")
for example in examples:
    agent.run(example)
    print("-" * 50 + "\n")

print("=== ПОПРОБУЙ САМ ===")

print("Примеры:")
print("- Посчитай 50 * 20")
print("- Что такое AI?")
print("- Погода в Минске\n")

while True:
    user_input = input("Твой запрос (или 'выход'): ")

    if user_input.lower() == "выход":
        break
    agent.run(user_input)

