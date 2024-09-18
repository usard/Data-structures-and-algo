matcher = {
     '(':')' ,
     '{' : '}',
     '[' : ']',
     ')':'(',
     '}':'{',
     ']':'['
}

# def isValid( s: str) -> bool:
#         stack=[]
#         for i in range(len(s)):
#             if len(stack) == 0:
#                 stack.append(s[i])
#             else:
#                 print(stack[-1], s[i])
#                 if stack[-1] == s[i]:
#                     print(' ia mahere')
#                     stack.pop()
#                 else:
#                     return False
#         return True    

def isValid(s):
    stack = []
    for i in range(0,len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if matcher[s[i]] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])

    if len(stack)>0:
        return False
    else:
        return True



# print(isValid('[{()}]'))
print(isValid('[]{]'))