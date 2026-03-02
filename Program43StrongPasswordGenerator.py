import random 
import string
print("=== ГЕНЕРАТОР ПАРОЛЕЙ ===\n")

length = int(input("Длина пароля (8-32): "))
use_lower = input("Строчные буквы? (да/нет): ").lower()=="да"
use_upper = input("Заглавные буквы? (да/нет): ").lower() == "да"
use_digits = input("Цифры? (да/нет): ").lower() == "да"
use_symbols = input("Символы (!@#$...)? (да/нет): ").lower() == "да"

chars = ""
if use_lower:
    chars += string.ascii_lowercase
if use_upper:
    chars += string.ascii_uppercase
if use_digits:
    chars += string.digits
if use_symbols:
    chars += "!@#$%^&*"

if not chars:
    print("❌ Выбери хотя бы один тип символов!")
    exit()

password = ''.join(random.choice(chars) for _ in range (length))
print(f"\n🔒 Твой пароль: {password}")
score = 0 
if len(password) >=12: 
    score += 2
if use_lower and use_upper: 
    score += 1
if use_digits: 
    score += 1
if use_symbols: 
    score += 2
if score>=5:
    print("💪 Сила: ОЧЕНЬ СИЛЬНЫЙ")
elif score >= 3:
    print("⚡ Сила: СРЕДНИЙ")
else:
    print("⚠️ Сила: СЛАБЫЙ")

save = input("\nСохранить в файл? (да/нет): ").lower()
if save == "yes":
    filename = input("Имя файла (например passwords.txt): ")
    with open(filename, 'a', encoding = 'utf-8') as f:
        from datetime import datetime
        f.write(f"{datetime.now().strftime('%d.%m.%Y %H:%M')} | {password}\n")
    print(f"✅ Сохранено в {filename}")
