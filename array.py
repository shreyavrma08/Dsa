

                       #Leetcode 66
from numpy import *
digits=[1,2,3]
nums=int("".join(map(str,digits)))
# print(nums)
nums+=1
# print(nums)
digits=list(map(int,str(nums))) 
print(digits)


#leetcode 26
from numpy import *
nums = [1,1,2,2,5]

k = 1
for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        nums[k] = nums[i]
        k += 1

print(nums[0:k]) #we use this becaues we have to print all the elemt of k variable


#                             leetcode53(simple logic)
# from numpy import *
nums=[-2,1,-3,4,-1,2,1,-5,4]
n=len(nums)
maxi=float("-inf")
for i in range(0,n):
    total=0
    for j in range(i,n):
        total=total+nums[j]
        maxi=max(maxi,total)
print(maxi)

 #                       OR
n=len(nums)
maxi=float("-inf")
total=0
for i in range(0,n):
    total=total+nums[i]
    maxi=max(maxi,total)
    if total <0:
        total=0
print(maxi)

 #                          Leetcode 121
prices=[7,2,1,5,6,4,8]
n=len(prices)
max_profit=0

for i in range(0,n):

    for j in range(i+1,n):
        if prices[j]>prices[i]:
            p=prices[j]-prices[i]
            max_profit=max(max_profit,p)
print(max_profit)#tc=0(n^2), Sc=0(1)
#                                    OR
prices=[7,2,1,5,6,4,8]
max_profit=0
min_price=float("inf")
n=len(prices)

for i in range(0,n):
    min_price=min(min_price,prices[i])
    max_profit=max(max_profit,prices[i]-min_price)
print(max_profit)


#                          Leetcode 2149
nums=[5,10,-3,-1,-10,6]  
n=len(nums)
pos=[]
neg=[]
for num in nums:
    
    if num >0:
        pos.append(num)
    else:
        neg.append(num)
result = []
i = 0

while i < len(pos) and i < len(neg):
    result.append(pos[i])
    result.append(neg[i])
    i += 1
print(result)
                

                #leetcode- 128
nums=[1,99,101,98,2,5,3,100,1,1]
n=len(nums)
max_count=0
for i in range(0,n):
    num=nums[i]
    count=1
    while num+1 in nums:
        count+=1
        num=num+1
    max_count=max(max_count,count)
print(max_count)
               #OR
nums=[1,99,101,98,2,5,3,100,1,1]
n=len(nums)
nums.sort()
count=0
last_smaller=-float('-inf')
longest=0
for i in range(0,n):
    num=nums[i]
    if num-1==last_smaller:
        count +=1
        last_smaller=num
    elif num != last_smaller:
        count =1
        last_smaller=num
    longest=max(longest,count)
print(longest)

    #or

nums=[1,99,101,98,2,5,3,100,1,1]
n=len(nums)
my_set=set()
for i in range(0,n):
    my_set.add(nums[i])
longest=0
for i in my_set:
    if i -1 not in my_set:
        x=i
        count=1
        while x + 1 in my_set:
            count +=1
            x+=1

        longest=max(longest,count)
print(longest)

 #                   leetcode-73

nums=[[7,9,2,3],[20,8,0,10],[29,0,10,5],[4,14,6,7]]
rows=len(nums)
columns=len(nums[0])

row_mark = [0] * rows
col_mark = [0] * columns

for i in range(0,rows):
    for j in range(0,columns):
        if nums[i][j] ==0:
            row_mark[1] = 1
            col_mark[2] = 1
            row_mark[2] = 1
            col_mark[1] = 1

for i in range(rows):
    for j in range(columns):
        if row_mark[i] == 1 or col_mark[j] == 1:
            nums[i][j] = 0
print(nums,end=" ",)
for row in nums:
    print(row)
                   
#                    leetcode-48
nums=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(nums)
cols=len(nums[0])
result=[[0]*rows for  _  in range(cols)]
# print (result)
for i in range(rows):
    for j in range(cols):
        result[j][i]= nums[i][j]
# print(result)
for rows in result:
    rows[0], rows[2] = rows[2], rows[0]
print(result,end=" ")
           



 #                       leetcode-54
def spiralOrder( matrix):
    if not matrix or not matrix[0]:
        return []
    result= []
    #initialize pointer for traverrsal.
    top, left =0, 0
    bottom,right = len(matrix) -1, len(matrix[0]) -1

    #Traverse the matrix in a spiral order.
    while top <= bottom and left <= right:
        #Move left to right across the top row.
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top +=1

        #Move top to bottom along the right column.
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -=1

        #Move right to left across the bottom roe(if still valid).
        if top <=bottom:
            for i in range(right, left -1,-1):
                result.append(matrix[bottom][i])
            bottom -=1

        #Move bottom to top along the left column(if still valid).
        if left <= right:
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left += 1
    return result

matrix=[[1,2,3,4,5,6],[20,21,22,23,24,7],[19,32,33,34,25,8],[18,31,36,35,26,9],[17,30,29,28,27,10],[16,15,14,13,12,11]]
print(spiralOrder(matrix))




#                               leetcode-15
#brute
nums=[-1,0,1,2,-3,-4]
n=len(nums)
my_set=set()


for i in range(n):
  
    for j in range(i+1,n):
       
        for k in range(j+1,n):
           
            if nums[i]+nums[j]+nums[k] == 0:
                temp=[nums[i],nums[j],nums[k]]
                temp.sort()
                my_set.add(tuple(temp))
result = [list(triplet) for triplet in my_set]
print(result)
                         #or better
arr=[-1,0,1,2,-3,-4]
n=len(arr)
result=set()
for i in range(0,n):
    my_set=set()
    for j in range(i+1,n):
        third=-(arr[i]+arr[j])
        if third in my_set:
              temp=[arr[i],arr[j],third]
              temp.sort()
              result.add(tuple(temp))
        my_set.add(arr[j])
result=[list(triplet) for triplet in result]
print(result)
        
                             #or optimal solution

class Solution:
    def threeSum(self,nums):
        ans=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            if i !=0 and nums[i]==nums[i-1]:
                continue

            #Moving the 2 pointers
            j=i+1
            k=n-1
            while j<k:
                total_sum = nums[i] +nums[j]+ nums[k]
                if total_sum<0:
                    j+=1
                elif total_sum>0:
                    k=-1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    #skip the duplicates if occured
                    while j<k and nums[j]==nums[j-1]:
                        j +=1
                    while j<k and nums[k]==nums[k+1]:
                        k -=1

        return ans
nums=[-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
sol=Solution()
print(sol.threeSum(nums))

#                  Leetcode!8 Foursum
nums=[1,0,-1,0,-2,2]
n=len(nums)
my_set=set()
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
             for l in range(k+1,n):
                total=nums[i]+nums[j]+nums[k]+nums[l]
                if total == 0:
                    temp=[nums[i],nums[j],nums[k],nums[l]]
                    temp.sort()
                    my_set.add(tuple(temp))
result=[]
for ans in my_set:
    result.append(list(ans))
print(result)

#TC= O(n^4)
#SC= O(n)

                   #OR better solution
nums=[1,0,-1,5,-2,2,0,9]
n=len(nums)
target=0
for i in range(n):
    for j in range(i+1,n):
        hash_set=set()
        for k in range(j+1,n):
            total=nums[i]+nums[j]+nums[k]
            fouth= target-total
            if fouth in hash_set:
                temp=[nums[i],nums[j],nums[k]]
                temp.sort()
                my_set.append(tuple(temp))
            hash_set.add(nums[k])
result=[]
for ans in my_set:
    result.append(list(ans))
print(result)

# TC= o(n^3)    and SC=O(n)


                       #OR (Optimal)
def fourSome(nums, target):
    nums.sort()
    n = len(nums)
    ans = []

    for i in range(n):

        # skip duplicate i
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n):

            # skip duplicate j
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            k = j + 1
            l = n - 1

            while k < l:

                total = nums[i] + nums[j] + nums[k] + nums[l]

                if total == target:

                    ans.append([nums[i], nums[j], nums[k], nums[l]])

                    k += 1
                    l -= 1

                    # skip duplicate k
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1

                    # skip duplicate l
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1

                elif total < target:
                    k += 1

                else:
                    l -= 1

    return ans


nums = [1,1,1,1,2,2,3,3,3,4,4,4,5,5]
target = 8

print(fourSome(nums, target))

# TC=o(n^2*n)         and  SC=O(no. of ans)=O(1)