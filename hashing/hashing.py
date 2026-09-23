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
        print(hash_table[complement],i)
    hash_table[num[i]]=i
print()
        