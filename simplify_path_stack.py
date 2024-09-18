def simplifyPath(path):
        stack=[]
        for i in range(len(path)):
            if path[i] == '/' and len(stack):
                text = ''
                while stack and stack[-1]!='/':
                    text = stack.pop()+text
                if text == '':
                    pass
                elif text == '..':
                    stack.pop()
                    stack and stack.pop()
                    stack.append('/')
                elif text == '.':
                    stack.pop()
                else:
                    stack and stack.pop()
                    text ='/'+text
                    stack.append(text)
                    stack.append('/')
            else:
                # stack and stack[-1] == '/' and stack.pop()
                stack.append(path[i])
        if len(stack) > 1 and stack[-1] == '/':
           stack.pop()
        return ''.join(stack)

print(simplifyPath('/a/../../b/../c//.//'))