class Variables:
    # private var
    __privateVar=12
    # def fun1(self,age,name):
    #     # instance var
    #     self.age=age
    #     # protected var
    #     self._name=name
    def __init__(self,age,name):
        # instance var
        self.age=age
        # protected var
        self._name=name

class Derived(Variables):
    def printVars(self):
        print("age",self.age)
        print("name",self._name)
        # print("private variable",self.__privateVar)

# v=Variables(22,"peter")
# v.fun1(22,"peter")
d=Derived(22,"peter")
d.printVars()