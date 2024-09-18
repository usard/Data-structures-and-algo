def postfix_infix(s):
    infix=[]
    for i in range(len(s)):
        if s[i].isalpha():
            infix.append(s[i])
        else:
            opnd2 = infix.pop()
            opnd1 = infix.pop()
            exp = '('+opnd1+s[i]+opnd2+')'
            infix.append(exp)
    return ''.join(infix)




print(postfix_infix('dab*c++ef*-'))