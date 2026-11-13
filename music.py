from abc import ABC, abstractmethod


# 1. Abstraction: Create an abstract base (parent) class
class Animal(ABC):

  def __init__(self, name, species):
    # Common setup code shared by all child classes
    self.name = name
    self.species = species

  # Inherited method available to all child classes
  def describe(self):
    print(f"{self.name} is a {self.species}.")

  # 2. Force every child class to implement its own play_sound() method
  @abstractmethod
  def play_sound(self):
    pass


# 3. Inheritance: Child class 1
class Dog(Animal):

  def __init__(self, name, breed):
    # Call the parent constructor to avoid rewriting setup code
    super().__init__(name, species="Dog")
    self.breed = breed

  # Required implementation of the abstract method
  def play_sound(self):
    print(f"{self.name} says: Woof! Woof!")

  # Custom method unique to Dog
  def fetch(self, item):
    print(f"{self.name} the {self.breed} fetches the {item}.")


# 4. Inheritance: Child class 2
class Cat(Animal):

  def __init__(self, name, indoor=True):
    # Call the parent constructor using super()
    super().__init__(name, species="Cat")
    self.indoor = indoor

  # Required implementation of the abstract method
  def play_sound(self):
    print(f"{self.name} says: Meow!")

  # Custom method unique to Cat
  def scratch(self):
    print(f"{self.name} scratches the scratching post.")


# 5. Create objects from child classes and call methods
if __name__ == "__main__":
  dog = Dog("Buddy", "Golden Retriever")
  cat = Cat("Whiskers")

  # Calling inherited methods
  dog.describe()
  cat.describe()

  print("-" * 30)

  # Calling overridden abstract methods
  dog.play_sound()
  cat.play_sound()

  print("-" * 30)

  # Calling custom child methods
  dog.fetch("ball")
  cat.scratch()
  