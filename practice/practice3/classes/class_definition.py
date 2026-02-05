# 1) Simple class with attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 20)
print(p.name, p.age)


# 2) Class with a method
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(3, 5))


# 3) Class with default value
class Car:
    def __init__(self, brand="Unknown"):
        self.brand = brand

c1 = Car()
c2 = Car("Toyota")
print(c1.brand, c2.brand)


# 4) Class with two methods
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

r = Rectangle(4, 5)
print(r.area(), r.perimeter)


# 5) Class with class variable
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
c = Counter()
print(Counter.count)