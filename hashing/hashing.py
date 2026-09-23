def f(number,arr):
    count=0
    n=len(arr)
    for i in range(n):
        if arr[i] == number:
            count=count+1
    return count
number=1
arr=[1,2,1,1,3,4]
result=f(number,arr)
print(result)


#Leetcode 1: two sum TC=O(n)   SC=O(n)
num=[2,6,5,8,11]
target=14
hash_table={}
for i in range(len(num)):
    complement=target - num[i]
    if complement in hash_table:
        print((hash_table[complement],i))
    hash_table[num[i]]=i
print()


def fourSum(nums,target):
    nums.sort()
    result=[]
    n=len(nums)
    for i in range(n-3):
        #Skip duplicate i
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n-2):
            #Skip duplicate j
            if j>i+1 and nums[j] == nums[j-1]:
                continue
            left=j+1
            right=n-1
            while left< right:
                total= nums[i]+nums[j]+nums[left]+nums[right]
                if total==target:
                    result.append([
                        nums[i],
                        nums[j],
                        nums[left],
                        nums[right]
                    ])
                    # Skip duplicate left values
                    while left < right and nums[left]==nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left +=1
                    right_=1
                elif total <target:
                    left +=1
                else:
                    right-=1
        return result
nums = [4,3,3,4,4,2,1,2,1,1]
target = 9

print(fourSum(nums, target))


       

        