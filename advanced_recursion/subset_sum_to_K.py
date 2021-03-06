'''

Given an array A of size n and an integer K, return all subsets of A which sum to K.
Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
Note : The order of subsets are not important.
Input format :
Line 1 : Integer n, Size of input array
Line 2 : Array elements separated by space
Line 3 : K 
Constraints :
1 <= n <= 20
Sample Input :
9 
5 12 3 17 1 18 15 3 17 
6
Sample Output :
3 3
5 1


'''




def subset(arr, k):
    n=len(arr)
    if(n==1):
        if(arr[0]==k):
            output = [ [k] ]
            return output
        else:
            output = []
            return output

    output1 = subset(arr[:-1], k)
    output2 = subset(arr[:-1], k-arr[-1])
    for lst in output2:
        lst.append(arr[-1])
    if arr[-1]==k:
        output2.append([k])
    return output1 + output2

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
k=int(input())
output=subset(arr, k)
for lst in output:
    print(*lst)



    

