
# Lists

# largest number of list
numbers = [3,100,9,8,9,48,]
max_numer = numbers[0]

for number in numbers:
    if number > max_numer:
        max_numer = number
print(max_numer)


# 2D (dimensional) List

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# List Methods

numbers.append(50)
print(numbers)
numbers.insert(0, 52)
print(numbers)
numbers.remove(100)
print(numbers)
# numbers.clear()
numbers.pop() # last item
print(numbers)
print(numbers.index(52)) # index number
print(50 in numbers) # Boolean if Exist/not
print(numbers.count(9)) # total number times

# Sort/Reverse number
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

# Sort/Reverse Text
numbers = ['F', 'A', 'd', 'e', 'c']
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers_copy = numbers.copy()
numbers.append('Y')
print(numbers_copy)


# Write a program to remove the duplicates in a list
print('remove the duplicates')

numbers = [3,100,9,8,9,48,8,9,100]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(unique_numbers)


# Tuples // immutable List
# can not add/remove/update any item in the tuples list, can just get/count item

numbers = (1, 2, 3)
print(numbers[1])


# Unpacking

coordinates = [1, 2, 3]
x, y, z = coordinates
print(x, y, z)












