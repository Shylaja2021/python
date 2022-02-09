class SIVariable:
    staticVariable=10

    def __init__(self):
        self.insta1=20
        self.insta2=30

s=SIVariable()
print("Static variable using className ",SIVariable.staticVariable)
print("Static variable using object ",s.staticVariable)
print("instance variable1 using object ",s.insta1)
print("instance variable2 using object ",s.insta2)

# cant access instance varibles using classname
# print("instance variable1 using className ",SIVariable.insta1)
# print("instance variable2 using className ",SIVariable.insta2)
print("assigning new value to Static variable using instance(object) ")
print("Static variable before change ",s.staticVariable)
s.staticVariable=100
print("Static variable using object after value change ",s.staticVariable)
print("Static variable using className after value change ",SIVariable.staticVariable)

print("assigning new value to Static variable using className ")
print("Static variable before change ",SIVariable.staticVariable)
SIVariable.staticVariable=200
print("Static variable using className after value change ",SIVariable.staticVariable)
print("Static variable using object after value change ",s.staticVariable)
