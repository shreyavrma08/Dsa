# #Same as leetcode=344 reverse of string 
# #Tc= O(n)  and Sc=O(n)
# def reverse(nums,left,right):
#     # left=0 
#     # right =len(nums)-1
#     if left>= right:
#         return 
#     nums[left],nums[right]=nums[right],nums[left]
#     reverse(nums,left +1, right-1)
    


# nums=[5,9,8,3,6,7,1,4,2]
# reverse(nums,0,len(nums)-1)
# print(nums)

# # reverse(nums,2,5)
# # print(nums)


#Check string is palindrome using while loop
#tc=O(n)  Sc=O(1)
def isPalindrome(s):
    n=len(s)
    left=0
    right=n-1
    while left<right:
        if s[left] != s[right]:
            return False
        left +=1
        right-=1
    return True
s="anbcddcbna"
print(isPalindrome(s))

#Check string is palindrome using while recursion
def isPalindrome(s,left,right):
    
    if left>=right:
        return True
    if s[left] != s[right]:
        return False
    return isPalindrome(s,left+1,right-1)
s="anbcddcbna"
print(isPalindrome(s,0,len(s)-1))


# def isPalindrome(self, s):

#         left = 0
#         right = len(s) - 1

#         while left < right:

#             while left < right and not (s[left].isalpha() or s[left].isdigit()):
#                 left += 1

#             while left < right and not (s[right].isalpha() or s[right].isdigit()):
#                 right -= 1

#             if s[left].lower() != s[right].lower():
#                 return False

#             left += 1
#             right -= 1

#         return True

# s="anBcddCbna"
# print(isPalindrome(s,0,len(s)))

#Leetcode 125 Valid palinedrome.
def isPalindrome(s, left, right):

    if left >= right:
        return True

    if s[left].lower() != s[right].lower():
        return False

    return isPalindrome(s, left + 1, right - 1)


s = "mAdam"

print(isPalindrome(s, 0, len(s) - 1))
      
