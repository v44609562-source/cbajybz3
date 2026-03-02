print('Hello, world!')
print('What is your name?')  # Ask for their name.
my_name = input('>')
print('It is good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))
print('What is your age?')  # Ask for their age.
my_age = input('>')
print('You will be ' + str(int(my_age) + 1) + ' in a year.')



name = "Марк"
age = 16
goal = 10000  # долларов в месяц

# 2. Вывод на экран
print("=== МОЯ ИНФОРМАЦИЯ ===")
print("Меня зовут:", name)
print("Мне", age, "лет")
print("Моя цель:", goal, "$ в месяц")

# 3. Математика
hours_per_day = 4
days_in_year = 365
total_hours = hours_per_day * days_in_year
print("\n=== РАСЧЁТЫ ===")
print("Часов обучения в год:", total_hours)

# 4. Ввод данных от пользователя
print("\n=== ДАВАЙ ПОЗНАКОМИМСЯ ===")
user_name = input("Как тебя зовут? ")
user_age = input("Сколько тебе лет? ")

# 5. Вывод результата
print("\nПривет,", user_name + "!")
print("Тебе", user_age, "лет - отличный возраст для программирования!")


len('hello')
print(len)