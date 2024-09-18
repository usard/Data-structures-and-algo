def check_precedence(a):
    if a == '(':
        return 5
    elif a == ')':
        return 5
    elif a == '/':
        return 4
    elif a == '*':
        return 3
    elif a == '+':
        return 2
    elif a == '-':
        return 1
    else :
        return 0
    
    

def infix_postfix_stack(s):
    p=[]
    r=[]
    for i in range(0,len(s)):
        if s[i].isalpha():
            p.append(s[i])
        else:
            if s[i] == '(':
                r.append(s[i])
            elif s[i] == ')':
                while r and r[-1] != '(':
                    p.append(r.pop())
                if r and r[-1] == '(' :
                    r.pop()
            else:
                check = check_precedence(s[i])
                if len(r) == 0 or check > check_precedence(r[-1]):
                    r.append(s[i])
                else:
                    if r[-1]  == '(':
                        r.append(s[i])
                    else:
                        while check < check_precedence(r[-1]) and r[-1] != '(':
                            p.append(r.pop())
                        r.append(s[i])     
    while len(r):
        p.append(r.pop())
    
    return p

            
print(''.join(infix_postfix_stack('(d+(a*b+c)-e*f)')))