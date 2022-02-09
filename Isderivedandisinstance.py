class Base:
    pass

class Derived(Base):
    pass


print("issubclass(Base,Derived) : ",issubclass(Base,Derived))
print("issubclass(Derived,Base) : ",issubclass(Derived,Base))

b=Base()
d=Derived()

print("isinstance(d,Base) :",isinstance(d,Base))
print("isinstance(b,Derived) : ",isinstance(b,Derived))
print("isinstance(b,Base) : ",isinstance(b,Base))
print("isinstance(d,Derived) : ",isinstance(d,Derived))