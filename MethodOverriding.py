class Base:
    def display(self):
        print("parent calss")

class Child(Base):
    def display(self):
        super(Child,self).display()
        print("child class")

c=Child()
c.display()