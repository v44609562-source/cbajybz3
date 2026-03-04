import os
import shutil
from datetime import datetime

class FileOrganizer:
    def __init__(self, folder_path):
        self.categories = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
            "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".odt"],
            "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
            "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
            "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".json"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Other": []
        }
        self.stats = {cat: 0 for cat in self.categories}

    def get_category(self):
        for category in self.categories:
            category_path = os.path.join(self.folder_path, category)
            if not os.path.exists(category_path):
                os.makedirs(category_path)
                print(f"📁 Создана папка: {category}")
                 
    def organize(self, dry_run=False):
        """Организовать файлы
        dry_run = True - только показать что будет сделано, не перемещать
        dry_run=False - реально переместить файлы
        """
        print(f"\n🔍 Сканирую: {self.folder_path}\n")
        files = [f for f in os.listdir(self.folder_path)
                 if os.path.isfile(os.path.join(self.folder_path, f))]
        if not files:
            print("❌ Нет файлов для сортировки")
            return
        print(f"Найдено файлов: {len(files)}\n")
        if not dry_run:
            self.create_folders()
        for filename in files:
            if filename.startswith('.') or filename.endswith('.py'):
                continue
            category = self.get_category(filename)
            
            if dry_run:
                self.stats[category] += 1 
                print(f"📋 {filename} → {category}")
            else:
                source = os.path.join(self.folder_path, filename)
                destination_folder = os.path.join(self.folder_path, category)
                destination = os.path.join(destination_folder, filename)
            try:
                shutil.move(source, destination)
                self.stats[category] +=1
                print(f"✅ {filename} → {category}")
            except Exception as e:
                print(f"❌ Ошибка с {filename}: {e}")

        self.generate_report(dry_run)
        
    def generate_report(self, dry_run = False):
        """Генерация отчёта"""
        print("\n" + "="*50)
        if dry_run:
            print("📊 ПРЕДВАРИТЕЛЬНЫЙ ОТЧЁТ (файлы НЕ перемещены)")
        else:
            print("📊 ОТЧЁТ О СОРТИРОВКЕ")
        print("="*50 + "\n")
        for category, count in self.stats.items():
            if count > 0 :
                print(f"{category}: {count} файлов")
        total = sum(self.stats.values())
        print(f"\nВсего: {total} файлов")
        if not dry_run:
            report_file = os.path.join(
                self.folder_path,
                f"organize_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            )
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(f"Отчёт о сортировке файлов\n")
                f.write(f"Дата: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n")
                f.write(f"Папка: {self.folder_path}\n\n")
                for category, count in self.stats.items():
                    if count > 0:
                        f.write(f"\nВсего: {total}")
                    print(f"\n💾 Отчёт сохранён: {report_file}")
print("="*50)
print("     SMART FILE ORGANIZER")
print("="*50)
print("\nАвтоматическая сортировка файлов по категориям\n")

folder = input("Путь к папке (или '.' для текущей): ").strip()

if folder == '.' or folder == '':
    folder = os.getcwd()
if not os.path.exists(folder):
    print("❌ Папка не найдена!")
    exit()
organizer = FileOrganizer(folder)
print("\n--- ШАГ 1: ПРЕДПРОСМОТР ---")
organizer.organize(dry_run=True)
print("\n" + "="*50)
confirm = input("\nВыполнить сортировку? (да/нет): ").strip().lower()
if confirm == "да":
    print("\n--- ШАГ 2: СОРТИРОВКА ---")
    organizer = FileOrganizer(folder)
    organizer.organize(dry_run=False)
    print("\n✅ Готово!")
else:
    print("\n❌ Отменено")
