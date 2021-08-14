'''

Check if a given String S is palindrome or not (using recursion). Return true or false.
Input Format :
String S
Output Format :
true or false
Sample Input 1 :
racecar
Sample Output 1:
true
Sample Input 2 :
ninja
Sample Output 2:
false

'''


def sumofdigits(n):
    if n==0:
        return 0
    smallOutput=sumofdigits(n//10)
    return smallOutput+n%10
    
n=int(input())
print(sumofdigits(n))


























def palindrome(s):
    if(len(s)<1):
        print('true')
    else:
        if(s[0]==s[-1]):
            return(palindrome(s[1:-1]))
        else:
            print('false')
        
a=str(input(''))
palindrome(a)
