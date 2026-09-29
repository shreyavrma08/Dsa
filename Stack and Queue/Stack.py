class stack:
    def __init__(self):
        self.s=[]
    def length(self):
        return len(self.s)
    def push(self,value):
        self.s.insert(0,value)
    def peek(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.s[0]
    def pop(self):
        if len(self.s)==0:
            raise Exception("Stack is empty")
        else:
            return self.pop(0)
stk=stack()
# stk.pop()#   raise Exception("Stack is empty")
stk.push(10)
stk.push(20)
stk.push(30)
print(stk.peek())