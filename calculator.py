number = int(input("Введите число для таблицы умножения: "))
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")