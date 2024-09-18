def infix_prefix(s):
    p=[]
    o=[]
    for i in range(len(s)-1,-1,-1):
        print(s[i])
        if s[i].isalpha():
            p.append(s[i])
        else:
          if s[i] == '(':
              exp = o.pop()+p.pop()+p.pop()
              o.pop()
              p.append(exp)
          else:
            o.append(s[i])
    return ''.join(p)       

# print(infix_prefix('((a+b)*(c-d))')) #*+ab-cd
# print(infix_prefix('(d+(a*b+c)-e*f)')) # fec+d*ab
# print(infix_prefix('((d+((a*b)+c))-(e*f))')) # -+d+*abc*ef