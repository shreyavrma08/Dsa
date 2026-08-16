#increasing order 
# TC O(n(n+1))/2  almost equal to O(n^2)  SC=O(1)
def insertion(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums
nums=[2,5,6,3,8,9,10,7,1]
print(insertion(nums))

#Decreasing order
def insertion(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]<key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums
nums=[2,5,6,3,8,9,10,7,1]
print(insertion(nums))


