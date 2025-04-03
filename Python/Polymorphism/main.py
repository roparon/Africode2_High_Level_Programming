# Polymorphism - Comes from the Greek word "polus" meaning many and "morphe" meaning form
# its a programming concept that allows same methods to behave differently depending on the object
#1. Methods overriding
#2. Methods overloading
#3. operator overloading
#4. Duck typing



#1. Methods Overriding
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    


    #2. Methods Overloading
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c
    
op1 = MathOperations()
print(op1.add(2, 4))  # Output: 6
print(op1.add(2, 4, 6))  # Output: 12