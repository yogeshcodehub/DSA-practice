def isSorted(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True


arr=[1,10,4,5,6]
print(isSorted(arr))