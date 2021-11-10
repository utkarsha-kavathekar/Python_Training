class OverloadAdd:
    def __init__(self, a):
        self.a = a
 
    # adding two objects
    def __add__(self, o):
        return self.a + o.a
ob1 = OverloadAdd(1)
ob2 = OverloadAdd(2)
ob3 = OverloadAdd("Hello")
ob4 = OverloadAdd("python")
 
print(ob1 + ob2)
print(ob3 + ob4)

#operator overloading + for complex no
class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
     # adding two objects
    def __add__(self, other):
        return self.a + other.a, self.b + other.b
 
Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)