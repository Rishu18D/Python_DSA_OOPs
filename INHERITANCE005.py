#Multilevel inheritance...
class Grandparent:
    def greet(self):
     return "Hello from Grandparent✌️✌️" 
class Parent(Grandparent):
    def greet(self):
     return "Hello from parent✌️✌️" 
class Child(Parent):
    pass
child=Child()
print(child.greet())    