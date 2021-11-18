def bubble_sort(list1):
    for i in range(0,len(list1)-1):

        for j in range(i+1,len(list1)):

            if list1[i]>list1[j]:

                temp=list1[i]
                list1[i]=list1[j]
                list1[j]=temp

    return list1

list2=[45,22,87,40,61,29,32,58,40]
print('List before sorting : ',list2)
print('List after bubble sorting : ',bubble_sort(list2))

def selection_sort(list1):

    for i in range(0,len(list1)):
        minindex=i
        for j in range(i+1,len(list1)):
            if list1[j]<list1[minindex]:
                minindex=j

        list1[minindex],list1[i]=list1[i],list1[minindex]
    return list1

print('List before sorting : ',list2)
print('List after selection sorting : ',bubble_sort(list2))