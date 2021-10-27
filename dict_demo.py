#Using some basic functions to work with dictionary

dict1={'name':'Priya','clg':'DKTE','dept':'IT','city':'sangli'}
print(dict1)
print("name is %s "%dict1['name'])

if 'city' in dict1:
    print("City is %s "%dict1['city']) 

dict1['year']='Final Year'

dict2={'one':1,'two':2,'three':3}
print(dict2)
del dict2['two'] #delete specific value as per given key
print(dict2)
dict2.clear() #remove all elements in dict
print(dict2)

for key,value in dict1.items():
    print(key,":",value)

print(dict1.keys()) #list of all keys
print(dict1.values()) #list of all values

dict3={'dict3key':'dict3val'}
dict1.update(dict3)
print(dict1)

#Using some basic functions to work with set
list1=[1,2,6,3,6,9,2]
set1=set(list1)
print(set1)

set2=set([1,7,9,3,5])
print(set1 | set2)  #set union
print(set1 & set2)  #set intersection