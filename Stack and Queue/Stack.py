#                              #Chai and code

# # push and pop in stack using insert()
# class stack:
#     def __init__(self):
#         self.s=[]
#     def length(self):
#         return len(self.s)
#     def push(self,value):
#         self.s.insert(0,value)
#     def peek(self):
#         if len(self.s) == 0:
#             raise Exception("Stack is Empty")
#         else:
#             return self.s[0]
#     def pop(self):
#         if len(self.s)==0:
#             raise Exception("Stack is empty")
#         else:
#             return self.s.pop(0)
# stk=stack()
# # stk.pop()#   raise Exception("Stack is empty")
# stk.push(10)
# stk.push(20)
# stk.push(30)
# print(stk.peek())
# print(stk.pop())
# print(stk.pop())
# print(stk.pop())


# # push and pop using appened()
# class stack:
#     def __init__(self):
#         self.s=[]
#     def length(self):
#         return len(self.s)
#     def push(self,value):
#         self.s.append(value)
#     def peek(self):
#         if len(self.s) == 0:
#             raise Exception("Stack is Empty")
#         else:
#             return self.s[0]
#     def pop(self):
#         if len(self.s)==0:
#             raise Exception("Stack is empty")
#         else:
#             return self.s.pop(0)
# stk=stack()
# # stk.pop()#   raise Exception("Stack is empty")
# stk.push(10)
# stk.push(20)
# stk.push(30)
# print(stk.peek())
# print(stk.pop())
# print(stk.pop())
# print(stk.pop())


# class Stack:
#     def __init__(self):
#         self.items=[]
#     def is_empty(self):
#         return len(self.items) == 0
#     def push(self,items):
#         self.items.append(items)
#     def pop(self):
#         if len(self.items) == 0:
#             return "Cannot pop,stack is empty"
#         x=self.items.pop()
#         return x
#     def top(self):
#         if len(self.items)==0:
#             return "Cannot top,stack is empty"
#         return self.items[-1]
#     def size(self):
#         return len(self.items)
# stack=Stack()
# stack.push(5)
# stack.push(10)
# stack.push(15)
# print(f"Stack content ={stack}")
# print(f"Popped item ={stack.pop()}")
# print(f"Stack content={stack}")
# print(f"Top item after pop={stack.top()}")
# print(f"Stack is empty = {stack.is_empty()}")










                            #code and debug
#Implementing stack using queue
from collections import deque
class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def push(self,item):
        self.queue.append(item)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    
    def pop(self):
        if len(self.queue)==0:
            return "Stack is empty"
        return self.queue.popleft()

    def top(self):
        if len(self.queue)==0:
            return "Stack is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue)==0

    def size(self):
        return len(self.queue)
    
stk=StackUsingQueue()
stk.push(100)
stk.push(200)
stk.push(300)
stk.push(400)

print(stk.top())
print(stk.pop())
print(stk.pop())
print(stk.top())
stk.push(5)
print(stk.top())
print(stk.pop())
