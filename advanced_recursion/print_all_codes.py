'''

Assume that the value of a = 1, b = 2, c = 3, ... , z = 26. You are given a numeric string S. Write a program to print the list of all possible codes that can be generated from the given string.
Note : The order of codes are not important. Just print them in different lines.
Input format :
A numeric string S
Output Format :
All possible codes in different lines
Constraints :
1 <= Length of String S <= 10
Sample Input:
1123
Sample Output:
aabc
kbc
alc
aaw
kw

'''




m = {"0":"", "1":"a", "2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h",
     "9":"i", "10":"j","11":"k","12":"l","13":"m","14":"n","15":"o","16":"p",
     "17":"q", "18":"r","19":"s","20":"t","21":"u","22":"v","23":"w",
     "24":"x","25":"y","26":"z"}

def printCodes(string, output):
    length = len(string)
    if length==0:
        #print(output)
        return
    if length==1:
        print(output, m[string], sep='')
        return
    elif string in m:
        print(output, m[string], sep='')

    # Print possiblities after removing 1 character
    printCodes(string[1:], output+m[string[0]])

    # Print possiblities after removing 2 character
    if string[0:2] in m:
        printCodes(string[2:], output+m[string[0:2]])

def printCodesMain(string):
    printCodes(string, '')

# Main
string=input()
printCodesMain(string)

    

