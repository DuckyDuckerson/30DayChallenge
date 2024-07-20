import random

class Treat:
    def __init__(self, flavor, size):
        self.flavor = flavor
        self.size = size

    def bake(self):
        print(f"Baking a {self.size} {self.flavor} treat")
        if random.randint(1, 2) == 1:
            self.burn()

    def burn(self):
        print("The treat burnt!")

class Cake(Treat):
    def __init__(self, flavor, size):
        Treat.__init__(self, flavor, size)

    def slice(self, slices):
        print(f"The cake is sliced into {slices} slices")

    

cookie = Treat("chocolate chip", "large")
cake = Cake("chocolate", "large")
vanilla_cake = Cake("vanilla", "small")

cookie.bake()


cake.bake()
cake.slice(8)

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

sunny = Cat("Sunny")
rover = Dog("Rover")

pikachu = Animal("Pikachu")

sunny.speak()
rover.speak()
pikachu.speak()