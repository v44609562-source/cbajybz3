# Проверка силы пароля

def check_password(pwd):
    score = 0
    
    if len(pwd) >= 8: score += 1
    if len(pwd) >= 12: score += 1
    if any(c.isupper() for c in pwd): score += 1
    if any(c.islower() for c in pwd): score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c in "!@#$%^&*" for c in pwd): score += 1
    
    if score <= 2: return "❌ Слабый"
    elif score <= 4: return "⚠️ Средний"
    else: return "✅ Сильный"

while True:
    pwd = input("\nПароль (или 'выход'): ")
    if pwd == "выход": break
    print(f"Сила: {check_password(pwd)}")