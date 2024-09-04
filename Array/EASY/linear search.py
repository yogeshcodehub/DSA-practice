def search(arr,k):

    for i,j in enumerate  (arr):
        if k ==j:
            return 'k is in index = ', i

arr=[1,2,3,4,5,6]
k=5
print(search(arr,k))
