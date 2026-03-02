import random
questions = [
    {
         "question": "Столица Беларуси?",
        "options": ["Минск", "Москва", "Киев", "Варшава"],
        "correct": 0
    },
    {
        "question": "2 + 2 * 2 = ?",
        "options": ["8", "6", "4", "10"],
        "correct": 1
    },
]

score = 0 
for q in random.sample(questions , 2):
    print(f"\n{q['question']}")
    for i, opt in enumerate (q['options'], 1):
        print(f"{i}. {opt}")
    
    try:
        answer = int(input("Answer:")) - 1
        if answer == q['correct']:
            print("all rigth")
            score += 1 
        else:
            print(f" dont rigth. answer: {q['options'][q['correct']]}")
    except ValueError:
        print("Ошибка! Нужно вводить ЦИФРУ номера ответа.")

print(f"\n result of {score}/ {len(questions)}")