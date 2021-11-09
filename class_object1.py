class Circle:
    pi=3.142     #class variable same as static varible
    all_circles=[]
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.radius*self.radius*Circle.pi   #class varible accessed with class name 
                                                    # its value is comman to all objects
    #decorater used to denote static method
    @staticmethod       
    def testStatic():
        print("inside the testStatic() static method")
        print('You can access static varible pi here',Circle.pi)
    
    @classmethod
    def totalArea(classnm):
        total=0
        for c in classnm.all_circles:
            total=total+c.area()
        return total



if __name__=='__main__':
    print('class varibale pi=',Circle.pi)
    c1=Circle(4)
    print("area is ",c1.area())

    c2=Circle(5)
    print("area is ",c2.area())

    #object is not required to call static method
    Circle.testStatic()
    #object can be used to call it but it has no meaning
    c1.testStatic()

    Circle.all_circles=[c1,c2]
    print('total area ',Circle.totalArea())


