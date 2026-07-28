class Node:
    def __init__(self,value=None):
        self.data=value
        self.next=None
        self.prev=None
class DoublyLL:
    def __init__(self):
        self.head=None
    def insertAtEnd(self,value):
        temp=Node(value)
        if(self.head==None):
            self.head=temp
            return
        t=self.head
        while (t.next != None):
            t=t.next
        t.next=temp
        temp.prev=t
    def insertAtBeg(self,value):
        temp=Node(value)
        if(self.head==None):
            self.head=temp
            return
        temp.next=self.head
        self.head.prev=temp
        self.head=temp

    def printDLL(self):
        t1=self.head
        while(t1.next != None):
            print(t1.data,end=" <-->")
            t1=t1.next
        print(t1.data)

obj=DoublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtBeg(5)
obj.printDLL()

