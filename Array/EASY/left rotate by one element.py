def rotate(arr):
    temp=arr[0]
    arr.remove(arr[0])
    arr.append(temp)

    return arr

arr=[1,2,3,4,5,6]
print(rotate(arr))