'''

Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array. Return -1 if it is not present in the array.
Last index means, the index of first occurrence of x in the input array.
Do this recursively. Indexing in the array starts from 0.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x
Output Format :
Last index or -1
Constraints :
1 <= N <= 10^3
Sample Input :
4
9 8 10 8
8
Sample Output :
1

'''




def lastIndex(arr,x):

    n=len(arr)

    if n<=0:
        return -1
    
    smallOutput=lastIndex(arr[1:],x)

    if smallOutput==-1:
        if x==arr[0]:
            return 0
        else:
            return -1

    else:
        return smallOutput+1

    
l=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(lastIndex(arr,x))
