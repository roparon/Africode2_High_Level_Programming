class Animal:
    def __init__(self, name, species):
        self.__name = name
        self.__species = species
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def speak(self):
        return f"{self.get_name()} says Woof!"
    
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def speak(self):
        return f"{self.get_name()} says Meow!"
    
class Bird(Animal):
    def __init__(self, name, wing_span):
        super().__init__(name, "Bird")
        self.wing_span = wing_span
    
    def speak(self):
        return f"{self.get_name()} chirps!"
    
dog1 = Dog("Max", "Golden Retriever")
cat1 = Cat("Whiskers", "Gray")
bird1 = Bird("Tweety", "Small")

animals = [dog1, cat1, bird1]

for animal in animals:
    print(animal.speak())
