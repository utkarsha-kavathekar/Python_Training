class Parent1:
    def foo(self):
        print('Called parent1 foo()')

class Parent2:
    def foo(self):
        print('Called parent2 foo()')

    def bar(self):
        print('Called parent2 bar()')

class Child1(Parent1,Parent2):
    pass

class Child2(Parent1,Parent2):
    def foo(self):
        print('Called child2 foo()')

    def bar(self):
        print('Called child2 bar()')

class GrandChild(Child1,Child2):
    pass

gcObj=GrandChild()
gcObj.foo()
print('--------------------------')
gcObj.bar()
print('--------------------------')

chld1Obj=Child1()
chld1Obj.foo()
print('---------------------------')
chld1Obj.bar()
print('---------------------------')
Parent2.foo(chld1Obj)