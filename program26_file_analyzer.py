# program26_file_analyzer.py

import os

print("=== АНАЛИЗАТОР ТЕКСТОВЫХ ФАЙЛОВ ===\n")

def analyze_file(filepath):
    """Анализирует файл"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    words = content.split()
    chars = len(content)
    
    # Самые частые слова
    word_count = {}
    for word in words:
        word = word.lower().strip('.,!?;:')
        word_count[word] = word_count.get(word, 0) + 1
    
    top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]
    
    return {
        "lines": len(lines),
        "words": len(words),
        "chars": chars,
        "top_words": top_words
    }

# Список .py файлов в текущей папке
files = [f for f in os.listdir('.') if f.endswith('.py')]

print("📁 Найдено .py файлов:", len(files))
print("\nВыбери файл для анализа:\n")

for i, file in enumerate(files, 1):
    print(f"{i}. {file}")

choice = int(input("\nНомер файла: ")) - 1

if 0 <= choice < len(files):
    filepath = files[choice]
    
    print(f"\n📊 АНАЛИЗ: {filepath}\n")
    
    result = analyze_file(filepath)
    
    print(f"Строк: {result['lines']}")
    print(f"Слов: {result['words']}")
    print(f"Символов: {result['chars']}")
    
    print("\n🔝 ТОП-10 СЛОВ:")
    for word, count in result['top_words']:
        print(f"  {word}: {count} раз")
else:
    print("❌ Неверный выбор")