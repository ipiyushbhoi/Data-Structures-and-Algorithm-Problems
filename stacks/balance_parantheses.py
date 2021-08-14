
def checkBalanced(expr):
    
    stack=[]
    
    for i in expr:
        if i=='(' or i=='{' or i=='[':
            stack.append(i)
        elif i==')':
            if len(stack)!=0 and i!='(':
                stack.pop()
            else:
                return False
        elif i==']':
            if len(stack)!=0 and i!='[':
                stack.pop()
            else:
                return False
        elif i=='}':
            if len(stack)!=0 and i!='{':
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    return False            
            
### Implement your code here

exp=input()
if checkBalanced(exp):
    print('true')
else:
    print('false')

