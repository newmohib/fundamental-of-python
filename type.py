# price = 10
# # rating = 4.9
# name = 'Mohibr'
# is_publish = False
# print(name * 10)

full_name = 'Mohibur Rahman'

name = input('What is your name? ')
print('Hi ' + name)


# int()
# float()
# bool()

birth_year = input('Birth year: ')
age = 2019 - int(birth_year)
print(age)

weight_lbs = input('Weight (lbs)? ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)



email = '''
Hi Mohib,

Here is our first email to you 

Thank you,
The Support Team
'''
print(email)

course = 'Python for Beginners'
print(course[0])
print(course[-2])
print(course[0:3])
print(course[2:])
print(course[:5])
print(course[:])
print(course[1:-1]) # y-r

# formated String

first = 'Md'
last = 'Rahim'
msg = f'{first} {last} is a coder'
print(msg)

print(len(course))

print(course.upper())
print(course.capitalize())
print(course.replace('n', 'J'))
print('Python' in course)
print(course.find('Python'))


