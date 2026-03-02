# Program 22: Pomodoro таймер для фокуса

import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(minutes, label):
    total_seconds = minutes * 60
    
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        
        clear_screen()
        print(f"\n{'='*40}")
        print(f"   {label}")
        print(f"{'='*40}\n")
        print(f"        ⏱️  {timer}")
        print(f"\n{'='*40}")
        print("\n   Фокусируйся на задаче!")
        print("   (Ctrl+C для остановки)")
        
        time.sleep(1)
        total_seconds -= 1
    
    clear_screen()
    print(f"\n🎉 {label} ЗАВЕРШЁН!")
    print("\a")  # Звуковой сигнал

def pomodoro():
    session = 1
    
    while True:
        print(f"\n🍅 POMODORO — Сессия {session}")
        input("Нажми Enter чтобы начать...")
        
        
        # 25 минут работы
        countdown(25, f"РАБОТА — Сессия {session}")
        
        if session % 4 == 0:
            # Длинный перерыв после 4 сессий
            print("\n✅ 4 сессии выполнены! Длинный перерыв.")
            input("Нажми Enter для перерыва 15 минут...")
            countdown(15, "ДЛИННЫЙ ПЕРЕРЫВ")
        else:
            # Короткий перерыв
            print("\n✅ Сессия завершена! Короткий перерыв.")
            input("Нажми Enter для перерыва 5 минут...")
            countdown(5, "ПЕРЕРЫВ")
        
        session += 1
        
        continue_work = input("\nПродолжить? (да/нет): ").lower()
        if continue_work != "да":
            print(f"\n🎯 Завершено сессий: {session - 1}")
            print(f"⏱️ Время работы: {(session - 1) * 25} минут")
            print("\n💪 Отличная работа!")
            break

# Меню
print("=== POMODORO TIMER ===")
print("\n25 минут работы → 5 минут перерыв")
print("После 4 сессий → 15 минут перерыв\n")

pomodoro()