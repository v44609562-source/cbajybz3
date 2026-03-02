import math
from datetime import datetime, timedelta

class SmartCalculatorAgent:
    def __init__(self):
        self.tools = {
             "math": self.math_calc,
            "percent": self.percent_calc,
            "time": self.time_calc,
            "currency": self.currency_calc,
            "goal": self.goal_calc
        }
    def math_calc(self, expression):
        try:
            safe_dict = {"sqrt": math.sqrt, "pow": math.pow, "pi": math.pi}
            result = eval(expression,{"__builtins__":{}}, safe_dict)
            return result
        except Exception as e:
            return f"Ошибка: {e}"
            
    def percent_calc(self, params):
        import re 
        found_number = re.findall(r'\d+', params)
        if len(found_number) >= 2:
            percent = float(found_number[0])
            value = float(found_number[1])   
            result = value * (percent/100)
            return f"{percent}%  от {value} = {result}"
        return "Не понял запрос"
    
    def time_calc(self, params):
        import re 
        match = re.search(r'(\d+)\s*(день|дня|дней)', params)
        if match:
            days = int(match.group(1))
            if "через" in params:
                target = datetime.now() +timedelta(days=days)
                return f"Через {days} дней: {target.strftime('%d.%m.%Y')}"
            else:
                target = datetime.now() - timedelta(days=days)
                return f"{days} дней назад: {target.strftime('%d.%m.%Y')}"
    def currency_calc(self, params):
        rates = {"USD": 3.27, "EUR": 3.55, "RUB": 0.036}
        import re 
        match = re.search(r'(\d+)\s*(\w+)', params)
        if match:
            amount = float(match.group(1))
            currency = match.group(2).upper()
            if currency in rates:
                result = amount * rates[currency]
                return f"{amount} {currency} = {result:.2f} BYN"
            return "Не понял запрос"
    
    def goal_calc(self, params):
        import re
        match = re.search(r'(\d+).*?(\d+)', params)
        if match:
            goal = float(match.group(1))
            monthly = float(match.group(2))
            months = goal/monthly 
            years = months/12
            return f"Цель ${goal} при ${monthly}/мес:\n  {months:.1f} месяцев ({years:.1f} лет)"
        return "Не понял запрос"
    
    def think(self, request):
        req = request.lower()
        if any(w in req for w in ["процент", "%", "скидка"]):
            return "percent"
        elif any(w in req for w in ["через", "дней", "когда", "дата"]):
            return"time"
        elif any(w in req for w in ["usd", "eur", "rub", "доллар", "евро"]):
            return "currency"
        elif any(w in req for w in ["цель", "достичь", "заработать"]):
            return "goal"
        else: 
            return"math"
        
    def run(self, request):
        print(f"\n💬 Ты: {request}")
        print("🤔 Думаю...")
        tool_name = self.think(request)
        print(f"📋 Использую: {tool_name}")
        tool = self.tools[tool_name]
        result = tool(request)
        print (f"✅ Результат: {result}")
        return result 
    
agent = SmartCalculatorAgent()
print("=== УМНЫЙ КАЛЬКУЛЯТОР-АГЕНТ ===\n")
examples = [
     "Посчитай sqrt(144) + 10",
    "Сколько будет 20% от 1000?",
    "Какая дата через 90 дней?",
    "Конвертируй 100 USD в BYN",
    "Сколько времени достичь 10000 при 500 в месяц?"
]

for example in examples:
    agent.run(example)
    print()

print("\n=== ПОПРОБУЙ САМ ===")
while True:
    user = input("\nЗапрос ('выход' для выхода): ")
    if user.lower() == "exit":
        break
    agent.run(user)





