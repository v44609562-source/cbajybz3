from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests
from datetime import datetime
import random

TOKEN = "8195553126:AAH_abv0qKPzvcyx3iDSFeOI6rkPGxCpXO8"

# Функции API (скопируй из program27)
def get_weather(city="Pinsk"):
    try:
        url = f"http://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=5)
        data = response.json()
        current = data["current_condition"][0]
        return f"{current['temp_C']}°C, {current['weatherDesc'][0]['value']}"
    except:
        return "Не удалось загрузить"

def get_currency():
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url, timeout=5)
        data = response.json()
        byn = data["rates"]["BYN"]
        eur = data["rates"]["EUR"]
        return f"1 USD = {byn:.2f} BYN\n1 EUR = {1/eur:.2f} USD"
    except:
        return "Не удалось загрузить"

def get_motivation():
    quotes = [
        "🔥 Ты не бросаешь. Продолжай.",
        "💪 Каждый день = прогресс.",
        "⚡ Тяжело? Значит растёшь.",
        "🚀 Ты на правильном пути.",
        "🎯 Шаг за шагом к цели.",
    ]
    return random.choice(quotes)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "☀️ Daily Dashboard Bot\n\n"
        "/dashboard - Утренняя сводка\n"
        "/weather - Погода\n"
        "/currency - Валюты\n"
        "/motivation - Мотивация"
    )

async def dashboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "☀️ ТВОЯ СВОДКА\n\n"
    
    now = datetime.now()
    text += f"📅 {now.strftime('%d.%m.%Y %H:%M')}\n\n"
    
    text += f"🌤️ Погода: {get_weather('Minsk')}\n\n"
    text += f"💰 Курсы:\n{get_currency()}\n\n"
    text += f"{get_motivation()}\n\n"
    text += "🎯 Цели на сегодня:\n"
    text += "• 3-4 часа кода\n"
    text += "• 1 новая программа\n"
    text += "• Обновить GitHub"
    
    await update.message.reply_text(text)

async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🌤️ {get_weather('Minsk')}")

async def currency_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💰 {get_currency()}")

async def motivation_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_motivation())

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("dashboard", dashboard))
    app.add_handler(CommandHandler("weather", weather_command))
    app.add_handler(CommandHandler("currency", currency_command))
    app.add_handler(CommandHandler("motivation", motivation_command))
    
    print("✅ Daily Bot запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()