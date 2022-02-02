class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

    def get_pos(self):
        return (self.x, self.y)


point1 = Point(10, 20)
point1.draw()

point2 = Point(20, 40)
point2.move()

point3 = Point(30, 60)
print(point3.get_pos())


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('Hi there!')
        print('My name is ' + self.name)


peter = Person('Peter')
peter.talk()


class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('bark')


class Cat(Mammal):
    def be_annoying(self):
        print('annoying...')
