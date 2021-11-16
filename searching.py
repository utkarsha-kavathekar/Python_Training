def linearSearch(list1,no):
    for i in range(0,len(list1)):
        if(list1[i]==no):
            return i
       
    return 'not found'

def binarySearch(arr,no):
    low=0
    high=len(arr)-1
    mid=0

    while(low<=high):
        mid = (low+high)//2
        print('low:',low,' mid:',mid,' High:',high)

        if(arr[mid]<no):
            low=mid+1

        elif(arr[mid]>no):
            high=mid-1

        elif(arr[mid==no]):
            return mid
        
        else:
            print('inside while')
            return 'not found'
    return 'not found'   


list1 = [78,33,27,15,49,23,44,50,67]
print(list1)
print('index of 23 is ',linearSearch(list1,23))
print('index of 88 is ',linearSearch(list1,88))

list1.sort()
print(list1)
print('index of 23 is ',binarySearch(list1,23))
print('index of 88 is ',binarySearch(list1,88))
