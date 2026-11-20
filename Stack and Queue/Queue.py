#                        #Implenting queue (Chai and code)
# class Queue:
#     def __init__(self):
#         self.items=[]
#     def isEmpty(self):
#         return len(self.items)== 0
#     def insert(self,value):
#         self.items.append(value)
#     def delete(self):
#         if(self.isEmpty()):
#             print("Queue is Empty")
#         else:
#             return self.items.pop(0)
# q=Queue()
# q.insert(10)
# q.insert(20)
# q.insert(30)
# print(q.delete())
# print(q.delete())
# print(q.delete())
# q.delete()


#                               #Implementing Queue (Code and debug)
# class Queue:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items)==0

#     def enqueue(self, item):
#         self.items.append(item)


    
#     def dequeue(self):
#         if len(self.items) ==0:
#             print("dequeue from empty queue")
#             return
#         x= self.items.pop(0)
#         return x

#     def front(self):
#         if len(self.items) == 0:
#             print("Cannot peek, queue is empty")
#             return
#         return self.items[0]

#     def rear(self):
#         if len(self.items) == 0:
#             print("Cannot read, queue is empty")
#             return
#         return self.items[-1]

#     def size(self):
#         return len(self.items)

# q = Queue()

# q.enqueue(23)
# q.enqueue(5)
# q.enqueue(15)
# q.enqueue(30)

# print("Size:", q.size())
# print("Front:", q.front())
# print("Rear:", q.rear())

# print("Dequeued:", q.dequeue())
# print("Dequeued:", q.dequeue())

# print("Front:", q.front())
# print("Rear:", q.rear())

# print("Is Empty:", q.is_empty())


# #Empty quese test cases
# q = Queue()

# print(q.is_empty())  # True
# print(q.size())      # 0

# print(q.dequeue())   # dequeue from empty queue
# print(q.front())     # Cannot peek, queue is empty
# print(q.rear())      # Should handle empty queue safely


#Implementing Queue using 2 stack
class StackQueue:
    def __init__(self):
        self.st1=[]
        self.st2=[]

    def push(self, x):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self):
            if not self.st1:
                print("Stack is empty")
                return -1  #Representing empty stack
            top_element=self.st1.pop()
            return top_element
        
    def top(self):
            if not self.st1:
                print("Stack is empty")
                return -1
            return self.st1[-1]

    def is_empty(self):
            return not self.st1

q=StackQueue()
q.push(10)
q.push(20)
q.push(30)
print(q.top())
print(q.pop())
print(q.pop())
q.push(7)
print(q.pop())

q = StackQueue()

q.push(100)
q.push(200)
q.push(300)

print(q.pop())  # 300

q.push(400)
q.push(500)

print(q.top())  # 500
print(q.pop())  # 500
print(q.pop())  # 400
print(q.pop())  # 200
print(q.pop())  # 100