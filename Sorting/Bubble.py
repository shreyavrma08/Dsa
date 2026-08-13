#Average Case=O(n^2)   Sc=O(1)
def bubblesort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                # j+=1
    return nums
nums=[5,1,6,8,2,4,9]
print(bubblesort(nums))

def bubblesort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        is_swap=False
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                is_swap=True
        if is_swap==False:
            return
nums=[1,2,4,5,9,10,12,14]
print(bubblesort(nums))