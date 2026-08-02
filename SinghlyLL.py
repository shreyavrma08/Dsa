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


#                                  #LEETCODE :- 141 
# #brute Tc=O(n) And Sc=O(n)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.prev=None
#     def cycle(self):
#         temp=self.head
#         my_set=set()
#         while temp is not None:
#             if temp in my_set:
#                 print(True)
#                 return
#             my_set.add(temp)
#             temp=temp.next
#         print(False)
# #         
# #creating linked list
# l = LinkedList()

# l.head = Node(5)
# l.head.next = Node(9)
# l.head.next.next = Node(1)
# l.head.next.next.next = Node(7)
# l.head.next.next.next.next = Node(6)
# l.head.next.next.next.next.next = Node(1)
# l.head.next.next.next.next.next.next = Node(9)
# l.head.next.next.next.next.next.next.next = Node(2)
# l.head.next.next.next.next.next.next.next.next= Node(8)
# l.head.next.next.next.next.next.next.next.next.next=l.head.next.next
# l.cycle()

# #optimal Tc=O(n)  And Sc=O(1)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.prev=None
#     def cycle(self):
#         slow=self.head
#         fast=self.head
#         while fast is not None and fast.next is not None:
#             slow=slow.next
#             fast=fast.next.next
#             if slow==fast:
#                 print(True)
#                 return
#         print(False)
# #creating linked list
# l = LinkedList()

# l.head = Node(5)
# l.head.next = Node(9)
# l.head.next.next = Node(1)
# l.head.next.next.next = Node(7)
# l.head.next.next.next.next = Node(6)
# l.head.next.next.next.next.next = Node(1)
# l.head.next.next.next.next.next.next = Node(9)
# l.head.next.next.next.next.next.next.next = Node(2)
# l.head.next.next.next.next.next.next.next.next= Node(8)
# l.head.next.next.next.next.next.next.next.next.next=l.head.next.next
# l.cycle()

# #                Leetcode-142
# #Brute
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
        
#     def cycle(self):
#         temp=self.head
#         my_set=set()
#         while temp is not None:
#             if temp in my_set:
#                 print(temp.val)
#                 return
#             my_set.add(temp)
#             temp=temp.next
#         print(None)
# #         
# #creating linked list
# l = LinkedList()

# l.head = Node(5)
# l.head.next = Node(9)
# l.head.next.next = Node(1)
# l.head.next.next.next = Node(7)
# l.head.next.next.next.next = Node(6)
# l.head.next.next.next.next.next = Node(1)
# l.head.next.next.next.next.next.next = Node(9)
# l.head.next.next.next.next.next.next.next = Node(2)
# l.head.next.next.next.next.next.next.next.next= Node(8)
# l.head.next.next.next.next.next.next.next.next.next=l.head.next.next
# l.cycle()
# #Optimal TC=O(n)   and SC=O(1)
 
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.prev=None
#     def cycle(self):
#         slow=self.head
#         fast=self.head
#         while fast is not None and fast.next is not None:
#             slow=slow.next
#             fast=fast.next.next
#             if slow==fast:
#                 slow=self.head
#                 while slow != fast:
#                     slow=slow.next
#                     fast=fast.next
#                 print(slow.val)
#                 return
#         print(None)
# #creating linked list
# l = LinkedList()

# l.head = Node(5)
# l.head.next = Node(9)
# l.head.next.next = Node(1)
# l.head.next.next.next = Node(7)
# l.head.next.next.next.next = Node(6)
# l.head.next.next.next.next.next = Node(1)
# l.head.next.next.next.next.next.next = Node(9)
# l.head.next.next.next.next.next.next.next = Node(2)
# l.head.next.next.next.next.next.next.next.next= Node(8)
# l.head.next.next.next.next.next.next.next.next.next=l.head.next.next
# l.cycle()


#                           #Length of Loop in Linkedlist/ Floyd Cycle Detection

# #Brute TC=O(n)      SC=O(n)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.prev=None
#     def cycle(self):
#         temp=self.head
#         travel=0
#         my_dict=dict()
#         while temp is not None:
#             if temp in my_dict:
#                 print(travel-my_dict[temp])
#                 return
#             my_dict[temp]=travel
#             travel+=1
#             temp=temp.next
#         print(None)


# #creating linked list
# l = LinkedList()

# l.head = Node(5)
# l.head.next = Node(9)
# l.head.next.next = Node(1)
# l.head.next.next.next = Node(7)
# l.head.next.next.next.next = Node(6)
# l.head.next.next.next.next.next = Node(1)
# l.head.next.next.next.next.next.next = Node(9)
# l.head.next.next.next.next.next.next.next = Node(2)
# l.head.next.next.next.next.next.next.next.next= Node(8)
# l.head.next.next.next.next.next.next.next.next.next=l.head.next.next
# l.cycle()


#        #Optimal  TC= O(n)   and sc=O(1)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def cycle(self):
#         slow = self.head
#         fast = self.head

#         while fast is not None and fast.next is not None:
#             slow = slow.next
#             fast = fast.next.next

#             if slow == fast:
#                 count = 1          # Initialize count

#                 slow = slow.next

#                 while slow != fast:
#                     slow = slow.next
#                     count += 1

#                 print(count)
#                 return

#         print("No Cycle")


# # Creating linked list
# l = LinkedList()

# l.head = Node(5)
# l.head.next = Node(9)
# l.head.next.next = Node(1)
# l.head.next.next.next = Node(7)
# l.head.next.next.next.next = Node(6)
# l.head.next.next.next.next.next = Node(1)
# l.head.next.next.next.next.next.next = Node(9)
# l.head.next.next.next.next.next.next.next = Node(2)
# l.head.next.next.next.next.next.next.next.next = Node(8)

# # Create cycle
# l.head.next.next.next.next.next.next.next.next.next = l.head.next.next

# l.cycle()


                              ##Leetcode=328
#           # Brute TC=O(n)      Sc=o(n)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print_odd_even(self):
#         if self.head is None or self.head.next is None:
#             return

#         values = []

#         # Store even index nodes (0,2,4...)
#         temp = self.head
#         while temp:
#             values.append(temp.val)
#             temp = temp.next
#             if temp:
#                 temp = temp.next

#         # Store odd index nodes (1,3,5...)
#         temp = self.head.next
#         while temp:
#             values.append(temp.val)
#             temp = temp.next
#             if temp:
#                 temp = temp.next

#         # Replace values
#         temp = self.head
#         index = 0

#         while temp:
#             temp.val = values[index]
#             index += 1
#             temp = temp.next

#         # Print
#         temp = self.head
#         while temp:
#             print(temp.val, end=" ")
#             temp = temp.next



# # Creating linked list
# l = LinkedList()

# l.head = Node(8)
# l.head.next = Node(7)
# l.head.next.next = Node(1)
# l.head.next.next.next = Node(5)
# l.head.next.next.next.next = Node(6)
# l.head.next.next.next.next.next = Node(4)
# l.head.next.next.next.next.next.next = Node(9)
# l.print_odd_even()


# #   Optimal TC=O(n)   SC=O(n)

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def oddEven(self):
#         if self.head is None or self.head.next is None:
#             return

#         odd = self.head
#         even = self.head.next
#         even_head = even

#         while even is not None and even.next is not None:
#             odd.next = odd.next.next
#             odd = odd.next

#             even.next = even.next.next
#             even = even.next

#         odd.next = even_head

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.val, end=" ")
#             temp = temp.next
#         print()


# # Creating linked list
# l = LinkedList()

# l.head = Node(8)
# l.head.next = Node(7)
# l.head.next.next = Node(1)
# l.head.next.next.next = Node(5)
# l.head.next.next.next.next = Node(6)
# l.head.next.next.next.next.next = Node(4)
# l.head.next.next.next.next.next.next = Node(9)

# l.oddEven()
# l.display()

                      #Leetcode=19 
    #Brute TC=O(2N)=O(n)       SC= O(1)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def remove_nth_node(self,n):
#         length=0
#         temp=self.head
#         while temp is not None:
#             length+=1
#             temp=temp.next

#         if length==n:
#             new_head=self.head.next
            
#             print(new_head)
#         position_to_stop=length-n
#         temp=self.head
#         count=1
#         while count<position_to_stop:
#             temp=temp.next
#             count+=1
#         temp.next=temp.next.next
#         #to print complete linkedlist
#     def display(self):
#             temp = self.head
#             while temp:
#                 print(temp.val, end=" ")
#                 temp = temp.next
#             print()   
# l = LinkedList()

# l.head = Node(1)
# l.head.next = Node(3)
# l.head.next.next = Node(4)
# l.head.next.next.next = Node(7)
# l.head.next.next.next.next = Node(1)
# l.head.next.next.next.next.next = Node(2)
# l.head.next.next.next.next.next.next = Node(6)
# print("Original:")
# l.display()

# l.remove_nth_node(2)

# print("After deletion:")
# l.display()

# #Optimal tc=O(N)  Sc=O(1)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def remove_nth_node(self,n):
#         slow=self.head
#         fast=self.head
#         # Move fast n steps ahead
#         for _ in range(n):
#             fast=fast.next
#              # Remove head
#         if fast==None:
#                 return self.head.next
#         # Move both pointers
#         while fast.next is not None:
#                 slow=slow.next
#                 fast=fast.next
#               # Delete nth node from end   
#         slow.next=slow.next.next
#         return self.head
        
            
#         #to print complete linkedlist
#     def display(self):
#             temp = self.head
#             while temp:
#                 print(temp.val, end=" ")
#                 temp = temp.next
#             print()   
# l = LinkedList()

# l.head = Node(1)
# l.head.next = Node(3)
# l.head.next.next = Node(4)
# l.head.next.next.next = Node(7)
# l.head.next.next.next.next = Node(1)
# l.head.next.next.next.next.next = Node(2)
# l.head.next.next.next.next.next.next = Node(6)
# print("Original:")
# l.display()

# l.remove_nth_node(2)

# print("After deletion:")
# l.display()


#Palindrome or not
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def palindrome(self):
#         temp=self.head
#         stack=[]
#         while temp!=None:
#             stack.append(temp.val)
#             temp=temp.next
#         temp = self.head
#         while temp!=None:
#             if temp.val != stack.pop():
#                 print("Not Palindrome")
#                 return
#             temp=temp.next
        
#         print("palindrome")
# l = LinkedList()

# l.head = Node(1)
# l.head.next = Node(3)
# l.head.next.next = Node(4)
# l.head.next.next.next = Node(3)
# l.head.next.next.next.next = Node(2)
# # l.head.next.next.next.next.next = Node(1)
# # l.head.next.next.next.next.next.next = Node(6)
# l.palindrome()




    
# 

    
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isPalindrome(self):
        slow = self.head
        fast = self.head

        # Find middle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        temp = slow

        while temp is not None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        # Compare
        first = self.head
        second = prev

        while second is not None:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True


l = LinkedList()

l.head = Node(1)
l.head.next = Node(3)
l.head.next.next = Node(4)
l.head.next.next.next = Node(3)
l.head.next.next.next.next = Node(1)


if l.isPalindrome():
    print("Palindrome")
else:
    print("Not Palindrome")