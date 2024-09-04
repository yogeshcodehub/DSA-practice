def rotate_by_n(arr,n):

    n=n%len(arr)

    return arr[n:]+arr[:n]

arr=[1,2,3,4,5]
n=2
print(rotate_by_n(arr,n))
