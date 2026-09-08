nums=[3,1,2,4,1,5,2,6,4]
#MERGE TO SORTED ARRAY
left=[1,2,3,4]
right=[1,1,3,4,5,6,7]
def merge_sort(left,right):
    result=[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
#if any of the array becomes empty
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result

print(merge_sort(left,right))