def second_largest(arr):
    l=float('-inf')
    sl=float('-inf')
    for i in arr:
        if i>l:
            sl=l
            l=i
        elif i>sl and i!=l:
            sl=i
    return sl

arr=[1,2,3,4,5,6]
print(second_largest(arr))
