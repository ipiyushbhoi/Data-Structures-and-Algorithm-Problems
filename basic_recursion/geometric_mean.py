'''

Given k, find the geometric sum i.e.
1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
using recursion. Return the answer.
Sample Input :
3
Sample Output :
1.875

'''



import math
def geometricmean(n):

    if n==0:
        return 1

    smallOutput=geometricmean(n-1)
    
    return smallOutput+1/math.pow(2,n)


    
n=int(input())

print(geometricmean(n))
