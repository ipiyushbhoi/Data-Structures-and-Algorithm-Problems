'''

Given a string, compute recursively a new string where all appearances of "pi" have been replaced by "3.14".
Sample Input 1 :
xpix
Sample Output :
x3.14x
Sample Input 2 :
pipi
Sample Output :
3.143.14
Sample Input 3 :
pip
Sample Output :
3.14p


'''




def replace(s):

    if len(s)<2:
        return s
    for i in range(0,len(s)):
        if s[i:i+2]=='pi':
            return '3.14'+replace(s[i+2:])
    return s[0]+replace(s[1:])


n=str(input())
print(replace(n))
