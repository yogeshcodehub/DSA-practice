def move_zeros(arr):
    i=0
    for j in range(len(arr)):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    return arr

arr=[1,2,3,0,0,0,0,0,0,4]
print(move_zeros(arr))