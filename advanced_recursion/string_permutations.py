'''

Given a string S, find and return all the possible permutations of the input string.
Note 1 : The order of permutations is not important.
Note 2 : If original string contains duplicate characters, permutations will also be duplicates.
Input Format :
String S
Output Format :
All permutations (in different lines)
Sample Input :
abc
Sample Output :
abc
acb
bac
bca
cab
cba

'''


 
def returnPermutations(s):
    l = []
    length = len(s)
    if length==1:
        return [s]
    for i in range(0, length):
        permutations = returnPermutations(s[0:i]+s[i+1:])
        for perm in permutations:
            l.append(s[i] + perm)
    return l

s = input()
permutations = returnPermutations(s)
print(*permutations, sep='\n')




    

