class ClassName:
    def __init__(self, arg1, arg2, ...):
        self.attribute1 = arg1
        self.attribute2 = arg2
        # Initialization of other attributes or setup

class Person:
    def __init__(self, name, age):
        self.name = name  # Setting the name attribute
        self.age = age    # Setting the age attribute

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance of Person
person1 = Person("Alice", 30)
person1.introduce()  # Output: Hello, my name is Alice and I am 30 years old.
class Car:
    def __init__(self, make, model, year=2022):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Camry")
print(car1.year)  # Output: 2022 (uses the default value)



#  In Python, the __init__ method is a special method, often called the constructor, that is automatically called when an object (instance) of a class is created.
#  This method is typically used to initialize the instance's attributes and set up any necessary initial state. The double underscores in __init__ indicate that
#  it's a "magic" method with a special purpose in Python.

#  How __init__ Works
#  Parameters: The first parameter of __init__ is always self, which refers to the instance being created. Additional parameters can be added to set initial values for the instance attributes.
#  Initialization: Inside __init__, you can define attributes specific to the instance, often based on the arguments provided during object creation.
