'''

Given an integer n, using phone keypad find out all the possible strings that can be made using digits of input n.
Return empty string for numbers 0 and 1.
Note : The order of strings are not important.
Input Format :
Integer n
Output Format :
All possible strings in different lines
Constraints :
1 <= n <= 10^6
Sample Input:
23
Sample Output:
ad
ae
af
bd
be
bf
cd
ce
cf

'''





def keypad(num):
    options = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    if (num==0):
        lst = [""]
        return lst

    small = num//10
    remainder = num%10
    lst = keypad(small)

    optionslen = len(options[remainder])
    lstlen = len(lst)
    lst *= optionslen
    k=0
    for i in range(0, optionslen):
        for j in range(0, lstlen):
            lst[k] = lst[k] + options[remainder][i]
            k += 1
    return lst

n=int(input())
l=keypad(n)
for i in l:
    print(i)

    

