'''

Given an integer n, count and return the number of zeros that are present in the given integer using recursion.
Input Format :
Integer n
Output Format :
No. of 0s
Sample Input :
10204
Sample Output
2

'''




def countzeros(n):

    if n<0:
        n*=-1

    if n<10:
        if n==0:
            return 1
        return 0

    smallOutput=countzeros(n//10)

    if n%10==0:
        smallOutput+=1
    return smallOutput


    
n=int(input())

print(countzeros(n))
