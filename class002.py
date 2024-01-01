class Fun:
    def __init__(self, name, sex, age, game):
        self.name = name
        self.sex = sex
        self.age = age
        self.game = game

    def walk(self):
        print(f"{self.name} is walking Sexy")

    def dance(self):
        print(f"{self.name} is dancing in style")

    def enjoy(self):
        print(f"{self.name} is having a great time")

human1 = Fun("Alex", "male", 32, "playing a game")
human2 = Fun("Katrina", "female", 16, "enjoying a hobby")
human3 = Fun("Lena", "female", 17, "having fun with friends")

print(f"{human1.name} is playing with {human2.name} and {human3.name} and together they are having lots of fun")
human1.dance()
human2.walk()
human3.enjoy()
