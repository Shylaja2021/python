# using default argument
class MethodOverload:
    # def sum(self,a,b):    error
    #     print(f"sum is {a+b}")

    def sum(self,a,b,c=0):
        print(f"sum is {a+b+c}")
print("using default argument")
m=MethodOverload()
m.sum(2,3)
m.sum(2,3,4)

#using variable length

class MethodOverload1:
    # def sum(self,a,b):    error
    #     print(f"sum is {a+b}")

    def sum(self,*args):
        result=0
        for num in args:
            result+=num
        print(f"sum is {result}")
print("using varible length argument")
m=MethodOverload1()
m.sum(2,3)
m.sum(2,3,4)
