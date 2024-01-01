#Muktiple inheritance...
class Singer:
    def sing(self):
     return "la la la"
class Dancer:
    def dance(self):
     return "shake you body!"
class Performer(Singer,Dancer):
     pass
performer=Performer()
print(performer.sing())
print(performer.dance())     