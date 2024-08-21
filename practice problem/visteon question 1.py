def findmissing(arr,k):
    num_set=set(arr)
    rept_num=None
    missing=None
    for i in range(1,k+1):
        if i not in num_set:
            missing=i
            break

    for j in range(k-1,-1,-1):
        if arr[j] in num_set:
            rept_num=arr[j]
            break


    return [missing,rept_num]


ar=[6,1,2,3,5,5,7]
l=len(ar)
print(findmissing(ar,l))
