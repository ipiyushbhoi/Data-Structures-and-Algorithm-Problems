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
