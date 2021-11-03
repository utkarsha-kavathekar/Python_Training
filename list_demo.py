#Using some basic functions to work with list

list1=[34,98,22,54,18,39,73]
print("list1: ")
print(list1)

print("Length of list1:%d "%len(list1))
print("Element at index 3 is %d "%list1[3])

print("Slicing list:")
print(list1[1:5])

list1[4]="modified value at index 4"
list1.append("appended string")
list1.insert(5,"inserted at index 5")
print(list1)

list1.remove(73)
print("Poped value from list is %s "%list1.pop())
list1.extend(["extended","Values","of list"])
print(list1)

list2=list1
print("Reversing list2")
list2.reverse()
print(list2)

print(39 in list1)

#New list functions
list3=[86,23,76,11,49]
print(list3)
list3.sort()
print(list3)

print(type(list3))
list3.append(55)
list3.extend([72,93,11])
print("Index of 55 is ",list3.index(55))
print("Max of list:",max(list3))
print("Min of list:",min(list3))
print("Sum of list:",sum(list3))
print("count of 11 in list",list3.count(11))
#This fun do not work in python 3.x
"""
l1=[91,12,34]
l2=[87,56,33]
print("Comapring list ",cmp(l1,l2))
"""






