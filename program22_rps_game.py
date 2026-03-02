import random

print("=== КАМЕНЬ НОЖНИЦЫ БУМАГА ===\n")

choices = ["камень", "ножницы", "бумага"]

score_player = 0
score_bot = 0
rounds = 0
stats = {
    "wins": 0,
    "losses": 0,
    "draws": 0,
    "total": 0
}

while True:
    print(f"\nСчёт: Ты {score_player} — {score_bot} Бот")
    print("Выбери: камень / ножницы / бумага / стоп")
    
    player = input("\nТвой выбор: ").lower()
    
    if player == "стоп":
        break
    
    if player not in choices:
        print("❌ Неверный выбор!")
        continue
    
    bot = random.choice(choices)
    print(f"Бот выбрал: {bot}")
    
    rounds += 1
    stats["total"] += 1

    if player == bot:
        print("🤝 Ничья!")
        stats[ "draws"] += 1
    elif (
        (player == "камень" and bot == "ножницы") or
        (player == "ножницы" and bot == "бумага") or
        (player == "бумага" and bot == "камень")
    ):
        print("🎉 ТЫ ПОБЕДИЛ!")
        score_player += 1
        stats["wins"] += 1

    else:
        print("💀 БОТ ПОБЕДИЛ!")
        score_bot += 1
       # stats["total"] += 1
        stats["losses"] += 1

print(f"\n=== ИТОГ ===")
print(f"Раундов: {rounds}")
print(f"Ты: {score_player} | Бот: {score_bot}")

if score_player > score_bot:
    print("🏆 Общая победа за тобой!")
elif score_bot > score_player:
    print("🤖 Бот выиграл серию!")
else:
    print("🤝 Общая ничья!")

print(f"\n=== СТАТИСТИКА ===")
print(f"Всего раундов: {stats['total']}")
print(f"Побед: {stats['wins']}")
print(f"Поражений: {stats['losses']}")
print(f"Ничьих: {stats['draws']}")

if stats['total'] > 0:
    winrate = (stats['wins'] / stats['total']) * 100
    print(f"Винрейт: {winrate:.1f}%")
    
    if winrate >= 60:
        print("🏆 Ты доминируешь!")
    elif winrate >= 40:
        print("⚔️ Равная борьба!")
    else:
        print("💀 Бот тебя уделывает!")