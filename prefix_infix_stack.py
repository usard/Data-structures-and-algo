def prefix_infix(s):
    infix=[]
    for i in range(len(s)-1,-1,-1):
        # print(s[i])
        if s[i].isalpha():
            infix.append(s[i])
        else:
            opnd1= infix.pop()
            opnd2 = infix.pop()
            exp  = '('+opnd1+s[i]+opnd2+')'
            # print(exp)
            infix.append(exp)
    return ''.join(infix)


        





# print(prefix_infix('-+d+*abc*ef'))'-+d+*abc*ef'
# print(prefix_infix('*+ab-cd'))
print(prefix_infix('-+d+*abc*ef'))