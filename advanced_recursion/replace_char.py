'''

Given an input string S and two characters c1 and c2, you need to replace every occurrence of character c1 with character c2 in the given string.
Do this recursively.
Input Format :
Line 1 : Input String S
Line 2 : Character c1 and c2 (separated by space)
Output Format :
Updated string
Constraints :
1 <= Length of String S <= 10^6
Sample Input :
abacd
a x
Sample Output :
xbxcd

'''




def replaceChar(s,c1,c2):
    
    if len(s)==0:
        return s
    
    smallOutput=replaceChar(s[1:],c1,c2)
    
    if s[0]==c1:
        return c2+smallOutput
    
    return s[0]+smallOutput
    
s=input('')
c1,c2=input().split()
print(replaceChar(s,c1,c2))
