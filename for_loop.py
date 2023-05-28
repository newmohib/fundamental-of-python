
# for loop

# String Loop

name = 'Python'
for item in name:
    print(item)

list = ['javaScript', 'java', 'python']
for item in list:
    print(item)

print('Range to End')

range_item = range(5)
for item in range_item:
    print(item)

print('Range Start to End')

range_item = range(10, 15)
for item in range_item:
    print(item)

print('Staps')
range_item = range(20, 30, 3)
for item in range_item:
    print(item)

# price calculation

prices = [10,20,30]
total = 0
for price in prices:
    total += price # augmented
print(f"Total: {total}")


# Nested Loops

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

print('Shape')
lists = [5,2,5,2,2]
for item in lists:
    print('x' * item)











