import requests
from bs4 import BeautifulSoup
import json
import os

print("=== ПАРСЕР ЦИТАТ ===\n")

QUOTES_FILE = "quotes.json"

def scrape_quotes(pages=3):
    """Парсит цитаты с сайта"""
    all_quotes = []
    
    for page in range(1, pages + 1):
        print(f"📥 Загрузка страницы {page}...")
        
        url = f"http://quotes.toscrape.com/page/{page}/"
        
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Находим все цитаты
            quotes = soup.find_all('div', class_='quote')
            
            for quote in quotes:
                text = quote.find('span', class_='text').text
                author = quote.find('small', class_='author').text
                tags = [tag.text for tag in quote.find_all('a', class_='tag')]
                
                all_quotes.append({
                    "text": text,
                    "author": author,
                    "tags": tags
                })
            
            print(f"✅ Найдено {len(quotes)} цитат")
        
        except Exception as e:
            print(f"❌ Ошибка: {e}")
    
    return all_quotes

def save_quotes(quotes):
    """Сохранить в JSON"""
    with open(QUOTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(quotes, f, ensure_ascii=False, indent=2)
    print(f"\n💾 Сохранено {len(quotes)} цитат в {QUOTES_FILE}")

def load_quotes():
    """Загрузить из JSON"""
    if os.path.exists(QUOTES_FILE):
        with open(QUOTES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def search_quotes(quotes, keyword):
    """Поиск по ключевому слову"""
    results = []
    keyword = keyword.lower()
    
    for quote in quotes:
        if (keyword in quote["text"].lower() or 
            keyword in quote["author"].lower() or 
            keyword in " ".join(quote["tags"]).lower()):
            results.append(quote)
    
    return results

def filter_by_author(quotes, author):
    """Фильтр по автору"""
    return [q for q in quotes if author.lower() in q["author"].lower()]

def get_random_quote(quotes):
    """Случайная цитата"""
    import random
    return random.choice(quotes) if quotes else None

def show_quote(quote):
    """Красиво показать цитату"""
    print(f"\n{quote['text']}")
    print(f"— {quote['author']}")
    if quote['tags']:
        print(f"Теги: {', '.join(quote['tags'])}")

# Главное меню
while True:
    print("\n--- ПАРСЕР ЦИТАТ ---")
    print("1. Спарсить новые цитаты")
    print("2. Показать случайную цитату")
    print("3. Поиск по слову")
    print("4. Цитаты автора")
    print("5. Статистика")
    print("6. Выход")
    
    choice = input("\nВыбери (1-6): ")
    
    if choice == "1":
        pages = int(input("Сколько страниц спарсить (1-10)? "))
        quotes = scrape_quotes(min(pages, 10))
        save_quotes(quotes)
    
    elif choice == "2":
        quotes = load_quotes()
        if quotes:
            quote = get_random_quote(quotes)
            show_quote(quote)
        else:
            print("❌ Нет цитат. Сначала спарси: выбери 1")
    
    elif choice == "3":
        quotes = load_quotes()
        if not quotes:
            print("❌ Нет цитат")
            continue
        
        keyword = input("Ключевое слово: ")
        results = search_quotes(quotes, keyword)
        
        print(f"\n🔍 Найдено: {len(results)}")
        for i, q in enumerate(results[:5], 1):
            print(f"\n{i}. {q['text'][:80]}...")
            print(f"   — {q['author']}")
    
    elif choice == "4":
        quotes = load_quotes()
        if not quotes:
            print("❌ Нет цитат")
            continue
        
        author = input("Автор: ")
        results = filter_by_author(quotes, author)
        
        print(f"\n📚 Найдено цитат: {len(results)}")
        for q in results[:5]:
            show_quote(q)
    
    elif choice == "5":
        quotes = load_quotes()
        if not quotes:
            print("❌ Нет цитат")
            continue
        
        authors = {}
        all_tags = {}
        
        for q in quotes:
            authors[q['author']] = authors.get(q['author'], 0) + 1
            for tag in q['tags']:
                all_tags[tag] = all_tags.get(tag, 0) + 1
        
        print(f"\n📊 СТАТИСТИКА:")
        print(f"Всего цитат: {len(quotes)}")
        print(f"Авторов: {len(authors)}")
        
        top_authors = sorted(authors.items(), key=lambda x: x[1], reverse=True)[:5]
        print("\n🏆 ТОП-5 АВТОРОВ:")
        for author, count in top_authors:
            print(f"  {author}: {count} цитат")
        
        top_tags = sorted(all_tags.items(), key=lambda x: x[1], reverse=True)[:5]
        print("\n🏷️ ТОП-5 ТЕГОВ:")
        for tag, count in top_tags:
            print(f"  {tag}: {count} раз")
    
    elif choice == "6":
        print("\n👋 Пока!")
        break
    
    else:
        print("❌ Неверный выбор")