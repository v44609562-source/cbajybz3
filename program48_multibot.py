from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
import json
from datetime import datetime
import math
import re


TOKEN = "8195553126:AAH_abv0qKPzvcyx3iDSFeOI6rkPGxCpXO8"


NOTES_FILE = "bot_notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_notes(notes):
    with open(NOTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 MULTI-FUNCTION BOT\n\n"
        "Что умею:\n\n"
        "📝 /note текст - сохранить заметку\n"
        "/notes - показать все заметки\n"
        "/clear - очистить заметки\n\n"
        "🔢 /calc выражение - калькулятор\n"
        "Примеры: /calc 50*20 или /calc sqrt(144)\n\n"
        "📊 /stats текст - анализ текста\n\n"
        "📄 Отправь файл - покажу тип и размер"
    )

async def note_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Сохранить заметку"""
    user_id = str(update.effective_user.id)
    if not context.args:
        await update.message.reply_text("Формат: /note текст заметки")
        return
    
    note_text = ' '.join(context.args)
    
    notes = load_notes()
    if user_id not in notes:
        notes[user_id] = []
    
    notes[user_id].append({
        "text": note_text,
        "date": datetime.now().strftime("%d.%m.%Y %H:%M")
    })
    
    save_notes(notes)
    
    await update.message.reply_text(
        f"✅ Заметка #{len(notes[user_id])} сохранена!"
    )

async def notes_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать все заметки"""
    user_id = str(update.effective_user.id)
    notes = load_notes()
    
    if user_id not in notes or not notes[user_id]:
        await update.message.reply_text("❌ Заметок нет")
        return
    
    text = "📝 ТВОИ ЗАМЕТКИ:\n\n"
    for i, note in enumerate(notes[user_id], 1):
        text += f"{i}. {note['text']}\n"
        text += f"   📅 {note['date']}\n\n"
    
    await update.message.reply_text(text)

async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Очистить заметки"""
    user_id = str(update.effective_user.id)
    notes = load_notes()
    
    if user_id in notes:
        count = len(notes[user_id])
        notes[user_id] = []
        save_notes(notes)
        await update.message.reply_text(f"🗑️ Удалено {count} заметок")
    else:
        await update.message.reply_text("❌ Заметок и так нет")

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Калькулятор"""
    if not context.args:
        await update.message.reply_text(
            "Формат: /calc выражение\n"
            "Примеры:\n"
            "  /calc 50 * 20\n"
            "  /calc sqrt(144)\n"
            "  /calc pow(2, 10)"
        )
        return
    
    expression = ' '.join(context.args)
    
    try:
        safe_dict = {
            "sqrt": math.sqrt,
            "pow": math.pow,
            "pi": math.pi,
            "sin": math.sin,
            "cos": math.cos
        }
        result = eval(expression, {"__builtins__": {}}, safe_dict)
        await update.message.reply_text(f"✅ Результат: {result}")
    except Exception as e:
        await update.message.reply_text(f"❌ Ошибка: {e}")

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Анализ текста"""
    if not context.args:
        await update.message.reply_text("Формат: /stats текст для анализа")
        return
    
    text = ' '.join(context.args)
    
    words = text.split()
    chars = len(text)
    sentences = text.count('.') + text.count('!') + text.count('?')
    
    if words:
        longest = max(words, key=len)
        avg_length = sum(len(w) for w in words) / len(words)
    else:
        longest = ""
        avg_length = 0
    
    report = f"📊 АНАЛИЗ ТЕКСТА\n\n"
    report += f"Слов: {len(words)}\n"
    report += f"Символов: {chars}\n"
    report += f"Предложений: {sentences}\n"
    report += f"Самое длинное слово: {longest} ({len(longest)} букв)\n"
    report += f"Средняя длина слова: {avg_length:.1f}"
    
    await update.message.reply_text(report)
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc = update.message.document
    
    filename = doc.file_name
    size = doc.file_size
    mime_type = doc.mime_type
    
    # Определяем категорию
    ext = os.path.splitext(filename)[1].lower()
    
    categories = {
        "Изображение": [".jpg", ".png", ".gif"],
        "Документ": [".pdf", ".docx", ".txt"],
        "Видео": [".mp4", ".avi", ".mkv"],
        "Аудио": [".mp3", ".wav"],
        "Архив": [".zip", ".rar"],
        "Код": [".py", ".js", ".html"]
    }
    
    category = "Файл"
    for cat, exts in categories.items():
        if ext in exts:
            category = cat
            break
    
    size_mb = size / (1024 * 1024)
    
    info = f"📄 ИНФОРМАЦИЯ О ФАЙЛЕ\n\n"
    info += f"Название: {filename}\n"
    info += f"Тип: {category}\n"
    info += f"Размер: {size_mb:.2f} МБ\n"
    info += f"MIME: {mime_type}"
    
    await update.message.reply_text(info)

# === MAIN ===

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("note", note_command))
    app.add_handler(CommandHandler("notes", notes_command))
    app.add_handler(CommandHandler("clear", clear_command))
    app.add_handler(CommandHandler("calc", calc_command))
    app.add_handler(CommandHandler("stats", stats_command))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    
    print("✅ Multi-Function Bot запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()

