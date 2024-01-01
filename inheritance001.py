class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} meows!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.bark()  # Output: "Buddy barks!"
cat.meow()  # Output: "Whiskers meows!"
