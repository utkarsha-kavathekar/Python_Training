class SayHello:
    def __init__(self):         #constuctor with object as default arg
        print('Self is object passed as default',self)
        self.greet='This is instance varible greet'  #instantiating instance varible 'greet'

    def display(self,objno):
        print(self.greet,'of object no',objno)

#Creating object of class SayHello
obj1=SayHello()
print(obj1.greet)
obj1.display(1)

obj2=SayHello()
print(obj2.greet)
obj2.display(2)


