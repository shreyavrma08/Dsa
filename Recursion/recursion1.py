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

#Check string is palindrome using while loop



        
      
