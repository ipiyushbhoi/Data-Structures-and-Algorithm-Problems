'''

Given an integer sorted array (sorted in increasing order) and an element x, find the x in given array using binary search. Return the index of x.
Return -1 if x is not present in the given array.
Note : If given array size is even, take first mid.
Input format :

Line 1 : Array size

Line 2 : Array elements (separated by space)

Line 3 : x (element to be searched)

Sample Input :
6
2 3 4 5 6 8 
5 
Sample Output:
3 

'''



def binarySearchIndex(arr, start, end, val):
    if(start>end):
        return -1
    mid=(start+end)//2
    if(val == arr[mid]):
        return mid
    elif(val>arr[mid]):
        return binarySearchIndex(arr,mid+1,end,val)
    else:
        return binarySearchIndex(arr,start,mid-1,val)

def binarySearch(arr, val):
    n=len(arr)
    return binarySearchIndex(arr,0,n-1,val)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
val=int(input())
index=binarySearch(arr, val)
print(index)


    

