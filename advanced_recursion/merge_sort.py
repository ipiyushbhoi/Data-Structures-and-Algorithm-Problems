'''

Sort an array A using Merge Sort.
Change in the input array itself. So no need to return or print anything.
Input format :
Line 1 : Integer n i.e. Array size
Line 2 : Array elements (separated by space)
Output format :
Array elements in increasing order (separated by space)
Constraints :
1 <= n <= 1000
Sample Input:
6 
2 6 8 5 4 3
Sample Output:
2 3 4 5 6 8

'''




def mergeSort(arr,start,end):

    size=end-start
    if size<=1:
        return

    mid=(start+end)//2
    mergeSort(arr,start,mid)
    mergeSort(arr,mid,end)

    result=[0]*size

    i=start
    j=mid
    k=0
    
    while i<mid and j<end:
        if arr[i]<arr[j]:
            result[k]=arr[i]
            k+=1
            i+=1
        else:
            result[k]=arr[j]
            k+=1
            j+=1
        
    while i<mid:
        result[k]=arr[i]
        k+=1
        i+=1

    while j<end:
        result[k]=arr[j]
        k+=1
        j+=1

    for i in range(size):
        arr[start+i]=result[i]
            
    
n=int(input())
arr=list(map(int,input().split()))
mergeSort(arr,0,n)

for i in arr:
    print(i,end=' ')

