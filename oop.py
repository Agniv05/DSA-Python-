class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine has started.")

my_car = Car("Toyota", "Camry", 2022)  # Creating an object of class Car
my_car.start_engine()  # Calling a method on the object


# Encapsulation:
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number   # Public attribute
        self.__balance = balance               # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def __show_balance(self):                 # Private method
        print("Balance:", self.__balance)

#  Inheritance :
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Woof!"

my_dog = Dog("Buddy")
print(my_dog.name)     # Inherited from Animal
print(my_dog.speak())  # Overridden in Dog

#  Polymorphism :
class Bird:
    def sound(self):
        return "Chirp"

class Parrot(Bird):
    def sound(self):
        return "Squawk"

def make_sound(bird):
    print(bird.sound())

my_bird = Bird()
my_parrot = Parrot()
make_sound(my_bird)   # Output: Chirp
make_sound(my_parrot) # Output: Squawk

#  Abstraction:
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

my_circle = Circle(5)
print("Area of circle:", my_circle.area())

