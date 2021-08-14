'''
bool checkRedundantBrackets(char *input) {
	stack<char> s;

	bool flag = false;
	for(int i = 0; i < strlen(input); i++) {
		if(input[i] != ')') {
			s.push(input[i]);
		}
		else {
			while(s.top() != '(') {
				s.pop();
				flag = true;
				if(s.empty()) {
					break;
				}
			}
			if(s.empty()) {
				continue;
			}
			if(flag) {
				s.pop();
				flag = false;
			}
			else {
				return true;
			}
		}
	}
	return false;
}
'''

def checkredundant(s):
    
    stack=[]
    
    for i in s:
        if i!=')':
            stack.append(i)
        else:
            if stack[0]=='(':
                print('have')
                return 
            while stack[0]!='(':
                stack.pop(0)
            stack.pop(0)

    return 'doesnt have'
            

exp=input()
checkredundant(exp)

