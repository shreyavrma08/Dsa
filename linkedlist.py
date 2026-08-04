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
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def deleteMid(self, head):

        # Empty list or single node
        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        prev = None

        while fast is not None and fast.next is not None:

            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete middle node
        prev.next = slow.next

        return head


# Create linked list

l = LinkedList()

l.head = Node(1)
l.head.next = Node(2)
l.head.next.next = Node(4)
l.head.next.next.next = Node(5)
l.head.next.next.next.next = Node(2)


# Delete middle node

result = l.deleteMid(l.head)


# Print linked list

temp = result

while temp is not None:
    print(temp.val, end=" -> ")
    temp = temp.next

print("None")