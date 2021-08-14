'''

Sort an array A using Quick Sort.
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




def quickSort(arr,start,end):

    size=end-start
    if size<=1:
        return

    pivot=start
    count=start

    for i in range(start+1,end):
        if arr[i]<=arr[pivot]:
            count+=1

    arr[pivot],arr[count]=arr[count],arr[pivot]
    pivot=count

    left=start
    right=end-1

    while left<pivot:
        while arr[left]<=arr[pivot] and left<pivot:
            left+=1
            
        if left>=pivot:
            break

        while arr[right]>arr[pivot]:
            right-=1
            
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1

    quickSort(arr,start,pivot)
    quickSort(arr,pivot+1,end)


    
n=int(input())
arr=list(map(int,input().split()))
quickSort(arr,0,n)

for i in arr:
    print(i,end=' ')

