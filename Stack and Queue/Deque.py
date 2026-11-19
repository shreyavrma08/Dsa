                           #Chai and code

class Deque:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)== 0
    
    def insertAtEnd(self,value):
        self.items.append(value)

    def deleteAtFront(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.items.pop(0)
        
    def insertAtFront(self,value):
        self.items.insert(0,value)

    def deleteAtEnd(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.items.pop()
        
dq= Deque()
dq.insertAtEnd(10)
dq.insertAtFront(20)
dq.insertAtEnd(30)
dq.insertAtEnd(40)
dq.insertAtFront(50)
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
print(dq.deleteAtFront())
print(dq.deleteAtFront())
print(dq.deleteAtEnd())
dq.deleteAtEnd()
dq.deleteAtFront()










                   #Code and debug

from collections import deque
lst=deque([])
lst.append(100)
lst.append(200)
lst.append(300)
print(lst)
lst.appendleft(1)#no appenedright operation
lst.appendleft(9)
print(lst)
print(lst[0])
print(lst[1])
lst.pop()
print(lst)
lst.popleft()#no popright operation
print(lst)