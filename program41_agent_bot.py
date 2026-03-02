from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import math 
import requests
import random

TOKEN = "7953909173:AAHbW_GxoL7EYAnTYvfPvoajVVF2jPaUI4E"

def tool_quote():
     """Случайная цитата"""
     quotes = [
        "🔥 Продолжай каждый день!",
        "💪 Ты на правильном пути",
        "⚡ Маленькие шаги = большой результат",
        "🚀 Не останавливайся",
        "🎯 Фокус на цели"
     ]
     return random.choice(quotes)

def tool_calculator(expression):
    try:
        safe_dict = {"sqrt": math.sqrt, "pow": math.pow, "pi":  math.pi}
        result  = eval(expression, {"__builtins__": {}}, safe_dict)
        return f"Результат: {result}"
    except Exception as e:
        return  f"Ошибка: {e}"
    
def tool_weather(city = "Pinsk"):
    try:
        url = f"http://wttr.in/{city}?format=j1"
        response =requests.get(url, timeout=5)
        data = response.json()
        temp =  data["current_condition"][0]["temp_C"]
        desk =  data["current_condition"][0]["weatherDesc"][0]["value"]
        return f"{city}: {temp} °C, {desk}"
    except: 
        return "Не удалось получить погоду"
    
def tool_currency():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url, timeout=5)
        data = response.json()
        byn = data ["rates"]["BYN"]
        eur = data["rates"]["EUR"]
        return f"1 USD = {byn:.2f} BYN\n1 EUR = {1/eur:.2f} USD"
    except:
        return "Не удалось получить курсы"

   



def agent_think(user_text):
    """Агент решает какой tool использовать"""
    text = user_text.lower()
    if any(word in text for word in ["посчитай", "вычисли", "сколько", "+", "-", "*", "/"]):
        return  "calculator"
    elif any(word in text for word in ["погода", "температура", "градус"]):
        return "weather"
    elif any(word in text for word in ["курс", "доллар", "валюта", "usd", "eur"]):
        return "currency"
    elif any(word in text for word in ["мотивация", "цитата", "вдохнов"]):
        return "quote"
    else:
        return None
    

    






async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 AGENT BOT\n\n"
        "Я умный агент! Просто напиши что нужно:\n\n"
        "💡 Примеры:\n"
        "• Посчитай 50 * 20\n"
        "• Погода в pinsk\n"
        "• Курсы валют\n"
        "• Дай мотивацию\n\n"
        "Я САМ пойму что делать! 🧠"
    )






async def handle_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    thinking_msg = await update.message.reply_text("thinking...")
    tool_name = agent_think(user_text)
    if not tool_name:
        await thinking_msg.edit_text(
            "🤔 Не понял запрос. Попробуй:\n"
            "• Математику (посчитай 5*5)\n"
            "• Погоду (погода в Минске)\n"
            "• Валюты (курс доллара)\n"
            "• Мотивацию"
        )
        return
    await thinking_msg.edit_text(f"🤔 Думаю...\n📋 Использую: {tool_name}")
    
    if tool_name == "calculator":
        import re 
        match = re.search(r'[\d\+\-\*/\(\)\s]+', user_text)
        if match:
            expression = match.group()
            result = tool_calculator(expression)
        else:
            result = "Не нашёл математическое выражение"
    
    elif  tool_name == "weather":
        words= user_text.split()
        city = "Pinsk"
        for word in words:
            if word.capitalize() in ["Минск", "Москва", "Киев", "Лондон", "Париж", "Pinsk"]:
                city = word.capitalize()
                break 
        result = tool_weather(city)




    elif tool_name == "currency":
        result = tool_currency()
    elif tool_name == "quote":
        result = tool_quote()
    
    await update.message.reply_text(f"🤖 {result}")


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()