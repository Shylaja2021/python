class Base:
    def fun1(self):
        print("base class")
class Base2:
    def fun6(self):
        print("base 2")
class Child(Base):
    def fun2(self):
        print("child")

class SubChild(Child):
    def fun3(self):
        print("SubChild")

# class Multi(Base,Base2):
#     def fun4(self):
#         print("Multiple")
class Multi(Child,Base):
    def fun4(self):
        print("Multiple")

print("functions accessed from base")
b=Base()
b.fun1()
print("======================================")
print("functions accessed from child")
c=Child()
c.fun1()
c.fun2()
print("======================================")
print("functions accessed from subchild")
d=SubChild()
d.fun1()
d.fun2()
d.fun3()
print("======================================")
print("functions accessed from Multiple")
M=Multi()
M.fun4()

