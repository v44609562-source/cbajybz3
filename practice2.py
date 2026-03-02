spam= True 
print(spam)
false= '2+2'
print(false)


a= 42
b= 42 
print(f"{a} == {b} это {a == b}")  # True

my_age= True
b= True
print(f"{my_age} == {b} this {a == b}")



name = 'MARK'
if name == 'Alice':
    print('Hi, Alice.')
else: 
    print('go to нахуй')



name = 'Alic'
age = 3
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')


today_is_opposite_day = True

# Set say_it_is_opposite_day based on today_is_opposite_day:
if today_is_opposite_day == True:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False

# If it is opposite day, toggle say_it_is_opposite_day:
if today_is_opposite_day == True:
  say_it_is_opposite_day = not say_it_is_opposite_day

# Say what day it is:
if say_it_is_opposite_day == True:
    print('Today is Opposite Day.')
else:
    print('Today is not Opposite Day.')
