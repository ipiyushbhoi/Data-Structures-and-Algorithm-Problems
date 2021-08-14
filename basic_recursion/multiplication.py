'''

Given two integers m & n, calculate and return their multiplication using recursion. You can only use subtraction and addition for your calculation. No other operators are allowed.
Input format : m and n (in different lines)

Sample Input :
3 
5
Sample Output -
15

'''




def multiply(m,n):

    if m==0 or n==0:
        return 0
    smallOutput=multiply(m,n-1)
    
    return smallOutput+m


    
m=int(input())
n=int(input())

print(multiply(m,n))
