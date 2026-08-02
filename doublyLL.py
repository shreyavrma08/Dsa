# #Insertion at the End of DoublyLL
# class Node:
#     def __init__(self,value=None):
#         self.data=value
#         self.next=None
#         self.prev=None
# class DoublyLL:
#     def __init__(self):
#         self.head=None
#     def insertAtEnd(self,value):
#         temp=Node(value)
#         if(self.head==None):
#             self.head=temp
#             return
#         t=self.head
#         while (t.next != None):
#             t=t.next
#         t.next=temp
#         temp.prev=t


#     def printDLL(self):
#         t1=self.head
#         while(t1.next != None):
#             print(t1.data,end=" <-->")
#             t1=t1.next
#         print(t1.data)

# obj=DoublyLL()
# obj.insertAtEnd(10)
# obj.insertAtEnd(20)
# obj.insertAtEnd(30)
# obj.insertAtEnd(40)
# # obj.insertAtBeg(5)
# obj.printDLL()


# #Insertion at the Beg of DoublyLL
# class Node:
#     def __init__(self,value=None):
#         self.data=value
#         self.next=None
#         self.prev=None
# class DoublyLL:
#     def __init__(self):
#         self.head=None
#     def insertAtEnd(self,value):
#         temp=Node(value)
#         if(self.head==None):
#             self.head=temp
#             return
#         t=self.head
#         while (t.next != None):
#             t=t.next
#         t.next=temp
#         temp.prev=t
#     def insertAtBeg(self,value):
#         temp=Node(value)
#         if(self.head==None):
#             self.head=temp
#             return
#         temp.next=self.head
#         self.head.prev=temp
#         self.head=temp

#     def printDLL(self):
#         t1=self.head
#         while(t1.next != None):
#             print(t1.data,end=" <-->")
#             t1=t1.next
#         print(t1.data)

# obj=DoublyLL()
# obj.insertAtEnd(10)
# obj.insertAtEnd(20)
# obj.insertAtEnd(30)
# obj.insertAtEnd(40)
# obj.insertAtBeg(5)
# obj.printDLL()


# #Insert at Mid
# class Node:
#     def __init__(self,value=None):
#         self.data=value
#         self.next=None
#         self.prev=None
# class DoublyLL:
#     def __init__(self):
#         self.head=None
#     def insertAtEnd(self,value):
#         temp=Node(value)
#         if(self.head==None):
#             self.head=temp
#             return
#         t=self.head
#         while (t.next != None):
#             t=t.next
#         t.next=temp
#         temp.prev=t
#     def insertAtBeg(self,value):
#         temp=Node(value)
#         if(self.head==None):
#             self.head=temp
#             return
#         temp.next=self.head
#         self.head.prev=temp
#         self.head=temp
#     def insertAtMid(self,value,x):
#         t=self.head
#         while(t.next!=None):
#             if(t.data==x):
#                 break
#             else:
#                 t=t.next
#         temp=Node(value)
#         temp.next=t.next
#         t.next.prev=temp
#         t.next=temp
#         temp.prev=t

#     def printDLL(self):
#         t1=self.head
#         while(t1.next != None):
#             print(t1.data,end=" <-->")
#             t1=t1.next
#         print(t1.data)

# obj=DoublyLL()
# obj.insertAtEnd(10)
# obj.insertAtEnd(20)
# obj.insertAtEnd(30)
# obj.insertAtEnd(40)
# obj.insertAtBeg(5)
# obj.insertAtMid(50,20)
# obj.printDLL()


# #DEletion in doubly linked list

# class Node:
#     def __init__(self,value=None):
#         self.data=value
#         self.next=None
#         self.prev=None
# class DoublyLL:
#     def __init__(self):
#         self.head=None
#     def insertAtEnd(self,value):
#         temp=Node(value)
#         if(self.head==None):
#             self.head=temp
#             return
#         t=self.head
#         while (t.next != None):
#             t=t.next
#         t.next=temp
#         temp.prev=t
#     def insertAtBeg(self,value):
#         temp=Node(value)
#         if(self.head==None):
#             self.head=temp
#             return
#         temp.next=self.head
#         self.head.prev=temp
#         self.head=temp
#     def insertAtMid(self,value,x):
#         t=self.head
#         while(t.next!=None):
#             if(t.data==x):
#                 break
#             else:
#                 t=t.next
#         temp=Node(value)
#         temp.next=t.next
#         t.next.prev=temp
#         t.next=temp
#         temp.prev=t

#     def printDLL(self):
#         t1=self.head
#         while(t1.next != None):
#             print(t1.data,end=" <-->")
#             t1=t1.next
#         print(t1.data)

#     def deletion(self,value):
#             if (self.head == None):
#                 print("LL is empty")
#                 return
#             t=self.head
#             if(t.data == value):
#                 self.head = t.next
#                 self.head.prevt=None
#                 return
#             while(t.next != None):
#                 if(t.data == value):
#                     t.prev.next = t.next
#                     t.next.prev = t.next
#                     return
#                 else:
#                     t=t.next
#             if (t.data == value):
#                     t.prev.next = None



# obj=DoublyLL()
# obj.insertAtEnd(10)
# obj.insertAtEnd(20)
# obj.insertAtEnd(30)
# obj.insertAtEnd(40)
# obj.insertAtBeg(5)
# obj.insertAtMid(50,20)
# obj.deletion(5)
# obj.deletion(50)
# obj.deletion(40)
# obj.printDLL()

# #Reverse of a doublyLL


#                           #Reverse of linkedlist 
# #TC=O(2n)=O(2n)         SC=O(n)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev=None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def reverse(self):
#         temp=self.head
#         stack=[]
#         while temp is not None:
#             stack.append(temp.val)
#             temp=temp.next
#         temp=self.head
#         while temp is not None:
#                 temp.val=stack.pop()
                
#                 temp=temp.next
#     def display(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.val, end="->")
#             temp = temp.next
             
#         print("None")
    
# #creating linked list
# l = LinkedList()

# l.head = Node(5)
# l.head.next = Node(8)
# l.head.next.next = Node(7)
# l.head.next.next.next = Node(3)
# l.head.next.next.next.next = Node(2)
# print("Original Linked List:")
# l.display()

# l.reverse()

# print("Reversed Linked List:")
# l.display()


#  #                           Optimal Solution Of reverse
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def reverse(self):
#         curr=self.head
#         prev=None
#         while curr is not None:
#             front=curr.next
#             curr.next=prev
#             curr.prev=front
#             prev=curr
#             curr=front
#         self.head=prev
#     def display(self):
#         temp = self.head

#         while temp is not None:
#             print(temp.val, end=" -> ")
#             temp = temp.next

#         print("None")
# #creating linked list
# l = LinkedList()

# l.head = Node(5)
# l.head.next = Node(8)
# l.head.next.next = Node(7)
# l.head.next.next.next = Node(3)
# l.head.next.next.next.next = Node(2)
# print("Original Linked List:")
# l.display()

# l.reverse()

# print("Reversed Linked List:")
# l.display()


# #Deleting All Ocurence of a key in DoublyLL
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None


# class LinkedList:

#     def __init__(self):
#         self.head = None

#     def insert_at_end(self, val):
#         new_node = Node(val)

#         if self.head is None:
#             self.head = new_node
#             return

#         temp = self.head

#         while temp.next is not None:
#             temp = temp.next

#         temp.next = new_node
#         new_node.prev = temp

#     def delete_occurrence(self, k):
#         temp = self.head

#         while temp is not None:

#             if temp.val == k:

#                 # If deleting head
#                 if temp == self.head:
#                     self.head = temp.next

#                     if self.head is not None:
#                         self.head.prev = None

#                 else:
#                     # Connect previous node to next node
#                     temp.prev.next = temp.next

#                     # Connect next node to previous node
#                     if temp.next is not None:
#                         temp.next.prev = temp.prev

#             temp = temp.next

#     def display(self):
#         temp = self.head

#         while temp is not None:
#             print(temp.val, end=" <-> ")
#             temp = temp.next

#         print("None")


# # Creating linked list
# l = LinkedList()

# l.insert_at_end(5)
# l.insert_at_end(2)
# l.insert_at_end(3)
# l.insert_at_end(2)
# l.insert_at_end(10)

# print("Original:")
# l.display()

# l.delete_occurrence(2)

# print("After deleting 2:")
# l.display()

#Find pairs with given sum in DoublyLL
#Brute :  TC=O(n^2)   SC=O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
    def find_pairs(self, target):
        temp1=self.head
        result=[]
        while temp1 is not None:
           temp2=temp1.next
           while temp2 is not None:
                if temp1.val + temp2.val == target:
                    result.append([temp1.val,temp2.val])
                temp2=temp2.next
           temp1=temp1.next
        print(result)
#Creating linked list
l = LinkedList()
l.head = Node(1)
l.head.next = Node(2)
l.head.next.next = Node(3)
l.head.next.next.next = Node(4)
l.head.next.next.next.next = Node(5)
l.head.next.next.next.next.next = Node(6)
l.head.next.next.next.next.next.next = Node(8)
l.head.next.next.next.next.next.next.next = Node(9)
l.find_pairs(7)

#Better :  TC=O(n^2)   SC=O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
    def find_pairs(self, target):
        my_set=set()
        temp=self.head
        result=[]
        while temp is not None:
            remaining=target-temp.val
  
            if remaining in my_set:
                    result.append([remaining,temp.val])
            my_set.add(temp.val)
            temp=temp.next   
        print(result)
#Creating linked list
l = LinkedList()
l.head = Node(1)
l.head.next = Node(2)
l.head.next.next = Node(4)
l.head.next.next.next = Node(5)
l.head.next.next.next.next = Node(6)
l.head.next.next.next.next.next = Node(8)
l.head.next.next.next.next.next.next = Node(9)

l.find_pairs(7)

#Optimal :  TC=O(n^2)   SC=O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def find_pairs(self, target):
        left = self.head
        right = self.head
        result = []

        while right.next is not None:
            right = right.next

        while left is not None and right is not None and left.val < right.val:
            total = left.val + right.val

            if total == target:
                result.append([left.val, right.val])
                left = left.next
                right = right.prev

            elif total > target:
                right = right.prev

            else:
                left = left.next

        print(result)


# Creating linked list
l = LinkedList()

l.head = Node(1)

l.head.next = Node(2)
l.head.next.prev = l.head

l.head.next.next = Node(3)
l.head.next.next.prev = l.head.next

l.head.next.next.next = Node(4)
l.head.next.next.next.prev = l.head.next.next

l.head.next.next.next.next = Node(5)
l.head.next.next.next.next.prev = l.head.next.next.next

l.head.next.next.next.next.next = Node(6)
l.head.next.next.next.next.next.prev = l.head.next.next.next.next

l.head.next.next.next.next.next.next = Node(8)
l.head.next.next.next.next.next.next.prev = l.head.next.next.next.next.next

l.head.next.next.next.next.next.next.next = Node(9)
l.head.next.next.next.next.next.next.next.prev = l.head.next.next.next.next.next.next

l.find_pairs(7)

# #Creating linked list
# l = LinkedList()
# l.head = Node(1)
# l.head.next = Node(2)
# l.head.next.next = Node(3)
# l.head.next.next.next = Node(4)
# l.head.next.next.next.next = Node(5)
# l.head.next.next.next.next.next = Node(6)
# l.head.next.next.next.next.next.next = Node(8)
# l.head.next.next.next.next.next.next.next = Node(9)
# l.find_pairs(7)

