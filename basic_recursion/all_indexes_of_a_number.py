'''

Given an array of length N and an integer x, you need to find all the indexes where x is present in the input array. Save all the indexes in an array (in increasing order).
Do this recursively. Indexing in the array starts from 0.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x
Output Format :
indexes where x is present in the array (separated by space)
Constraints :
1 <= N <= 10^3

Sample Input :
5
9 8 10 8 8
8
Sample Output :
1 3 4

'''




def allIndexes(arr,x):

    n=len(arr)

    if n<=0:
        return []
    
    smallOutput=allIndexes(arr[:n-1],x)

    if x==arr[n-1]:
        smallOutput.append(n-1)

    return smallOutput

    
l=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
ans=allIndexes(arr,x)
for i in ans:
    print(i,end=' ')
print()
