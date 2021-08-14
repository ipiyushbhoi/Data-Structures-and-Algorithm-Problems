'''
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to return the answer.
Do this recursively.
Input format :
Two integers x and n (separated by space)
Output Format :
x^n (i.e. x raise to the power n)
Constraints :
1 <= x <= 30
0 <= n <= 30
'''




def power(x,n):

    if n==0:
        return 1

    smallOutput=power(x,n-1)
    return smallOutput*x

x,n=list(int(i) for i in input().strip().split(' '))
print(power(x,n))
