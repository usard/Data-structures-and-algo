# def postfix_prefix(s):
#     prefix=[]
#     for i in range(len(s)):
#         pass
#         if s[i].isalpha():
#             prefix.append(s[i])
#         else:
#             opnd2 = prefix.pop()
#             opnd1 = prefix.pop()
#             exp = s[i]+opnd1+opnd2
#             prefix.append(exp)
#     return ''.join(prefix)

def postfix_prefix(s):
    prefix = [] 
    for i in range(len(s)):
        if (isOperator(s[i])):
            opnd2 = prefix.pop()
            opnd1 = prefix.pop()
            exp = s[i]+opnd1+opnd2
            prefix.append(exp)
        else:
            prefix.append(s[i])
    return ''.join(prefix)


def isOperator(val):
    if val == '+':
        return True
    elif val == '-':
        return True
    elif val == '/':
        return True
    elif val == '*':
        return True
    else:
        return False
    



# print(postfix_prefix('ab+cd-*'))
# print(postfix_prefix('ABC/-AK/L-*'))