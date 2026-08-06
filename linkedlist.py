#Leetcode 2095
#optimal solution   TC=O(n+m)  Sc=O(1)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def deleteMid(self, head):
#         if head == None and head.next==None:
#             return None
        
#         n=0
#         temp=head
#         while temp!=None:
#             n+=1
#             temp=temp.next
#         result=n//2   
#         temp=head
#         while temp != None:
#             result-=1
#             if result ==0:
#                 middle=temp.next
#                 temp.next=temp.next.next
#                 break
#             temp=temp.next
#         return head
# l = LinkedList()

# l.head = Node(1)
# l.head.next = Node(2)
# l.head.next.next = Node(4)
# l.head.next.next.next = Node(5)
# l.head.next.next.next.next = Node(2)
# # Delete middle node

# result = l.deleteMid(l.head)


# # Print linked list

# temp = result

# while temp is not None:
#     print(temp.val, end=" -> ")
#     temp = temp.next

# print("None")


#Optimal  Time Complexity  = O(N)  and Space Complexity = O(1)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def deleteMid(self, head):

#         # Empty list or single node
#         if head is None or head.next is None:
#             return None

#         slow = head
#         fast = head
#         prev = None

#         while fast is not None and fast.next is not None:

#             prev = slow
#             slow = slow.next
#             fast = fast.next.next

#         # Delete middle node
#         prev.next = slow.next

#         return head


# # Create linked list

# l = LinkedList()

# l.head = Node(1)
# l.head.next = Node(2)
# l.head.next.next = Node(4)
# l.head.next.next.next = Node(5)
# l.head.next.next.next.next = Node(2)


# # Delete middle node

# result = l.deleteMid(l.head)


# # Print linked list

# temp = result

# while temp is not None:
#     print(temp.val, end=" -> ")
#     temp = temp.next

# print("None")


           #Leetcode:83
#TC=O(n)   SC=O(1)

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def removeDoublicate(self, head):
#         temp = head

#         while temp != None and temp.next != None:

#             nextNode = temp.next

#             while nextNode != None and nextNode.val == temp.val:
#                 nextNode = nextNode.next

#             temp.next = nextNode

#             if nextNode != None:
#                 nextNode.prev = temp

#             temp = temp.next

#         return head


# l = LinkedList()

# l.head = Node(1)

# l.head.next = Node(1)
# l.head.next.prev = l.head

# l.head.next.next = Node(1)
# l.head.next.next.prev = l.head.next

# l.head.next.next.next = Node(2)
# l.head.next.next.next.prev = l.head.next.next

# l.head.next.next.next.next = Node(3)
# l.head.next.next.next.next.prev = l.head.next.next.next

# l.head.next.next.next.next.next = Node(3)
# l.head.next.next.next.next.next.prev = l.head.next.next.next.next

# l.head.next.next.next.next.next.next = Node(4)
# l.head.next.next.next.next.next.next.prev = l.head.next.next.next.next.next



# result = l.removeDoublicate(l.head)


# temp = result

# while temp != None:
#     print(temp.val, end=" <-> ")
#     temp = temp.next

# print("None")


#Leetcode 21 Merge sorted linkedlist
#brute Time Complexity	O((N + M) log(N + M))     Space Complexity	O(N + M)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def mergeLL(self, head1, head2):
#         arr = []

        
#         temp1 = head1

#         while temp1 is not None:
#             
#             arr.append(temp1.val)
#             temp1 = temp1.next

        
#         temp2 = head2

#         while temp2 != None:
#             
#             arr.append(temp2.val)
#             temp2 = temp2.next

#         arr.sort()

#         #Convert array into Linkedlist
#         head = Node(arr[0])
#         temp = head

#         for i in range(1, len(arr)):
#             temp.next = Node(arr[i])
#             temp = temp.next

#         return head


# l = LinkedList()

# l1 = LinkedList()

# l1.head = Node(2)
# l1.head.next = Node(4)
# l1.head.next.next = Node(8)
# l1.head.next.next.next = Node(10)


# l2 = LinkedList()

# l2.head = Node(1)

# l2.head.next = Node(3)

# l2.head.next.next = Node(3)
# l2.head.next.next.next = Node(6)
# l2.head.next.next.next.next = Node(11)
# l2.head.next.next.next.next.next = Node(14)


# # Merge

# l = LinkedList()

# result = l.mergeLL(l1.head, l2.head)


# # Print result

# temp = result

# while temp is not None:
#     print(temp.val, end=" -> ")
#     temp = temp.next

# print("None")


# #Optimal   Time Complexity  = O(N + M)      Space Complexity = O(1)
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def mergeLL(self, head1, head2):
#         t1 = head1
#         t2 = head2

#         dNode = Node(-1)  # FIXED
#         temp = dNode

#         while t1 != None and t2 != None:

#             if t1.val < t2.val:
#                 temp.next = t1
#                 temp = t1
#                 t1 = t1.next

#             else:
#                 temp.next = t2
#                 temp = t2
#                 t2 = t2.next

#         if t1:
#             temp.next = t1
#         else:
#             temp.next = t2

#         return dNode.next  # FIXED


# l1 = LinkedList()

# l1.head = Node(2)
# l1.head.next = Node(4)
# l1.head.next.next = Node(8)
# l1.head.next.next.next = Node(10)


# l2 = LinkedList()

# l2.head = Node(1)
# l2.head.next = Node(3)
# l2.head.next.next = Node(3)
# l2.head.next.next.next = Node(6)
# l2.head.next.next.next.next = Node(11)
# l2.head.next.next.next.next.next = Node(14)


# # Merge

# l = LinkedList()

# result = l.mergeLL(l1.head, l2.head)


# # Print result

# temp = result

# while temp != None:
#     print(temp.val, end=" -> ")
#     temp = temp.next

# print("None")

#Leetcode:

#brute:
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev=None
#         self.child=None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def flattening_LL(self, head1):
#         arr=[]
#         temp=self.head
#         while temp != None:
#             t2=temp
#             while (t2 !=None):
#                 arr.append(t2.val)
#                 t2=t2.child
#             temp=temp.next
#             arr.sort()
#         #onvert array into Linkedlist
#         head = Node(arr[0])
#         temp = head

#         for i in range(1, len(arr)):
#             temp.next = Node(arr[i])
#             temp = temp.next
            

#         return head

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        self.child = None


class LinkedList:
    def __init__(self):
        self.head = None

    def flattening_LL(self, head1):

        arr = []

        temp = head1

        while temp != None:

            # Store main list value
            arr.append(temp.val)

            # Store child list values
            t2 = temp.child

            while t2 != None:
                arr.append(t2.val)
                t2 = t2.next

            temp = temp.next

        # Convert array into linked list

        if len(arr) == 0:
            return None

        head = Node(arr[0])
        temp = head

        for i in range(1, len(arr)):

            newNode = Node(arr[i])

            temp.next = newNode
            newNode.prev = temp

            temp = temp.next

        return head


# --------------------------------
# Create Main Linked List
# --------------------------------

l = LinkedList()

l.head = Node(1)

l.head.next = Node(2)
l.head.next.prev = l.head

l.head.next.next = Node(3)
l.head.next.next.prev = l.head.next

l.head.next.next.next = Node(4)
l.head.next.next.next.prev = l.head.next.next


# --------------------------------
# Create Child Linked List
# --------------------------------

child1 = Node(7)

child1.next = Node(8)
child1.next.prev = child1

child1.next.next = Node(9)
child1.next.next.prev = child1.next


# --------------------------------
# Connect Child List to Node 3
# --------------------------------

l.head.next.next.child = child1


# --------------------------------
# Flatten Linked List
# --------------------------------

result = l.flattening_LL(l.head)


# --------------------------------
# Print Flattened Linked List
# --------------------------------

temp = result

while temp != None:
    print(temp.val, end=" -> ")
    temp = temp.next

print("None")