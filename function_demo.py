#Different types of user defined function

def add(x,y):
    sum=x+y
    return sum

print("sum=",add(23,56))
"""
no1=int(input("Enter no1:"))
no2=int(input("Enter no2:"))
print("sum of %d and %d is"%(no1,no2),add(no1,no2))
"""
#Default arg fun
def defArg(s1,s2="welcome ",s3="Program"):
    print(s2+s1+s3)

defArg("python ")
defArg("java ","Bye ")
defArg("new ","Hello ","Project")

#keyword arg fun
def keyArg(a,b):
    if(a>b):
        print("a greater",a)
    else:
        print("b greater",b)

keyArg(15,20)
keyArg(b=8,a=67)

#variable no of positional arg
def varPosArg(listnm,*listItem):
    print(listnm)
    for item in listItem:
        print(item)

varPosArg("List of colors",'Blue','red','black','green')
varPosArg('List of subjects:','DBMS','Algorithm','ML')

#variable no of keyword arg
def varKeyArg(**argDict):
    for key,value in argDict.items():
        print(key," = ",value)

varKeyArg(name='riya',clg='MIT',dept='CSE')
varKeyArg(apple='red',banana='yellow')

#global variable
globalA="one"
globalB="Two"
print(globalA,globalB)
def globalVar():
    global globalA
    globalA='newvalA'
    globalB='newvalB'
globalVar()
print(globalA,globalB)

#Anonymous fun using lambda keyword
lowercase = lambda x:x.lower()
print(lowercase("UPPERCASE"))

square= lambda x:x*x
print("square of 8 is",square(8))

concat=lambda arg1,arg2,arg3:print(arg1+arg2+arg3)
concat("Anonymous fun ","with ","Multiple arg")

#Map function
def square1(x):
    return x*x
list1=[i for i in range(10)]
print(list1)
#map(fun,listofEle on which fun to apply) return new list
list2=list(map(square1,list1))
print(list2)
list2=list(map(lambda x:x+x,list1))
print(list2)

#Assignment1
#Given a string
#sentence = 'It is raining cats and dogs'
#get 1 target list with length of each word in this sentence

def getLengthOfEachWord(str1):
    list1=str1.split()
    return list(map(lambda s:len(s),list1))
    #print(list1)
print("list of len of each word in string 'It is raining cats and dogs'",getLengthOfEachWord('It is raining cats and dogs'))

