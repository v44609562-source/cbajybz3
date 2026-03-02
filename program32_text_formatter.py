# Инструмент для форматирования текста

print("=== TEXT FORMATTER ===\n")

def to_title_case(text):
    """Каждое слово с большой буквы"""
    return text.title()

def to_snake_case(text):
    """snake_case"""
    return text.lower().replace(" ", "_")

def to_camel_case(text):
    """camelCase"""
    words = text.split()
    return words[0].lower() + "".join(w.capitalize() for w in words[1:])

def count_words(text):
    """Подсчёт слов"""
    return len(text.split())

def remove_extra_spaces(text):
    """Убрать лишние пробелы"""
    return " ".join(text.split())

def censor_words(text, bad_words):
    """Заменить плохие слова на ***"""
    for word in bad_words:
        text = text.replace(word, "***")
    return text

# Меню
while True:
    print("\n--- TEXT FORMATTER ---")
    print("1. Title Case")
    print("2. snake_case")
    print("3. camelCase")
    print("4. Подсчитать слова")
    print("5. Убрать лишние пробелы")
    print("6. Цензура слов")
    print("7. Выход")
    
    choice = input("\nВыбери (1-7): ")
    
    if choice == "7":
        break
    
    text = input("\nВведи текст: ")
    
    if choice == "1":
        print(f"Результат: {to_title_case(text)}")
    elif choice == "2":
        print(f"Результат: {to_snake_case(text)}")
    elif choice == "3":
        print(f"Результат: {to_camel_case(text)}")
    elif choice == "4":
        print(f"Слов: {count_words(text)}")
    elif choice == "5":
        print(f"Результат: {remove_extra_spaces(text)}")
    elif choice == "6":
        bad = input("Плохие слова (через запятую): ").split(",")
        print(f"Результат: {censor_words(text, [w.strip() for w in bad])}")
```

---

## БЛОК 2 (3 часа): ПОДГОТОВКА К ДЕНЬГАМ

### Часть 1: Fiverr Research (1 час)

**Что делать:**

1. **Зайди на Fiverr.com**
2. **Поищи:**
   - "telegram bot"
   - "python automation"
   - "web scraping"

3. **Изучи 10-15 gig'ов:**
   - Что они предлагают?
   - Какие цены? ($5-500)
   - Как описывают услугу?
   - Какие примеры показывают?

4. **Запиши в Google Doc:**
```
📊 FIVERR RESEARCH

Средние цены:
- Простой Telegram бот: $20-50
- Бот с API: $50-150
- Автоматизация: $100-300
- Веб-скрейпинг: $50-200

Что я УЖЕ умею делать:
✅ Telegram боты
✅ API интеграции
✅ Веб-скрейпинг
✅ JSON обработка

Что могу продавать:
1. Telegram бот с любыми командами ($30-80)
2. Парсер данных с сайта ($50-150)
3. Автоматизация рутинных задач ($80-200)

Первый gig (черновик):
"I will create a custom Telegram bot with API integration"
Цена: $30
Срок: 3 дня