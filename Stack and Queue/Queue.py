# #Implenting queue (Chai and code)
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


                              #Implementing Queue (Code and debug)
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items)==0

    def enqueue(self, item):
        self.items.append(item)


    
    def dequeue(self):
        if len(self.items) ==0:
            print("dequeue from empty queue")
            return
        x= self.items.pop(0)
        return x

    def front(self):
        if len(self.items) == 0:
            print("Cannot peek, queue is empty")
            return
        return self.items[0]

    def rear(self):
        if len(self.items) == 0:
            print("Cannot read, queue is empty")
            return
        return self.items[-1]

    def size(self):
        return len(self.items)

q = Queue()

q.enqueue(23)
q.enqueue(5)
q.enqueue(15)
q.enqueue(30)

print("Size:", q.size())
print("Front:", q.front())
print("Rear:", q.rear())

print("Dequeued:", q.dequeue())
print("Dequeued:", q.dequeue())

print("Front:", q.front())
print("Rear:", q.rear())

print("Is Empty:", q.is_empty())