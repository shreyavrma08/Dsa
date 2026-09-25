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

#Leetcode 18 4Sum TC=O(n^3)        Sc=(1)
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


#Leetcode 128 LOngest consecutive 
def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


# --- Example Function Call ---

# Sample list: The longest sequence here is, which has a length of 4
test_numbers = [100, 4, 200, 1, 3, 2]

# Call the function and save the result
result = longest_consecutive(test_numbers)

# Print the result to the console
print(f"The length of the longest consecutive sequence is: {result}")


#LOngest consecutive sequencce tc=O(n)   and sc=o(n#)
def largest_zero_sum(nums):
    hash_map = {}
    sum = 0
    longest = 0

    for i in range(len(nums)):
        sum += nums[i]

        if sum == 0:
            #
            longest = i + 1

        elif sum in hash_map:
            length = i - hash_map[sum]

            if length > longest:
                longest = length

        else:
            hash_map[sum] = i

    return longest


nums = [15, -2, 2, -8, 1, 7, 10, 23]

print(largest_zero_sum(nums))




       

        