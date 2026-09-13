"""
1) Import the required tools.
   a) Import `ABC` to create an abstract base class.
   b) Import `abstractmethod` to force child classes to define a method.

2) Create the abstract parent class.
   a) Create a class named `Animal`.
   b) Inherit from `ABC` to make it an abstract class.

3) Create the parent constructor.
   a) Define the `__init__()` method with `name` and `habitat`.
   b) Store these values as object attributes.

4) Create a common display method.
   a) Define the `display()` method.
   b) Print the animal’s name and habitat.
   c) Let all child classes use this method.

5) Create an abstract method.
   a) Use `@abstractmethod`.
   b) Define the `speak()` method.
   c) Leave it empty using `pass`.
   d) Make sure every child class must create its own version of `speak()`.

6) Create the `Dog` child class.
   a) Inherit from the `Animal` class.
   b) Use `super().__init__()` to call the parent constructor.
   c) Add an extra attribute for breed.
   d) Define the dog’s version of `speak()`.

7) Create the `Parrot` child class.
   a) Inherit from the `Animal` class.
   b) Use `super().__init__()` to set name and habitat.
   c) Add an extra attribute for phrase.
   d) Define the parrot’s version of `speak()`.

8) Create the `Lion` child class.
   a) Inherit from the `Animal` class.
   b) Use `super().__init__()` to set name and habitat.
   c) Add an extra attribute for pride.
   d) Define the lion’s version of `speak()`.

9) Create animal objects.
   a) Create one dog object.
   b) Create one parrot object.
   c) Create one lion object.

10) Run the animal sound show.
   a) Print the show title.
   b) Loop through all animal objects.
   c) Call `display()` for each animal.
   d) Call `speak()` for each animal.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display(self):
        print(f"Animal: {self.name}, habitat: {self.habitat}")


    @abstractmethod
    def speak(self):
         pass


class Dog(Animal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed

    def speak(self):
            print(f"Woof! My name is {self.name}, and I am a {self.breed}.")
            print(f"I live in the {self.habitat}.")


class Parrot(Animal):
     def __init__(self, name, habitat, phrase):
         super().__init__(name, habitat)
         self.phrase = phrase

     def speak(self):
            print(f"Hello! My name is {self.name}, and I can say '{self.phrase}'.")
            print(f"I live in the {self.habitat}.")


class Lion(Animal):
     def __init__(self, name, habitat, pride):
          super().__init__(name, habitat)
          self.pride = pride

     def speak(self):
          print(f"Roar! My name is {self.name}, and I am part of the {self.pride} pride.")
          print(f"I live in the {self.habitat}.")


dog = Dog("Bruno", "Home", "Golden Retriever")
parrot = Parrot("Polly", "Forest", "Polly wants a cracker.")
lion = Lion("Simba", "Savannah", "Pride of Simba")

print("Animal Sound Show")
print("==================")

for animal in [dog, parrot, lion]:
     animal.display()
     animal.speak()