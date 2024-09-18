def reverse_stack_recursion(s,r):
    if len(s) == 0:
        return r
    else:
        r.append(s.pop())
        return reverse_stack_recursion(s,r)


print(reverse_stack_recursion([1,2,3,4],[]))