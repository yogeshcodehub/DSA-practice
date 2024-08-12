def findmissing(arr,k):
    num_set=set(arr)
    rept=set()
    rept_num=None
    missing=[]
    for i in range(1,k+1):
        if i not in num_set:
            missing.append(i)

    for j in range(k-1,-1,-1):
        if arr[j] in rept:
            rept_num=arr[j]
            break
        rept.add(arr[j])


    return [min(missing),rept_num]


ar=[2,2,3,4,5,6,6]
l=len(ar)
print(findmissing(ar,l))
