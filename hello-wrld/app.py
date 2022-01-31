import math

name = input('What is your name? ')
favorite_color = input('What is your favorite color? ')
print(name + ' likes ' + favorite_color)

birth_year = input('Birth year: ')
print(type(birth_year))
age = 2022 - int(birth_year)
print(type(age))
print(age)

weight_lbs = input('Weight (lbs): ')
weight_kg = round(int(weight_lbs) * 0.45)
print(weight_kg)

text = 'Python for Beginners'
print(text[:])
print(text[:3], text[3:])
print(text[1:-1])
print(len(text))
print(text.upper())
print(text.lower())
print(text.find('P'))
print(text.replace('Beginners', 'Masters'))
print('Python' in text)

email = '''
Hi mate,
Here is my first email to you.

Cheers,
Spencer
'''
print(email)

first = 'Zoltan'
last = 'Busi'
msg = f'{first} [{last}] is a coder'
print(msg)

print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x += 3
x -= 6
print(x)

print(abs(-2.9))
ceil = math.ceil(2.9)
print(ceil)

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a cold day")
else:
    print('Enjoy your day')

if is_hot and is_cold:
    print('What a fuck?!')
if not is_hot and not is_cold:
    print('Really?!')

temp = 30

if temp >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
