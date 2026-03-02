# Программа 10: Telegram бот-помощник

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import json
import os
from datetime import datetime


# ВСТАВЬ СЮДА СВОЙ ТОКЕН (который дал BotFather)
TOKEN = "7953909173:AAHbW_GxoL7EYAnTYvfPvoajVVF2jPaUI4E"
DATA_FILE = "study_data.json"

def load_data():
    """Загрузить данные из JSON"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_data(data):
    """Сохранить данные в JSON"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_user(data, user_id):
    """Получить или создать пользователя"""
    if user_id not in data:
        data[user_id] = {
            "subjects": {},
            "history": [],
            "streak": 0,
            "last_check": None
        }
    return data[user_id]

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(
            f"👋 Привет, {user_name}!\n\n"
        "Я твой AI помощник. Вот что я умею:\n"
        "/start - приветсвие\n"
        "/help - Помощь\n"
        "/add_subject — Добавить предмет\n"
        "/set_goal — Установить цель (часов/неделю)\n"
        "/log — Отметить занятие\n"
        "/stats — Статистика\n"
        "/week — Прогресс за неделю\n"
        "/best — Самый изучаемый предмет\n\n"
        "Или просто напиши мне что-нибудь!"
    )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 ПОМОЩЬ\n\n"
        "Доступные команды:\n"
        "/start - приветсвие\n"
        "/help - Помощь\n"
        "/add_subject — Добавить предмет\n"
        "/set_goal — Установить цель (часов/неделю)\n"
        "/log — Отметить занятие\n"
        "/stats — Статистика\n"
        "/week — Прогресс за неделю\n"
        "/best — Самый изучаемый предмет\n"
        "/streak\n"
    )

# Команда /add
async def add_subject(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Получаем user_id
    user_id = str(update.effective_user.id)
    
    # Проверяем аргументы: /add Python 10
    if len(context.args) < 2:
        await update.message.reply_text(
            "❌ Формат: /add Предмет Цель\n"
            "Пример: /add Python 10"
        )
        return
    
    subject = context.args[0]
    goal = int(context.args[1])
    
    # Загружаем данные
    data = load_data()
    user = get_user(data, user_id)
    
    # Добавляем предмет
    user["subjects"][subject] = {
        "goal": goal,
        "hours_this_week": 0
    }
    
    save_data(data)
    
    await update.message.reply_text(
        f"✅ {subject} добавлен!\n"
        f"Цель: {goal} ч/неделю"
    )

async def streak_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    data = load_data()
    user = get_user(data, user_id)
    
    if not user["history"]:
        await update.message.reply_text("❌ Нет записей. Начни: /log Python 2")
        return
    
    # Считаем streak
    from datetime import datetime, timedelta
    
    dates = sorted(set(entry["date"] for entry in user["history"]), reverse=True)
    
    if not dates:
        await update.message.reply_text("❌ Нет записей")
        return
    
    streak = 0
    today = datetime.now().date()
    
    for i, date_str in enumerate(dates):
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        expected = today - timedelta(days=i)
        
        if date == expected:
            streak += 1
        else:
            break
    
    await update.message.reply_text(
        f"🔥 STREAK: {streak} дней подряд!\n\n"
        f"Продолжай учиться каждый день! 💪"
    )

# Команда /progress
async def log_session(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    # Проверяем: /log Python 2
    if len(context.args) < 2:
        await update.message.reply_text(
            "❌ Формат: /log Предмет Часы\n"
            "Пример: /log Python 2"
        )
        return
    
    subject = context.args[0]
    hours = float(context.args[1])
    
    data = load_data()
    user = get_user(data, user_id)
    
    # Проверяем есть ли предмет
    if subject not in user["subjects"]:
        await update.message.reply_text(
            f"❌ Предмет {subject} не найден.\n"
            f"Сначала добавь: /add {subject} 10"
        )
        return
    
    # Записываем часы
    user["subjects"][subject]["hours_this_week"] += hours
    
    # Добавляем в историю
    today = datetime.now().strftime("%Y-%m-%d")
    user["history"].append({
        "date": today,
        "subject": subject,
        "hours": hours
    })
    
    save_data(data)
    
    current = user["subjects"][subject]["hours_this_week"]
    goal = user["subjects"][subject]["goal"]
    percent = (current / goal) * 100
    
    await update.message.reply_text(
        f"🔥 Записано: {subject} — {hours}ч\n\n"
        f"На этой неделе: {current}/{goal}ч\n"
        f"Прогресс: {percent:.0f}%"
    )

# Команда /motivation
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    data = load_data()
    user = get_user(data, user_id)
    
    if not user["subjects"]:
        await update.message.reply_text(
            "❌ Предметов нет.\n"
            "Добавь: /add Python 10"
        )
        return
    
    # Формируем статистику
    text = "📊 СТАТИСТИКА\n\n"
    
    for subject, info in user["subjects"].items():
        current = info["hours_this_week"]
        goal = info["goal"]
        percent = (current / goal) * 100 if goal > 0 else 0
        
        # Прогресс-бар
        filled = int(percent / 5)
        bar = "█" * min(filled, 20) + "░" * max(20 - filled, 0)
        
        text += f"📚 {subject}\n"
        text += f"   Цель: {goal}ч/нед\n"
        text += f"   Сейчас: {current}ч\n"
        text += f"   [{bar}] {percent:.0f}%\n"
        
        if percent >= 100:
            text += "   🎉 Цель выполнена!\n"
        elif percent >= 70:
            text += "   💪 Почти там!\n"
        
        text += "\n"
    
    # Общая статистика
    total_hours = sum(s["hours_this_week"] for s in user["subjects"].values())
    text += f"⏱️ Всего на неделе: {total_hours}ч\n"
    
    await update.message.reply_text(text)



# Обработка обычных сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    
    # Простые ответы
    if "привет" in user_message or "здравствуй" in user_message:
        await update.message.reply_text("👋 Привет! Как дела с обучением?")
    
    elif "как дела" in user_message:
        await update.message.reply_text(
            "У меня всё отлично! Я бот, я всегда готов помочь 🤖\n"
            "А у тебя как? Сколько программ сегодня написал?"
        )
    
    elif "устал" in user_message or "тяжело" in user_message:
        await update.message.reply_text(
            "Понимаю, бывает тяжело. Но ты молодец что продолжаешь! 💪\n"
            "Сделай перерыв, погуляй, потом продолжишь.\n"
            "Главное — не бросай!"
        )
    
    elif "спасибо" in user_message:
        await update.message.reply_text("Пожалуйста! Всегда рад помочь! 😊")
    
    else:
        # Эхо — повторяет сообщение
        await update.message.reply_text(
            f"Ты написал: {update.message.text}\n\n"
            "Используй команды для большего функционала:\n"
            "/help - посмотреть все команды"
        )

async def week_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Прогресс за неделю"""
    user_id = str(update.effective_user.id)
    
    data = load_data()
    user = get_user(data, user_id)
    
    if not user["subjects"]:
        await update.message.reply_text("❌ Предметов нет. Добавь: /add Python 10")
        return
    
    # Фильтруем историю за эту неделю
    from datetime import datetime, timedelta
    today = datetime.now().date()
    week_start = today - timedelta(days=today.weekday())
    
    this_week = [h for h in user["history"] 
                 if datetime.strptime(h["date"], "%Y-%m-%d").date() >= week_start]
    
    # Считаем часы по предметам
    week_hours = {}
    for entry in this_week:
        subj = entry["subject"]
        week_hours[subj] = week_hours.get(subj, 0) + entry["hours"]
    
    # Формируем ответ
    text = "📅 ПРОГРЕСС ЗА НЕДЕЛЮ\n\n"
    
    for subject, info in user["subjects"].items():
        current = week_hours.get(subject, 0)
        goal = info["goal"]
        percent = (current / goal) * 100 if goal > 0 else 0
        
        text += f"📚 {subject}\n"
        text += f"   {current}/{goal}ч ({percent:.0f}%)\n"
        
        if percent >= 100:
            text += "   ✅ Цель выполнена!\n"
        
        text += "\n"
    
    total = sum(week_hours.values())
    text += f"⏱️ Всего за неделю: {total}ч"
    
    await update.message.reply_text(text)

async def best_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Самый изучаемый предмет"""
    user_id = str(update.effective_user.id)
    
    data = load_data()
    user = get_user(data, user_id)
    
    if not user["history"]:
        await update.message.reply_text("❌ Нет записей. Начни: /log Python 2")
        return
    
    # Считаем общие часы по предметам
    total_hours = {}
    for entry in user["history"]:
        subj = entry["subject"]
        total_hours[subj] = total_hours.get(subj, 0) + entry["hours"]
    
    # Сортируем по часам
    sorted_subjects = sorted(total_hours.items(), key=lambda x: x[1], reverse=True)
    
    text = "🏆 ТОП ПРЕДМЕТОВ\n\n"
    
    for i, (subject, hours) in enumerate(sorted_subjects[:5], 1):
        emoji = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"][i-1]
        text += f"{emoji} {subject}: {hours}ч\n"
    
    # Лучший предмет
    best_subject, best_hours = sorted_subjects[0]
    text += f"\n🔥 Лидер: {best_subject} ({best_hours}ч)"
    
    await update.message.reply_text(text)

async def add_subject_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """То же что /add но с другим названием"""
    await add_subject(update, context)

async def set_goal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Изменить цель для предмета"""
    user_id = str(update.effective_user.id)
    
    # /set_goal Python 15
    if len(context.args) < 2:
        await update.message.reply_text(
            "❌ Формат: /set_goal Предмет Новая_цель\n"
            "Пример: /set_goal Python 15"
        )
        return
    
    subject = context.args[0]
    new_goal = int(context.args[1])
    
    data = load_data()
    user = get_user(data, user_id)
    
    if subject not in user["subjects"]:
        await update.message.reply_text(f"❌ Предмет {subject} не найден")
        return
    
    old_goal = user["subjects"][subject]["goal"]
    user["subjects"][subject]["goal"] = new_goal
    
    save_data(data)
    
    await update.message.reply_text(
        f"✅ Цель обновлена!\n"
        f"{subject}: {old_goal}ч → {new_goal}ч/нед"
    )

# Основная функция
def main():
    print("🤖 Бот запускается...")
    
    # Создаём приложение
    application = Application.builder().token(TOKEN).build()
    
    # Регистрируем команды
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_subject))
    application.add_handler(CommandHandler("log", log_session))
    application.add_handler(CommandHandler("stats", stats))
    application.add_handler(CommandHandler("week", week_command))
    application.add_handler(CommandHandler("best", best_command))
    application.add_handler(CommandHandler("add_subject", add_subject_command))
    application.add_handler(CommandHandler("set_goal", set_goal_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("streak", streak_command))

    # Регистрируем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запускаем бота
    print("✅ Бот запущен! Открой Telegram и напиши своему боту.")
    print("Для остановки нажми Ctrl+C")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

# Запуск
if __name__ == "__main__":
    main()