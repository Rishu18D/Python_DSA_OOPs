class human:
    def __init__(self,name,sex,age,color):
        self.name=name
        self.sex=sex
        self.age=age
        self.color=color
    def talk(self):
        print(f"{self.name} can talk")
    def walk(self):
        print(f"{self.name} can walk")
    def dance(self):
        print(f"{self.name} can dance")
man1=human("Babu","male",32,"Brown")
man2=human("Bittu","male",43,"white")
man3=human("Sona","female",16,"while")
print(f"the {man1.name} is playing with {man3.name} and {man2.name} is watching")
man3.talk()
man3.walk()
man3.dance()