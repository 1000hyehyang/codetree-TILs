class Stack:
    def __init__(self):
        self.top_ = -1
        self.arr = []
    
    def isEmpty(self):
        return self.top_ == -1

    def push(self, e):
        self.top_ += 1
        self.arr.append(e)
    
    def pop(self):
        data = self.arr[self.top_]
        del self.arr[self.top_]
        self.top_ -= 1
        return data
    
    def size(self):
        print(self.top_ + 1)
    
    def top(self):
        print(self.arr[self.top_])

stack = Stack()

st = input()
em = 0

for i in st:
    if i == '(':
        stack.push(i)
    elif i == ')':
        if stack.isEmpty():
            em = 1
            break
        stack.pop()

if em != 1 and stack.isEmpty():
    print('Yes')
elif em == 1:
    print('No')
else:
    print('No')