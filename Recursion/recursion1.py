def reverse(nums,left,right):
    # left=0 
    # right =len(nums)-1
    if left>= right:
        return 
    nums[left],nums[right]=nums[right],nums[left]
    reverse(nums,left +1, right-1)
    


nums=[5,9,8,3,6,7,1,4,2]
reverse(nums,0,len(nums)-1)
print(nums)

reverse(nums,2,5)
print(nums)