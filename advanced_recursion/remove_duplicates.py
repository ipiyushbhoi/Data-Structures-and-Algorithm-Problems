'''

Given a string S, remove consecutive duplicates from it recursively.
Input Format :
String S
Output Format :
Output string
Constraints :
1 <= Length of String S <= 10^3
Sample Input :
aabccba
Sample Output :
abcba

'''




def removeDuplicates(s):
    
    if len(s)<=1:
        return s
    
    smallOutput=removeDuplicates(s[1:])
    
    if s[0]==s[1]:
        return smallOutput
    
    return s[0]+smallOutput
    
s=input('')
print(removeDuplicates(s))
