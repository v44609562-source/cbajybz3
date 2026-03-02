from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import json
import os
from datetime import datetime
import requests
import random

TOKEN = "7953909173:AAHbW_GxoL7EYAnTYvfPvoajVVF2jPaUI4E"
TASKS_FILE = "dashboard_tasks.json"

# === ЗАГРУЗКА/СОХРАНЕНИЕ ===

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_tasks(data):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_user_tasks(data, user_id):
    if user_id not in data:
        data[user_id] = []
    return data[user_id]

# === API ФУНКЦИИ ===

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
        "🔥 Продолжай каждый день!",
        "💪 Ты на правильном пути",
        "⚡ Маленькие шаги = большой результат",
        "🚀 Не останавливайся",
        "🎯 Фокус на цели"
    ]
    return random.choice(quotes)

# === КОМАНДЫ БОТА ===

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Dashboard Bot\n\n"
        "Команды:\n"
        "/briefing - Утренняя сводка\n"
        "/add Название YYYY-MM-DD приоритет - Добавить задачу\n"
        "/tasks - Все задачи\n"
        "/today - На сегодня\n"
        "/overdue - Просроченные\n"
        "/done ID - Отметить выполненной\n"
        "/stats - Статистика\n"
        "/weather - Погода\n"
        "/currency - Курсы"
    )

async def briefing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    text = "☀️ УТРЕННЯЯ СВОДКА\n\n"
    
    # Дата
    now = datetime.now()
    text += f"📅 {now.strftime('%d.%m.%Y %H:%M')}\n\n"
    
    # Погода
    text += f"🌤️ {get_weather()}\n\n"
    
    # Валюты
    text += f"💰 {get_currency()}\n\n"
    
    # Задачи на сегодня
    data = load_tasks()
    user_tasks = get_user_tasks(data, user_id)
    
    today = datetime.now().strftime("%Y-%m-%d")
    today_tasks = [t for t in user_tasks if t.get("deadline") == today and not t.get("done", False)]
    
    if today_tasks:
        text += "🎯 НА СЕГОДНЯ:\n"
        for task in today_tasks:
            text += f"• {task['name']}\n"
    else:
        text += "✅ Задач на сегодня нет\n"
    
    text += f"\n{get_motivation()}"
    
    await update.message.reply_text(text)

async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    # /add Доделать_бота 2026-02-20 высокий
    if len(context.args) < 3:
        await update.message.reply_text(
            "❌ Формат:\n"
            "/add Название YYYY-MM-DD приоритет\n\n"
            "Пример:\n"
            "/add Доделать_бота 2026-02-20 высокий"
        )
        return
    
    name = context.args[0].replace("_", " ")
    deadline = context.args[1]
    priority = context.args[2]
    
    data = load_tasks()
    user_tasks = get_user_tasks(data, user_id)
    
    task = {
        "id": random.randint(1000, 9999),
        "name": name,
        "deadline": deadline,
        "priority": priority,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    user_tasks.append(task)
    data[user_id] = user_tasks
    save_tasks(data)
    
    await update.message.reply_text(
        f"✅ Задача добавлена!\n\n"
        f"ID: {task['id']}\n"
        f"{task['name']}\n"
        f"Дедлайн: {deadline}\n"
        f"Приоритет: {priority}"
    )

async def show_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    data = load_tasks()
    user_tasks = get_user_tasks(data, user_id)
    
    if not user_tasks:
        await update.message.reply_text("❌ Задач нет. Добавь: /add")
        return
    
    # Сортировка
    priority_order = {"высокий": 1, "средний": 2, "низкий": 3}
    active = [t for t in user_tasks if not t.get("done", False)]
    active.sort(key=lambda t: priority_order.get(t.get("priority", "низкий"), 4))
    
    text = "📋 МОИ ЗАДАЧИ\n\n"
    
    for task in active:
        emoji = {"высокий": "🔥", "средний": "⚡", "низкий": "💤"}
        text += f"{emoji.get(task.get('priority'), '•')} {task['name']}\n"
        text += f"   ID: {task['id']} | {task.get('deadline', 'нет дедлайна')}\n\n"
    
    done = [t for t in user_tasks if t.get("done", False)]
    if done:
        text += f"\n✅ Выполнено: {len(done)}"
    
    await update.message.reply_text(text)

async def today_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    data = load_tasks()
    user_tasks = get_user_tasks(data, user_id)
    
    today = datetime.now().strftime("%Y-%m-%d")
    today_tasks = [t for t in user_tasks if t.get("deadline") == today and not t.get("done", False)]
    
    if not today_tasks:
        await update.message.reply_text("✅ Задач на сегодня нет!")
        return
    
    text = "🎯 ЗАДАЧИ НА СЕГОДНЯ\n\n"
    for task in today_tasks:
        text += f"• {task['name']}\n"
        text += f"  ID: {task['id']} | {task.get('priority', 'средний')}\n\n"
    
    await update.message.reply_text(text)

async def overdue_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    data = load_tasks()
    user_tasks = get_user_tasks(data, user_id)
    
    today = datetime.now().strftime("%Y-%m-%d")
    overdue = [t for t in user_tasks if t.get("deadline", "9999-12-31") < today and not t.get("done", False)]
    
    if not overdue:
        await update.message.reply_text("✅ Просроченных задач нет!")
        return
    
    text = "⚠️ ПРОСРОЧЕННЫЕ ЗАДАЧИ\n\n"
    for task in overdue:
        text += f"• {task['name']}\n"
        text += f"  ID: {task['id']} | было {task.get('deadline')}\n\n"
    
    await update.message.reply_text(text)

async def mark_done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    # /done 1234
    if not context.args:
        await update.message.reply_text("❌ Формат: /done ID_задачи")
        return
    
    task_id = int(context.args[0])
    
    data = load_tasks()
    user_tasks = get_user_tasks(data, user_id)
    
    for task in user_tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(data)
            await update.message.reply_text(f"✅ Выполнено: {task['name']}")
            return
    
    await update.message.reply_text("❌ Задача не найдена")

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    data = load_tasks()
    user_tasks = get_user_tasks(data, user_id)
    
    total = len(user_tasks)
    done = len([t for t in user_tasks if t.get("done", False)])
    active = total - done
    
    percent = (done / total * 100) if total > 0 else 0
    
    text = "📊 СТАТИСТИКА\n\n"
    text += f"Всего задач: {total}\n"
    text += f"✅ Выполнено: {done} ({percent:.0f}%)\n"
    text += f"⏳ Активных: {active}\n"
    
    await update.message.reply_text(text)

async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    weather = get_weather()
    await update.message.reply_text(f"🌤️ {weather}")

async def currency_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    currency = get_currency()
    await update.message.reply_text(f"💰 {currency}")

# === MAIN ===

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("briefing", briefing))
    app.add_handler(CommandHandler("add", add_task))
    app.add_handler(CommandHandler("tasks", show_tasks))
    app.add_handler(CommandHandler("today", today_tasks))
    app.add_handler(CommandHandler("overdue", overdue_tasks))
    app.add_handler(CommandHandler("done", mark_done))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("weather", weather_command))
    app.add_handler(CommandHandler("currency", currency_command))
    
    print("✅ Dashboard Bot запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
