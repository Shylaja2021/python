import array as arr
a=arr.array('u',['a','b','c'])

print("char array: ",end=" ")
for i in range(0,3):
    print(a[i],end=" ")

# str=arr.array('u',['abc','mno','xyz'])
#
# print("string array: ")
# for i in range(0,3):
#     print(str[i])
print()
b=arr.array('i',[1,2,3,4,1,5])
print("int array: ",end=" ")
for i in range(0,6):
    print(b[i],end=" ")
print()
b.append(6)
print("int array after append: ",end=" ")
for i in range(0,7):
    print(b[i],end=" ")
print()
b.insert(2,10)
print("int array after insert: ",end=" ")
for i in range(0,8):
    print(b[i],end=" ")
print()

b.pop(3)
print("int array after pop at index 3: ",end=" ")
for i in range(0,7):
    print(b[i],end=" ")
print()
b.remove(10)
print("int array after pop at index 3: ",end=" ")
for i in range(0,6):
    print(b[i],end=" ")
print()