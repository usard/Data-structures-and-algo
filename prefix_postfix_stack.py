from postfix_prefix_stack import isOperator
# def isOperator(val):
#     if val == '+':
#         return True
#     elif val == '-':
#         return True
#     elif val == '/':
#         return True
#     elif val == '*':
#         return True
#     else:
#         return False
    

def prefix_postfix(s):
    postfix = []
    for i in range(len(s)-1,-1,-1):
        if isOperator(s[i]):
            opnd1 = postfix.pop()
            opnd2 = postfix.pop()
            exp = opnd1+opnd2+s[i]
            # print(exp)
            postfix.append(exp)
        else:
            postfix.append(s[i])
        
    return ''.join(postfix)

print(prefix_postfix('*+ab-cd'))
