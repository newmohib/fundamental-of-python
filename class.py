
# Class

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
# point1.x = 10
# point1.y = 20
print(point1.x)
point1.draw()

point2 = Point(30, 50)

# Constant

class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


persone = Person("Mohib")
persone.talk()



# Inheritance: inheritance is a mechanising of reuse of code

class Mammal:
    def walk(self):
        print("walk")


# python do not accepet any empty class, due to we add pass then its working fin here

class Dog(Mammal):
    pass


class Cat(Mammal):
    def bark(self):
        print("bark")


dog = Dog()
dog.walk()

cat = Cat()
cat.walk()
cat.bark()


