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


# In this example:

# We have a base class Animal with methods and properties.

# Dog, Cat, and Bird are subclasses that inherit from Animal and override the speak method.

# We use encapsulation to protect the name property in the Animal class.

# Instances like dog1, cat1, and bird1 are created from the subclasses, and we loop through them to call their specific speak methods.


# Base class - Animal (Superclass)
class Animal:
    # Constructor to initialize attributes
    def __init__(self, name, species):
        self.name = name    # public attribute
        self.__species = species  # private attribute

    # Method to make sound, but will be overridden by subclasses (abstraction)
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")
    
    # Getter for the private __species attribute (encapsulation)
    def get_species(self):
        return self.__species

# Dog class inherits from Animal (Inheritance)
class Dog(Animal):
    def __init__(self, name, breed):
        # Call to the parent class constructor
        super().__init__(name, "Dog")
        self.breed = breed

    # Override the speak method (Polymorphism)
    def speak(self):
        return f"{self.name} barks!"

# Cat class inherits from Animal (Inheritance)
class Cat(Animal):
    def __init__(self, name, color):
        # Call to the parent class constructor
        super().__init__(name, "Cat")
        self.color = color

    # Override the speak method (Polymorphism)
    def speak(self):
        return f"{self.name} meows!"

# Bird class inherits from Animal (Inheritance)
class Bird(Animal):
    def __init__(self, name, wing_span):
        # Call to the parent class constructor
        super().__init__(name, "Bird")
        self.wing_span = wing_span

    # Override the speak method (Polymorphism)
    def speak(self):
        return f"{self.name} chirps!"

# Creating instances of the subclasses
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Black")
bird = Bird("Flappy", "1 meter")

# Accessing methods of different instances
print(dog.speak())  # Polymorphism - Calls Dog's speak
print(cat.speak())  # Polymorphism - Calls Cat's speak
print(bird.speak())  # Polymorphism - Calls Bird's speak

# Accessing the private species attribute via the getter method
print(dog.get_species())  # "Dog"
print(cat.get_species())  # "Cat"
print(bird.get_species())  # "Bird"
