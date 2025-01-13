# Superclass
class Animal:
    def speak(self):
        return "I am an animal!"

# Subclass Dog
class Dog(Animal):
    def speak(self):
        return "Woof woof!"

# Subclass Cat
class Cat(Animal):
    def speak(self):
        return "Meow!"

# List of different animals
animals = [Animal(), Dog(), Cat()]

# Calling the 'speak' method for each object
for animal in animals:
    print(animal.speak())


