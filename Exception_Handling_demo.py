#Handling file not found exception
def reading():
    try:
        f=open('notpresent.txt')
        print('Successful executed no exception arrived')

    except IOError as a:
        print('Could not open, file not present',a)

#Handling exception with multiple except blocks
def multiExcept(var1):
    try:
        res=float(var1)

    except ValueError as v:
        print(v)
        res='could not convert non number to float'
    except TypeError as t:
        print(t)
        res='This object type can not converted to float'
    finally:
        print('this is finally block executes in any condition')

    return res  
#user defined exception using'raise'
class MyError(Exception):
    pass
def userdefExcpt():
    try:
        raise MyError('This is user defined exception')
    except MyError as error:
        print("details ",error)  


reading()
print(multiExcept(45))
print(multiExcept('abc'))
print(multiExcept({'a':'456'}))
userdefExcpt()