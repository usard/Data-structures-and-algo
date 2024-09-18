from collections import deque

class Pack: 
    def __init__ (self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def size(self):
        return len(self.container)
    
    def is_empty(self):
        return len(self.container) == 0
    
stack = Pack()

stack.push('a')
stack.push('b')
stack.push('c')

print(stack.container)
