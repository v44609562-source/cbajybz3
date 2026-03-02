# Программа 10: Telegram бот-помощник

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ВСТАВЬ СЮДА СВОЙ ТОКЕН (который дал BotFather)
TOKEN = "8564255727:AAEB--6_mQCf9vFfRojNQ1JZS2d0_46IOV8"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"👋 Привет, {user_name}!\n\n"
        "Я твой AI помощник. Вот что я умею:\n"
        "/start - Начать\n"
        "/help - Помощь\n"
        "/goal - Твоя цель\n"
        "/progress - Прогресс\n"
        "/motivation - Мотивация\n\n"
        "Или просто напиши мне что-нибудь!"
    )

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 ПОМОЩЬ\n\n"
        "Доступные команды:\n"
        "/start - Начать общение\n"
        "/help - Эта помощь\n"
        "/goal - Узнать твою цель\n"
        "/progress - Посмотреть прогресс\n"
        "/motivation - Получить мотивацию\n"
    )

# Команда /goal
async def goal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎯 ТВОЯ ЦЕЛЬ\n\n"
        "💰 $10,000/месяц за 2-4 года\n"
        "💎 Капитал $20M к 35 годам\n"
        "🔝 Топ-10% AI + Programming специалист\n\n"
        "💪 Продолжай работать каждый день!"
    )

# Команда /progress
async def progress_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 ПРОГРЕСС\n\n"
        "✅ День 1: Установка инструментов\n"
        "✅ День 2: 5 программ\n"
        "✅ День 3: 4 программы + Chapter 2\n"
        "✅ День 4: Telegram бот (это я!)\n\n"
        "📁 Всего программ: 10+\n"
        "⏱️ Часов обучения: ~12\n"
        "🔥 Дней подряд: 4\n\n"
        "Отличная работа! Продолжай!"
    )

# Команда /motivation
async def motivation_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import random
    
    motivations = [
        "🔥 Ты не бросаешь. Это уже делает тебя лучше 90% людей.",
        "💪 Каждый день кода приближает тебя к $10k/мес.",
        "⚡ Тяжело? Хорошо. Легко было бы — все бы так делали.",
        "🚀 Через 3 месяца ты будешь благодарить себя сегодняшнего.",
        "🎯 Маленькие шаги каждый день = большой результат через год.",
        "💎 Ты строишь будущее. Не останавливайся.",
        "🔝 Топ-10% — это не талант. Это постоянство.",
        "⭐ Ты уже сделал больше чем большинство мечтателей."
    ]
    
    motivation = random.choice(motivations)
    await update.message.reply_text(motivation)
###
async def premium_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💎 PREMIUM ФУНКЦИИ\n\n"
        "Доступно только для премиум пользователей:\n"
        "• Персональный AI ассистент\n"
        "• Расширенная аналитика прогресса\n"
        "• Напоминания о задачах\n"
        "• Приоритетная поддержка\n\n"
        "Стоимость: 100 Stars ⭐\n"
        "/buy_premium - Купить доступ"
    )

async def donate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❤️ ПОДДЕРЖАТЬ РАЗРАБОТЧИКА\n\n"
        "Если бот помогает тебе — можешь поддержать:\n"
        "• 10 Stars ⭐ - Спасибо!\n"
        "• 50 Stars ⭐ - Круто!\n"
        "• 100 Stars ⭐ - Ты лучший!\n\n"
        "Это мотивирует делать бота лучше! 🚀\n"
        "/send_stars - Отправить Stars"
    )

async def roadmap_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🗺️ ПУТЬ К $1000/МЕС\n\n"
        "📅 Неделя 1-2: Основы Python ✅\n"
        "   → 20 программ на GitHub\n\n"
        "📅 Неделя 3-4: Первые деньги 💰\n"
        "   → Fiverr gig: Telegram боты\n"
        "   → Первые $50-200\n\n"
        "📅 Неделя 5-8: Специализация ⚡\n"
        "   → Выбор ниши\n"
        "   → $200-500/мес\n\n"
        "📅 Неделя 9-12: Масштабирование 🚀\n"
        "   → Выше цены\n"
        "   → Больше клиентов\n"
        "   → $1000/мес ДОСТИГНУТО!\n\n"
        "Ты сейчас: Неделя 1 ✅"
    )

async def analytics_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    days_learning = 7
    programs_written = 16
    hours_total = 26
    github_commits = 15
    
    progress = (days_learning / 90) * 100
    
    await update.message.reply_text(
        f"📊 ТВОЯ АНАЛИТИКА\n\n"
        f"🔥 Дней обучения: {days_learning}\n"
        f"💻 Программ написано: {programs_written}\n"
        f"⏱️ Часов практики: {hours_total}\n"
        f"📁 GitHub commits: {github_commits}\n\n"
        f"📈 Прогресс к $1000/мес: {progress:.1f}%\n"
        f"{'█' * int(progress/5)}{'░' * (20-int(progress/5))}\n\n"
        f"🎯 До цели: {90-days_learning} дней\n"
        f"💪 Продолжай! Ты на правильном пути!"
    )

async def challenge_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import random
    
    challenges = [
        "Напиши функцию которая решает квадратное уравнение",
        "Создай программу для конвертации валют",
        "Сделай калькулятор индекса массы тела (BMI)",
        "Напиши игру 'Камень-Ножницы-Бумага'",
        "Создай генератор случайных цитат",
        "Сделай таймер Pomodoro (25 мин работы)",
        "Напиши программу для подсчёта калорий",
        "Создай конвертер температуры (C/F/K)",
    ]
    
    challenge = random.choice(challenges)
    
    await update.message.reply_text(
        f"🎯 ЧЕЛЛЕНДЖ НА СЕГОДНЯ\n\n"
        f"{challenge}\n\n"
        f"Время: 30-60 минут\n"
        f"Сложность: Средняя\n\n"
        f"Когда сделаешь — загрузи на GitHub! 🚀"
    )        
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

# Основная функция
def main():
    print("🤖 Бот запускается...")
    
    # Создаём приложение
    application = Application.builder().token(TOKEN).build()
    
    # Регистрируем команды
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("goal", goal_command))
    application.add_handler(CommandHandler("progress", progress_command))
    application.add_handler(CommandHandler("motivation", motivation_command))
    application.add_handler(CommandHandler("premium", premium_command))
    application.add_handler(CommandHandler("donate", donate_command))
    application.add_handler(CommandHandler("roadmap", roadmap_command))
    application.add_handler(CommandHandler("analytics", analytics_command))
    application.add_handler(CommandHandler("challenge", challenge_command))

    # Регистрируем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запускаем бота
    print("✅ Бот запущен! Открой Telegram и напиши своему боту.")
    print("Для остановки нажми Ctrl+C")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

# Запуск
if __name__ == "__main__":
    main()