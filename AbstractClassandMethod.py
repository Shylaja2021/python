import abc as a

class Shape(a.ABC):
    @a.abstractmethod
    def area(self):
        pass
    def demo(self):
        print("hello")

class Recatange(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(f"Area of Rectangle : {self.l*self.b}")

class Square(Shape):
    def __init__(self,s):
        self.s=s
    def area(self):
        print(f"Area of Square : {self.s*self.s}")

class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print(f"Area of Circle : {3.14*self.r*self.r}")

class Triangle(Shape):
    def __init__(self,h,b):
        self.h=h
        self.b=b
    def area(self):
        print(f"Area of Triangle : {(self.h*self.b)/2}")

r=Recatange(10,20)
r.area()

s=Square(5)
s.area()

c=Circle(8)
c.area()

t=Triangle(5,4)
t.area()

# shape=Shape()
t.demo()