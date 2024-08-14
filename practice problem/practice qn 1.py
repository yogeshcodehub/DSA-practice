def find_missing(arr,k):
    num_set=set(arr)
    missing=[]
    for i in range(1,k+1):
        if i not in num_set:
            missing.append(i)
    rept=set()
    repetting=None
    for j in arr:
        if j in rept:
            repetting=j
            break
        rept.add(j)
    return [min(missing),repetting]

arr=[6,6,1,2,3,4,5,5]
k=len(arr)
print(find_missing(arr,k))

