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