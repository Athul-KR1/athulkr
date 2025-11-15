age=18 #int
name="vijay" #string
weight=20.5 #float
print(age)
print(name)
print(weight)



x=50+60
print(x)
y="good"+"5"
print(y)


is_valid=True
print(is_valid)

x=10
y=20
T=x
x=y
y=T
print(x)
print(y)


x=10
y=20
x,y=y,x
print(x,y)


print(id(10))
print(id(20))

a=10
b=a
b=20
print(b is a)

x=10
print(type(x))

x=10.5
y=5.6
print(type(x))
print(type(y))

x={1,2,3,4}
print(type(x))

x=[1,2,3]
x[0]=2
print(x)
# y=(1,2,3)
# y[0]=3
# print(y)

x=[1,2,3]
x[0]=2
x.append(4)
print(x)
x.insert(1,4)
print(x)
x.count(1)
print(x.count(1))
x.remove(4)
print(x)
print(x.pop())
print(x)
x.pop(1)
print(x)
del x[1]
print(x)
x.reverse()
print(x)
x.sort()
print(x)


x=(1,2,3,3)
print(set(x))

s={1,2,3}
s.add(5)
print(s)
s.update([5,6])
print(s)
s.discard(3)
print(s)
s.remove(5)
print(s)
s.clear()
print(s)
