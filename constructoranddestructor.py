class DefaultConstructor:
    def __init__(self):
        self.name="default"
        print("default constructor : ",self.name)


class ParamConstructor:
    def __init__(self,name):
        self.name=name


    def __del__(self):
        print("deleted......")

    def display(self):
        print(f"parametraised constructor : {self.name}")

c=DefaultConstructor()
p=ParamConstructor("john")
p.display()
