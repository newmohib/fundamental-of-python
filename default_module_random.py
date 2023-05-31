
# Generating Random Values
# paython 3 module index

import random

for i in range(3):
    # random.random() this function is generate random value 0-1 like this 0.5863048082061596
    print(random.random())
    # randint this functions integer value
    print(random.randint(10, 20))


# return random item from list
members = ['John', 'Mary', 'Bob']
leader = random.choice(members)
print(leader)


#

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())

