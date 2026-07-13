# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.next=Node
# node1= Node(5)

# node2= Node(10)
# node3= Node(7)
# node4= Node(8)

# node1.next = node2
# node2.next= node3
# node3.next= node4

# print(node1)
# print(node1.val)
# print(node1.next)
# print(node1.next.val)
# print(node2)
# print(node1.next.next.next.val)

# class Node:


#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
        
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node

#     def traverse(self):
#         if not self.head:
#             print("SLL is empty")
#         else:
#             current = self.head
#             while current is not None:
#                 print(current.val, end=" ")
#                 current = current.next
#             print()


# # Usage
# sll = SinglyLinkedList()
# sll.append(10)
# sll.append(20)
# sll.append(30)
# sll.append(40)
# sll.append(1)

# sll.traverse()

                                #Leetcode-876(for odd)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def middle(self):
#         n = 0
#         temp = self.head

#         while temp is not None:
#             n += 1
#             temp = temp.next

#         temp = self.head

#         for i in range(0, n // 2):
#             temp = temp.next

#         print(temp.val)


# # creating linked list
# l = LinkedList()

# l.head = Node(5)
# l.head.next = Node(10)
# l.head.next.next = Node(27)
# l.head.next.next.next = Node(3)
# l.head.next.next.next.next = Node(99)

# l.middle()
                                   #or  ( Tortoise-Hare Approach )

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def middle(self):
#         slow=self.head
#         fast=self.head
#         while fast is not None and fast.next is not None:
#             slow=slow.next
#             fast=fast.next.next
#         print(slow.val) 
    
# #creating linked list
# l = LinkedList()

# l.head = Node(5)
# l.head.next = Node(10)
# l.head.next.next = Node(27)
# l.head.next.next.next = Node(3)
# l.head.next.next.next.next = Node(99)
# l.head.next.next.next.next.next = Node(99)

# l.middle()
# #TC=O(n/2)
# #SC=O(1)

                          #Reverse of linkedlist 
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


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


                            #Optimal Solution Of reverse
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
    # def reverse(self):
    #     temp=self.head
    #     prev=None
#         while temp is not None:
#             front=temp.next
#             temp.next=prev
#             prev=temp
#             temp=front
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


                                 #LEETCODE :- 141 
#brute Tc=O(n) And Sc=O(n)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.prev=None
    def cycle(self):
        temp=self.head
        my_set=set()
        while temp is not None:
            if temp in my_set:
                print(True)
                return
            my_set.add(temp)
            temp=temp.next
        print(False)
#         
#creating linked list
l = LinkedList()

l.head = Node(5)
l.head.next = Node(9)
l.head.next.next = Node(1)
l.head.next.next.next = Node(7)
l.head.next.next.next.next = Node(6)
l.head.next.next.next.next.next = Node(1)
l.head.next.next.next.next.next.next = Node(9)
l.head.next.next.next.next.next.next.next = Node(2)
l.head.next.next.next.next.next.next.next.next= Node(8)
l.head.next.next.next.next.next.next.next.next.next=l.head.next.next
l.cycle()

#optimal Tc=O(n)  And Sc=O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.prev=None
    def cycle(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                print(True)
                return
        print(False)
#creating linked list
l = LinkedList()

l.head = Node(5)
l.head.next = Node(9)
l.head.next.next = Node(1)
l.head.next.next.next = Node(7)
l.head.next.next.next.next = Node(6)
l.head.next.next.next.next.next = Node(1)
l.head.next.next.next.next.next.next = Node(9)
l.head.next.next.next.next.next.next.next = Node(2)
l.head.next.next.next.next.next.next.next.next= Node(8)
l.head.next.next.next.next.next.next.next.next.next=l.head.next.next
l.cycle()

#                Leetcode-142
#Brute
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def cycle(self):
        temp=self.head
        my_set=set()
        while temp is not None:
            if temp in my_set:
                print(temp.val)
                return
            my_set.add(temp)
            temp=temp.next
        print(None)
#         
#creating linked list
l = LinkedList()

l.head = Node(5)
l.head.next = Node(9)
l.head.next.next = Node(1)
l.head.next.next.next = Node(7)
l.head.next.next.next.next = Node(6)
l.head.next.next.next.next.next = Node(1)
l.head.next.next.next.next.next.next = Node(9)
l.head.next.next.next.next.next.next.next = Node(2)
l.head.next.next.next.next.next.next.next.next= Node(8)
l.head.next.next.next.next.next.next.next.next.next=l.head.next.next
l.cycle()
#Optimal TC=O(n)   and SC=O(1)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.prev=None
    def cycle(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=self.head
                while slow != fast:
                    slow=slow.next
                    fast=fast.next
                print(slow.val)
                return
        print(None)
#creating linked list
l = LinkedList()

l.head = Node(5)
l.head.next = Node(9)
l.head.next.next = Node(1)
l.head.next.next.next = Node(7)
l.head.next.next.next.next = Node(6)
l.head.next.next.next.next.next = Node(1)
l.head.next.next.next.next.next.next = Node(9)
l.head.next.next.next.next.next.next.next = Node(2)
l.head.next.next.next.next.next.next.next.next= Node(8)
l.head.next.next.next.next.next.next.next.next.next=l.head.next.next
l.cycle()



ggddddd